"""
Ephaptic Tilt Node (the fast local field: WHICH WAY)
====================================================
The fast counterpart to the slow Neuromodulatory Tide. Where the tide is a slow,
global, scalar readiness (WHETHER the substrate can resonate), this is the fast,
local, directional field (WHICH WAY the recall runs). It is the engine stand-in
for the ephaptic field carrying the skew operator A.

What it outputs is deliberately minimal: a SIGNED STRENGTH -- the amplitude and
chirality of the local current. The OPERATOR'S GEOMETRY does not live here; it
lives in the Tilted Cortex, built from the substrate's own stored patterns (the
Sompolinsky-Kanter cyclic skew). This node only says how hard the current pushes
and which way. That division is on purpose: a fast field sets amplitude and sign;
the carved structure sets the shape.

It runs faster than the tide (ms-scale in biology; here a short reversal period),
and can hold a direction or periodically REVERSE it. When it reverses, the Tilted
Cortex's recall walks the cycle the other way and its winner-traffic arrow flips
sign -- forward vs reverse replay, live.

Outputs:
  tilt   signed scalar = strength * chirality (feed -> Tilted Cortex `tilt`)
  chi    the chirality sign alone (+1 / -1)
  meter  amplitude bar + direction arrow

Do not hype. Do not lie. Just show.
PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.
"""
import numpy as np
import cv2

import __main__
BaseNode = __main__.BaseNode
QtGui = __main__.QtGui


class EphapticTiltNode(BaseNode):
    NODE_CATEGORY = "Cognition"
    NODE_COLOR = QtGui.QColor(60, 150, 120)  # ephaptic teal-green

    def __init__(self, strength=0.7, reverse_every=360, hold_sign=1):
        super().__init__()
        self.node_title = "Ephaptic Tilt (fast local field)"
        self.inputs = {
            'flip': 'signal',   # OPTIONAL: a rising signal flips chirality on demand
        }
        self.outputs = {
            'tilt':  'signal',
            'chi':   'signal',
            'meter': 'image',
        }
        self.strength = float(strength)
        self.reverse_every = int(reverse_every)   # frames between auto-reversals; 0 = never
        self.sign = 1 if int(hold_sign) >= 0 else -1
        self.t = 0
        self.was_flip = False
        self.display_img = np.zeros((90, 256, 3), dtype=np.uint8)

    def step(self):
        flip = self.get_blended_input('flip', 'sum') or 0.0
        self.t += 1

        # periodic auto-reversal (the local current changes chirality)
        if self.reverse_every > 0 and (self.t % self.reverse_every) == 0:
            self.sign = -self.sign
        # manual flip on a rising edge
        is_flip = float(flip) > 0.5
        if is_flip and not self.was_flip:
            self.sign = -self.sign
        self.was_flip = is_flip

        self.tilt = self.strength * self.sign
        self._render()

    def get_output(self, port_name):
        if port_name == 'tilt':  return float(self.tilt)
        if port_name == 'chi':   return float(self.sign)
        if port_name == 'meter': return self.display_img
        return None

    def _render(self):
        h, w = 90, 256
        img = np.zeros((h, w, 3), dtype=np.uint8)
        cx, cy = 128, 46
        col = (90, 200, 130) if self.sign > 0 else (120, 130, 255)

        # direction arrow
        half = int(np.clip(self.strength, 0, 1) * 90)
        if self.sign > 0:
            cv2.arrowedLine(img, (cx - half, cy), (cx + half, cy), col, 3, tipLength=0.3)
        else:
            cv2.arrowedLine(img, (cx + half, cy), (cx - half, cy), col, 3, tipLength=0.3)

        cv2.putText(img, "ephaptic tilt (which way)", (4, 16),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.32, (150, 200, 175), 1)
        dirtxt = "forward >>>" if self.sign > 0 else "<<< reverse"
        cv2.putText(img, f"{dirtxt}   |A|*chi {self.tilt:+.2f}", (4, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.32, col, 1)
        self.display_img = img

    def get_display_image(self):
        return QtGui.QImage(self.display_img.data, 256, 90, 256 * 3,
                            QtGui.QImage.Format.Format_RGB888)

    def get_config_options(self):
        return [
            ("Strength (|A|)", "strength", self.strength, "float"),
            ("Reverse every (frames, 0=never)", "reverse_every", self.reverse_every, None),
            ("Hold sign (1 fwd / -1 rev)", "hold_sign", self.sign, None),
        ]

    def set_config_options(self, options):
        if "strength" in options: self.strength = float(options["strength"])
        if "reverse_every" in options: self.reverse_every = int(options["reverse_every"])
        if "hold_sign" in options:
            self.sign = 1 if int(options["hold_sign"]) >= 0 else -1
