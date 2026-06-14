"""
Tilted Cortex Node (tide gates WHETHER; the applied skew A steers WHICH WAY)
============================================================================
The Primed Cortex could resonate or not (the slow tide, WHETHER) and could recall
content (the islands, WHAT) -- but its recall was a symmetric gradient settle, so
it had no direction. The arrow read off the winner traffic sat near zero because
nothing was driving a current. This node adds the third role: a fast, local,
APPLIED skew operator A -- the ephaptic tilt -- that steers which way the recall
runs, gated by the tide.

Three roles, now all in code:
  - tide   (slow scalar, the chemical primer)   -> WHETHER it can resonate   [beta, gate]
  - P_k    (stored patterns, the islands)        -> WHAT there is to recall   [content]
  - tilt   (applied skew A, the ephaptic field)  -> WHICH WAY the recall runs [direction]

The operator (grounded, not invented):
  Built cyclically over the cortex's own nodes, A is the antisymmetric transition
  connectivity of Sompolinsky & Kanter (1986) / Kleinfeld (1986) -- the textbook
  sequence-memory operator. In the recall iteration the symmetric term settles the
  field into a basin (gradient, curl-free, cheap); the skew term A adds a
  divergence-free CURRENT that pushes the descent from one basin toward its
  successor (solenoidal, the arrow, the part you pay to turn). That is exactly the
  gradient/curl split of `the_unnatural_direction.md` made into a drift term:

      s <- norm( leak*s + content(w@P)  +  tilt * normalized(A @ (P@s)) @ P )
                          \___ settle ___/    \________ steer ________/

  tilt is GATED BY THE TIDE: tilt_eff = tilt_signal * tide. No water, no steering --
  you cannot turn a boat that is stranded on dry rock. Flip the sign of tilt and the
  recall runs the cycle the other way; the winner-traffic arrow flips with it
  (forward vs reverse replay; Foster & Wilson 2006).

HONEST SCOPE:
  - The cyclic ORDER here is SEEDED from the node spawn order (= presentation
    order), not learned from STDP in this node. The learned-from-experience version
    is the transition memory T in `predictivecortexnode.py`; fold that in to make
    the order earned rather than configured.
  - The fast `tilt` input is a signed scalar STRENGTH + CHIRALITY (the local field's
    amplitude and direction). The operator's GEOMETRY lives here, in the substrate's
    own patterns -- the node just sets how hard and which way the current pushes.
  - Costs/dynamics are structural proxies, as everywhere in this line. That the
    biological ephaptic field IS this applied A remains the bet.

Back-compatible: with no `tilt` connected and tilt_gain=0 this is the Primed Cortex.

Do not hype. Do not lie. Just show.
PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.
"""
import numpy as np
import cv2
from collections import deque

import __main__
BaseNode = __main__.BaseNode
QtGui = __main__.QtGui


def _norm(v): return v / (np.linalg.norm(v) + 1e-9)
def _softmax(x, b):
    x = b * (x - x.max()); e = np.exp(x); return e / (e.sum() + 1e-12)


class TiltedCortexNode(BaseNode):
    NODE_CATEGORY = "Cognition"
    NODE_COLOR = QtGui.QColor(90, 175, 150)  # tilted mycelial green

    def __init__(self, beta=18.0, leak=0.25, familiar=0.30, novel=0.20,
                 alpha=0.20, budget=48, gain_floor=0.06, gate_lo=0.25, gate_hi=0.60,
                 tilt_gain=0.6, tilt_sign=1):
        super().__init__()
        self.node_title = "Tilted Cortex (whether + which way)"
        self.inputs = {
            'query_vec':    'spectrum',
            'tide':         'signal',     # slow scalar: WHETHER it can resonate
            'tilt':         'signal',     # fast signed scalar: WHICH WAY (ephaptic field strength+sign)
            'inject_token': 'spectrum',
            'learn_enable': 'signal',
            'atp':          'signal',
        }
        self.outputs = {
            'recall_vec':    'spectrum',
            'recall_img':    'image',
            'expressed_img': 'image',
            'confidence':    'signal',
            'expressed_conf':'signal',
            'express':       'signal',
            'n_nodes':       'signal',
            'arrow':         'signal',    # winner-traffic skew: now strongly signed, flips with tilt
            'demand':        'signal',
            'viz':           'image',
        }
        self.beta = float(beta); self.leak = float(leak)
        self.familiar = float(familiar); self.novel = float(novel)
        self.alpha = float(alpha); self.budget = int(budget)
        self.gain_floor = float(gain_floor)
        self.gate_lo = float(gate_lo); self.gate_hi = float(gate_hi)
        self.tilt_gain = float(tilt_gain); self.tilt_sign = 1 if int(tilt_sign) >= 0 else -1

        self.P = []
        self.dim = None
        self._A = None; self._n_A = 0
        self.recall_vec = None
        self.confidence = 0.0; self.expressed_conf = 0.0; self.express = 1.0
        self.arrow = 0.0; self.demand = 0.0; self.tide = 1.0; self.tilt_eff = 0.0
        self.last_winner = -1
        self.C = np.zeros((self.budget, self.budget))
        self.prev_onehot = np.zeros(self.budget)
        self.display_img = np.zeros((160, 256, 3), dtype=np.uint8)
        self.recall_img = np.zeros((16, 16, 3), dtype=np.float32)
        self.expressed_img = np.zeros((16, 16, 3), dtype=np.float32)

    # -------------------------------------------------------------
    def _ensure(self, v):
        if self.dim is None:
            self.dim = len(v)
            self.recall_vec = np.zeros(self.dim, np.float32)

    def _smooth(self, x, lo, hi):
        t = float(np.clip((x - lo) / (hi - lo + 1e-9), 0.0, 1.0))
        return t * t * (3.0 - 2.0 * t)

    def _build_A(self, n):
        # cyclic Sompolinsky-Kanter skew over the n nodes: k -> k+1 (mod n)
        A = np.zeros((n, n))
        for k in range(n):
            j = (k + 1) % n
            A[j, k] += 1.0
            A[k, j] -= 1.0
        return A

    def _refresh_A(self):
        n = len(self.P)
        if n != self._n_A:
            self._A = self._build_A(n) if n > 1 else None
            self._n_A = n

    def _recall(self, query, beta_eff, tilt, steps=12):
        s = _norm(query.copy()); P = np.stack(self.P); n = len(self.P)
        A = self._A if (self._A is not None and self._A.shape[0] == n) else None
        for _ in range(steps):
            o = P @ s
            w = _softmax(o, beta_eff)
            content = w @ P                       # gradient settle into a basin (WHAT)
            if A is not None and abs(tilt) > 1e-6:
                drift = (A @ o) @ P               # solenoidal current toward the successor (WHICH WAY)
                dn = np.linalg.norm(drift)
                if dn > 1e-9:
                    content = content + tilt * (drift / dn)
            s = _norm(self.leak * s + content)
        return s

    def _update_arrow(self, winner):
        oh = np.zeros(self.budget)
        if 0 <= winner < self.budget: oh[winner] = 1.0
        self.C = 0.97 * self.C + 0.03 * np.outer(oh, self.prev_onehot)
        self.prev_onehot = oh
        A = 0.5 * (self.C - self.C.T)
        n = min(len(self.P), self.budget)
        self.arrow = float(sum(A[k, (k + 1) % n] - A[(k + 1) % n, k] for k in range(n))) if n > 1 else 0.0

    # -------------------------------------------------------------
    def step(self):
        q = self.get_blended_input('query_vec', 'first')
        inj = self.get_blended_input('inject_token', 'first')
        learn = self.get_blended_input('learn_enable', 'sum')
        atp = self.get_blended_input('atp', 'sum')
        tide = self.get_blended_input('tide', 'sum')
        tilt_in = self.get_blended_input('tilt', 'sum')
        self.tide = 1.0 if tide is None else float(np.clip(tide, 0.0, 1.0))
        learn_on = True if learn is None else (float(learn) > 0.5)

        src = q if q is not None else inj
        if src is None:
            self._render(); return
        v = np.array(src, dtype=np.float32)
        self._ensure(v)
        if len(v) != self.dim:
            v = (v[:self.dim] if len(v) > self.dim else np.pad(v, (0, self.dim - len(v))))
        q = _norm(v)

        if len(self.P) == 0:
            self.P.append(q.copy()); self._refresh_A()
        P = np.stack(self.P)
        ov = P @ q; best = int(np.argmax(ov)); bestov = float(ov[best])

        beta_eff = max(1.0, self.beta * (self.gain_floor + (1.0 - self.gain_floor) * self.tide))

        # the ephaptic tilt: signed strength * chirality, GATED BY THE TIDE
        base_tilt = float(tilt_in) if tilt_in is not None else (self.tilt_gain * self.tilt_sign)
        self.tilt_eff = base_tilt * self.tide

        # INNER side: settle (content) + steer (applied skew A)
        s = self._recall(q, beta_eff, self.tilt_eff)
        self.recall_vec = s.astype(np.float32)
        self.confidence = float(_softmax(P @ s, beta_eff).max())

        # expression gate (stored vs accessible)
        self.express = self._smooth(self.tide, self.gate_lo, self.gate_hi)
        self.expressed_conf = self.confidence * self.express
        self.demand = self.expressed_conf if self.expressed_conf > 0.5 else 0.05

        # learning (consolidate / spawn), ATP-gated; rebuild A when a node is added
        atp_ok = (atp is None) or (float(atp) > 0.25)
        spawned = False
        if learn_on:
            if bestov >= self.familiar:
                self.P[best] = _norm((1 - self.alpha) * self.P[best] + self.alpha * q)
            elif bestov < self.novel and len(self.P) < self.budget and atp_ok:
                self.P.append(q.copy()); best = len(self.P) - 1; spawned = True
                self._refresh_A()

        # the winner the field actually lands on (after steering) -> arrow
        P2 = np.stack(self.P)
        win = int(np.argmax(P2 @ s))
        self.last_winner = win
        self._update_arrow(win)

        side = int(np.sqrt(self.dim))
        if side * side == self.dim:
            g = self.recall_vec.reshape(side, side)
            g = (g - g.min()) / (np.ptp(g) + 1e-9)
            self.recall_img = np.stack([g, g, g], -1).astype(np.float32)
            self.expressed_img = (self.recall_img * self.express).astype(np.float32)

        self._render(spawned)

    # -------------------------------------------------------------
    def get_output(self, port_name):
        if port_name == 'recall_vec':     return self.recall_vec
        if port_name == 'recall_img':     return self.recall_img
        if port_name == 'expressed_img':  return self.expressed_img
        if port_name == 'confidence':     return self.confidence
        if port_name == 'expressed_conf': return self.expressed_conf
        if port_name == 'express':        return self.express
        if port_name == 'n_nodes':        return float(len(self.P))
        if port_name == 'arrow':          return self.arrow
        if port_name == 'demand':         return self.demand
        if port_name == 'viz':            return self.display_img
        return None

    def _render(self, spawned=False):
        h, w = 160, 256
        img = np.zeros((h, w, 3), dtype=np.uint8)

        r = (np.clip(self.expressed_img, 0, 1) * 255).astype(np.uint8)
        if r.shape[0] >= 2:
            r = cv2.resize(r, (84, 84), interpolation=cv2.INTER_NEAREST)
            img[22:106, 8:92] = r
        cv2.putText(img, "accessible recall", (8, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.32, (150, 200, 170), 1)

        cv2.putText(img, f"tide {self.tide:.2f}", (104, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.34, (70, 170, 230), 1)
        ex = float(np.clip(self.express, 0, 1))
        cv2.rectangle(img, (104, 30), (104 + int(ex * 140), 42), (90, 220, 140), -1)
        cv2.rectangle(img, (104, 30), (244, 42), (80, 90, 90), 1)

        # tilt indicator: which way, how hard
        td = ">>>" if self.tilt_eff > 1e-3 else ("<<<" if self.tilt_eff < -1e-3 else " - ")
        tcol = (90, 200, 130) if self.tilt_eff > 0 else ((120, 130, 255) if self.tilt_eff < 0 else (120, 120, 130))
        cv2.putText(img, f"tilt {self.tilt_eff:+.2f} {td}", (104, 58),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.34, tcol, 1)

        cx, cy, R = 150, 98, 26
        n = len(self.P)
        for k in range(n):
            a = 2 * np.pi * k / max(n, 1)
            x = int(cx + R * np.cos(a)); y = int(cy + R * np.sin(a))
            c = (80, 230, 255) if k == self.last_winner else (70, 90, 80)
            cv2.circle(img, (x, y), 3, c, -1)
        cv2.putText(img, f"nodes {n}", (8, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.34, (150, 200, 170), 1)
        if spawned:
            cv2.putText(img, "+SPAWN", (190, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (90, 255, 160), 1)

        state = "PRIMED" if self.express > 0.5 else "inaccessible"
        scol = (90, 220, 140) if self.express > 0.5 else (120, 120, 140)
        cv2.putText(img, f"{state}   arrow {self.arrow:+.3f}", (8, 140),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.33, scol, 1)
        cv2.putText(img, "tide=whether  content=what  tilt=which way",
                    (8, 154), cv2.FONT_HERSHEY_SIMPLEX, 0.29, (120, 130, 140), 1)
        self.display_img = img

    def get_display_image(self):
        return QtGui.QImage(self.display_img.data, 256, 160, 256 * 3,
                            QtGui.QImage.Format.Format_RGB888)

    def get_config_options(self):
        return [
            ("Beta (recall sharpness)", "beta", self.beta, "float"),
            ("Field leak", "leak", self.leak, "float"),
            ("Familiar thr", "familiar", self.familiar, "float"),
            ("Novel thr", "novel", self.novel, "float"),
            ("Consolidation alpha", "alpha", self.alpha, "float"),
            ("Gain floor (beta at tide=0)", "gain_floor", self.gain_floor, "float"),
            ("Express gate lo", "gate_lo", self.gate_lo, "float"),
            ("Express gate hi", "gate_hi", self.gate_hi, "float"),
            ("Tilt gain (if no tilt input)", "tilt_gain", self.tilt_gain, "float"),
            ("Tilt sign (1 fwd / -1 rev)", "tilt_sign", self.tilt_sign, None),
            ("Node budget", "budget", self.budget, None),
        ]

    def set_config_options(self, options):
        for k in ("beta", "leak", "familiar", "novel", "alpha",
                  "gain_floor", "gate_lo", "gate_hi", "tilt_gain"):
            if k in options: setattr(self, k, float(options[k]))
        if "tilt_sign" in options:
            self.tilt_sign = 1 if int(options["tilt_sign"]) >= 0 else -1
        if "budget" in options:
            self.budget = int(options["budget"])
            self.C = np.zeros((self.budget, self.budget)); self.prev_onehot = np.zeros(self.budget)
