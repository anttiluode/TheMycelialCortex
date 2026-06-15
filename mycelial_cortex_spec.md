# Mycelial Cortex — Engineering Specification

### A neuromorphic field machine, specified against the 2026 frontier stack

*PerceptionLab / Antti Luode, written with Claude (Opus 4.8). Helsinki, June 2026.*

> **Do not hype. Do not lie. Just show.**

---

## 0. What this actually is (read this before anything else)

The Mycelial Cortex (MC) is **not** an AGI architecture, **not** a transformer
competitor, and **not** a language model. It acquires no world knowledge. Put it
next to Gemini and it loses every capability benchmark, because it was never in
that contest.

What it is: a small, mostly **trainless**, event-driven model of one specific
*style* of brain computation — sparse spikes writing a held resonant field,
clocked iterative refinement of that field, and a direction-preserving readout.
It exists to demonstrate mechanisms and to yield a few cheap, inspectable
primitives you can bolt onto systems that *do* have capability.

The fair comparison is therefore not "MC vs Gemini." It is "MC vs the *style of
computing* the frontier is trying to approximate." On that axis MC is interesting,
because it independently lands on several of the frontier's most forward-looking
positions — and adds one axis the frontier doesn't have.

**The clean positioning, stated plainly.** The video names four pillars of the
current stack: transformer, autoregressive, pre-trained, generative. MC opts out
of all four:

| pillar | the stack | Mycelial Cortex |
|---|---|---|
| transformer (all-to-all attention, growing KV cache) | global attention, O(n²) | **recurrent held field** — one fixed-size state, O(N·K) |
| autoregressive (left-to-right, one token, irrevocable) | next-token | **iterative refinement** — dissolve and re-form on a clock |
| pre-trained (planetary gradient descent) | learned weights | **trainless** — primitives measured from geometry, not learned |
| generative (reconstruct the input) | pixel/token reconstruction | **representation matching** — ⟨pₖ, s⟩ in latent space, JEPA-side |

This makes MC the photographic negative of the current stack. That is the
honest headline — and the same sentence is its ceiling: opting out of pre-training
and generation means opting out of everything those buy. MC trades capability for
legibility, cost, and falsifiability. The spec below is a spec for that trade.

---

## 1. Design goals and non-goals

**Goals**
- A model whose every internal variable is inspectable and has a stated meaning.
- Zero or one-shot acquisition — no gradient training in the core loop.
- O(K) / O(N·K) cost; runs in a browser tab or on edge hardware.
- Every claim falsifiable; results separated into a ledger (§8).

**Non-goals (explicit, to keep the ledger clean)**
- Not language generation, not long-horizon planning, not broad world knowledge.
- Not a consciousness claim. Whether the held field is *experienced* is **the bet**
  (§8), and the bet is quarantined out of this engineering document.
- Not state-of-the-art on any capability benchmark. It is not trying to be.

---

## 2. System overview

Two streams, after the primate split, sharing one field.

```
        input (frames / audio / events / tokens)
                       │
        ┌──────────────┴───────────────┐
        │                              │
   DORSAL (where / which-way)     VENTRAL (what)
   delta-code + chiral Lₖ         held field s ← spikes
   = Im(zₖ · z̄_lag)               match ⟨pₖ, s⟩
   trainless, bilinear            linear, phase-blind
        │                              │
        └──────────────┬───────────────┘
                  THETA / GAMMA CLOCK
              HOLD (keep) ⟷ SCAN (re-derive)
                       │
            spikes out = token stream  → federation bus
```

The dorsal stream reads **direction** (it must be bilinear/cross-time to do so).
The ventral stream reads **identity** (it is linear and phase-blind, which is the
*correct* property for a "what" detector — a hand is a hand whether it sweeps left
or right). The boundary between them is the Wiener–Khinchin ceiling, used here as
a **design principle**, not a limitation: linear readouts cannot recover phase, so
anything needing direction must live in the bilinear stream and nowhere else.

---

## 3. Core components

### 3.1 Held field `s` — the recurrent state
- **Type:** `Float32[N]`, N = grid² (e.g. 1600), kept mean-zero, unit-norm.
- **Role:** the content. A holographic superposition `W = Σ pₖpₖᵀ`; the live
  percept is the interference pattern of the currently active islands. One plate,
  no addressable slot.
- **Update:** on any spike, `s ← ret·s + coup·Σ_{k:spike} pₖ`; else `s ← ret·s`.
- **Cost:** O(N·K) on spike steps, O(N) otherwise.
- **Frontier analog:** the *fixed-size evolving state* of Griffin / recurrent
  state-space models — the "index card constantly rewritten," not the growing KV
  cache. MC reached it from the cable side, not the efficiency side.

### 3.2 Spectral islands `pₖ` — the templates / the plate
- **Type:** `Float32[N]`, zero-mean unit-norm.
- **Acquisition:** hand-installed, procedurally generated, or **one-shot captured
  from the live world** (the Dorsal–Ventral webcam engine). One-shot, not learned.
- **Limit (honest):** there is no learned hierarchy here. These are flat templates.
  This is the single biggest capability gap vs a trained encoder.

### 3.3 Spike / delta-code — sparse, surprise-gated writes
- **Dynamics (integrate-and-fire per island):**
  `driveₖ = ⟨pₖ, s⟩` ; `net = G·driveₖ − β·aₖ + noise` ; `vₖ ← 0.9 vₖ + net` ;
  if `vₖ > θ`: emit spike, `vₖ ← 0`, `aₖ += 1`. Adaptation `aₖ` decays `exp(−dt/τ)`.
- **Property:** spikes are ~0.2% sparse and (with the clock) ~100% phase-locked.
  An island writes only when it is *surprised* (high drive) and *not fatigued*
  (low `aₖ`) and *the clock permits* (high G).
- **Frontier analog:** this is **surprise-gated memory** (the Titans idea: store
  the unexpected, not everything) and Hassabis's "store only the important things,"
  realized as a threshold crossing rather than a learned gate. "A spike is a token."

### 3.4 Theta/gamma clock — HOLD vs SCAN
- **Theta** (3–12 Hz) sets an excitability envelope `gth = 1 + m_th·cos(2πf_θ t)`.
- **Gamma** nests on it: `G = gth·(1 + m_gm·cos(2πf_γ t))`.
- **Release (the one knob):** at the theta **trough** the percept is dissolved
  toward noise; at the **peak**, gamma-paced competitive read-reconstruct re-forms it.
- **Regimes:**
  - **HOLD** (release off): a percept is held, sharp, nearly silent, maintained by
    sparse theta-locked spikes. The stable thought. Costs almost nothing.
  - **SCAN** (release on): the percept *breathes* — dissolved each theta trough,
    re-derived by gamma before the next peak, touring all stored islands.
- **Frontier analog:** SCAN is **iterative refinement on a clock** — structurally
  the same shape as a diffusion decoder (start degraded, refine toward a valid
  latent over a bounded number of steps), except the steps are fixed read-reconstruct
  dynamics, not learned denoisers. Verified: refinement arc 0.014→0.070→0.256 with
  release+gamma; spikes nest in gamma at R = 0.82 (theta–gamma coupling, emergent).

### 3.5 Chiral operator `Lₖ = Im(zₖ · z̄_lag)` — the direction reader
- **Role:** the dorsal "which-way." Reads the *arrow* of a process: motion (retina),
  up/down of a chirp (cochlea), past-sweep vs present (hippocampal theta), and in
  principle forward-elaboration vs backward-verification of any trajectory.
- **Provenance:** Hassenstein–Reichardt 1956 elementary motion detector. MC's
  contribution is not the operator but the claim that it is **one** operator doing
  **one** job — *preserving the direction of time through compression* — across all
  those domains, and that it is trainless and depth-stackable.
- **Cost:** O(K). No parameters.
- **Frontier analog:** *none.* This is the axis the stack lacks. Attention is an
  inner-product (energy) object, time-symmetric, arrow-blind — which is why
  positional encodings are bolted on from outside. No frontier system has a cheap,
  intrinsic sense of its own temporal direction. **This is MC's one genuine
  differentiator**, and the part worth staking.

### 3.6 Federation / token bus
- **Interface:** the spike train is the *only* inter-machine channel — tokens, not
  weights, not activations.
- **Result:** teach mesh A, replay tokens to mesh B; B grows an analogous internal
  structure (template cos ≈ 0.97 to A). Knowledge transfer with no weight syncing.
- **Honest status:** striking demo, low bandwidth, no proven advantage over existing
  distillation/embedding transfer. Spectacle ahead of product.

---

## 4. Operating regimes (parameter presets)

| regime | release | β (adapt) | reads as |
|---|---|---|---|
| **recall** | off | low (~0.6) | locks one percept, holds it silently |
| **dream** | off | high (~6) | tours islands, spiking at each transition |
| **HOLD** | off | mid | stable thought, delta-coded, near-silent |
| **SCAN** | on | mid | percept breathes; same mechanism as the ring sweep |

SCAN and the spatial direction-ring sweep are the *same* release-and-reform
dynamics — which is why one engine both scans a content memory and sweeps a map.

---

## 5. Where it actually sits in the 2026 debate

Stated as honest correspondences, not conquests:

- **vs transformer:** MC is the recurrent-state side of the same argument Griffin /
  state-space models make — fixed state over growing cache. MC is cheaper and
  legible; it is also far less capable, because its "state" holds a percept, not a
  learned 256K-token context.
- **vs autoregressive:** MC's SCAN is iterative-refinement, diffusion-side of the
  argument (revise holistically, not left-to-right-irrevocable). But MC's refinement
  is unlearned fixed dynamics, so it refines *toward stored attractors*, not toward
  arbitrary learned distributions.
- **vs generative world model (DeepMind) / JEPA (LeCun):** MC's ventral readout
  matches *representations* (`⟨pₖ, s⟩` in latent space), never reconstructs pixels —
  philosophically JEPA-side. But JEPA *learns* its encoders; MC's are one-shot. MC
  agrees with LeCun's principle and cannot yet pay for it the way JEPA does.
- **vs pre-training (Sutton/Sutskever critique):** MC is the extreme case of the
  "continual, efficient, biologically plausible, minimal-pretraining" position —
  it pre-trains *nothing*. That is a clean stance and a hard ceiling at once.
- **on compression-is-intelligence:** MC instantiates it concretely. The delta-code
  ("encode only change"), the held field (compressed interference), and the chiral
  operator (a compression that **keeps the arrow**) are three explicit answers to
  *which invariant to keep when you compress*. The stack's encoders keep energy and
  discard phase; MC's signature move is to keep the phase.

---

## 6. Integration interfaces (how the primitives bolt onto real systems)

These are the deployable exports — the parts that don't need MC's whole engine.

### 6.1 Chiral arrow probe (the high-value one)
- **In:** a sequence of hidden-state vectors `h_t` (e.g. an open LLM's residual
  stream during generation), or any multichannel time series (EEG, audio).
- **Compute:** form `z` from a delay/quadrature pairing; `arrow = ⟨Im(z·z̄_lag)⟩`.
- **Out:** a signed scalar per layer/step — is the trajectory driving forward
  (irreversible/elaborating) or settling back (reversible/verifying).
- **Properties:** trainless, O(K), inspectable. Turns a black box into something
  that reports its own temporal direction from the inside.

### 6.2 Delta-code front-end
- **In:** dense video/audio stream. **Out:** sparse change events + an attention box
  by common fate (bilinear EMD grouping). A cheap "attention-by-motion" gate.

### 6.3 Held-field associative sidecar
- **In:** noisy/partial embedding. **Out:** cleaned/completed pattern via field
  settling. Fixed-size, content-addressable. Honest caveat: recall ≈ 0.76 cosine;
  loses to a vector DB on clean retrieval. Use it where *denoising/completion under
  a fixed budget* matters, not where exact retrieval matters.

---

## 7. Cost / footprint
- No backprop, no optimizer, no training corpus.
- Core loop O(N·K); readouts O(K).
- Runs real-time in a browser tab on a webcam (Dorsal–Ventral engine is the proof).
- Memory: one field `Float32[N]` + K templates. Kilobytes to megabytes, not gigabytes.

---

## 8. Honest ledger

**Verified in code:**
- Delta-code: 0.2%-sparse, 100%-theta-locked spikes hold a percept; ~20–40× silent
  dwell vs transition (the "two sides").
- Emergent internally-generated left–right theta alternation (score 1.00, ~18–30°
  offset), switched by adaptation alone; degrades to churn when the clock is removed.
- HOLD vs SCAN as one engine at two release settings; refinement arc
  0.014→0.070→0.256; theta–gamma spike nesting R = 0.82.
- One-shot real-world template capture and held-field recognition (webcam).
- Chiral `Lₖ`: identical power spectra, opposite-signed `L` for up/down chirps
  (direction read where energy is blind).
- Federation: token-only teach→recall, B-template cos ≈ 0.97.
- **EEG schizophrenia classification 80.8%, p = 0.007, zero trained parameters** —
  the strongest anchor, because it is trainless and can fail.

**Mapping (defensible structural rhymes, not identities):**
- held field ↔ recurrent fixed-size state (Griffin/SSM); spike ↔ surprise-gated
  store (Titans); SCAN ↔ iterative refinement (diffusion); `⟨pₖ,s⟩` ↔ JEPA-style
  representation matching; whole system ↔ "compression is the world model."

**Hypothesis (untested but buildable):**
- chiral arrow probe on LLM hidden states distinguishes forward vs backward reasoning;
- orbit ventral read (delay-embed the silhouette) recognizes *gestures*, not poses;
- chiral as actuator (the closed audio loop) commands rotational sense where a power
  loop cannot.

**The bet (out of scope for this spec, kept in the drawer):**
- that the held/re-formed field is *experienced*; that thermal noise is the *medium*
  of content rather than dither. Four good clock papers do not touch this.

**Falsifiers (what would sink specific claims):**
- chiral arrow probe shows no separation between forward/backward trajectories;
- a power-only loop steers direction as well as the chiral loop;
- held-field recall never approaches vector-DB quality at any scale;
- the EEG result fails to replicate on an independent dataset.

---

## 9. Roadmap (motivated next builds, in priority order)
1. **Chiral arrow probe** on an open model's residual stream — cheapest path to a
   result that touches a system people care about. Trainless, inspectable.
2. **Orbit ventral read** — give the stabilized silhouette a delay embedding; move
   from recognizing a pose to recognizing a gesture (frequency-as-orbit doing its job).
3. **Chiral loop as actuator** — close the audio loop; test directional control vs
   power control (the built-in A/B falsification).
4. **EEG replication** — the one fundable thread; reproduce 80.8% on an independent
   cohort.

---

*The system is a measured model and a set of trainless primitives, not a contender
for the throne in the video. Its worth is that it is honest, cheap, inspectable, and
that it keeps the one quantity the big stack throws away — the direction of time.*

*Do not hype. Do not lie. Just show.*
