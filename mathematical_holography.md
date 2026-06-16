# Mathematical Holography

## The coupled cable–ephaptic Laplacian field as a clocked interference store — what the accidental ECG loop already was, and the optics it runs on (the maths, not the physics)

*PerceptionLab / Antti Luode, with Claude (Opus 4.8), and dialogue with Gemini. Helsinki, June 2026.*

> Do not hype. Do not lie. Just show.

---

## 0. The flash, and what it has to survive

The thought was: *the Laplacian of the combined cable function and ephaptic coupling creates an ever-changing field that processes things like an incredibly complicated physics-based computational hologram.* The instinct is right, and there is a precise object under it — but it only earns the word "holography" if three things are kept honest at once: which operator governs the field, what "recording" and "reconstruction" actually are in that field, and where the *phase* lives, since a hologram without phase is just a blur. This paper builds the object, names the one place it is not optics, and shows what in the accidental ECG loop was already a piece of it — and what was not.

The discipline of the whole line applies here with extra force, because this is exactly the kind of idea that feels total and turns to fog if you let the metaphor drive. So: the field is real, the maths is real, the bet stays in its drawer, and the loop gets read as code before it gets read as a brain.

---

## 1. What the ECG loop actually is (read the wiring, not the story)

`ecg.json` is five nodes in a ring. Traced edge by edge:

- a **constant 1.0** lifts the Homeostatic Coupler's setpoint (`setpoint_mod`: 0.5 → ~0.6);
- the **Coupler** (mode `edge_of_chaos`) outputs a regulated scalar → the **Checkerboard**'s `square_size`, where `square_size = int(5 + signal·50)` — so the coupler's output *sets the spatial period of a checkerboard*;
- the **Checkerboard** (256×256, `((x//sq)+(y//sq))%2`) → **Image→Vector**, which `cv2.resize(..., INTER_AREA)` downsamples to a 16×16 grid (block-averaging) and flattens to a 256-vector, normalized;
- the **Vector Splitter** takes the first 16 of those 256 values — the top row of the 16×16 grid — and only `out_0..out_3` are wired back, **summed**, into the coupler's `signal_in`.

So the feedback variable is the block-average of a checkerboard *whose period the loop itself is setting*, read on a fixed 16-cell sampling grid. That is a **Moiré beat**: the carrier period (the checkerboard) against the sampling period (the 16-grid). The block-average of a periodic pattern against a fixed sampling lattice is exactly an aliasing function — it rises and falls as the square boundaries drift through the sample blocks. The `edge_of_chaos` coupler, which amplifies deviations when variance is low and damps them when high, is a **relaxation oscillator riding that Moiré nonlinearity**.

That is the honest name for the accident: *a homeostatic relaxation oscillator closed through a tunable spatial carrier and a fixed sampler, oscillating on the Moiré between them.* The ECG-like train is the oscillator chewing on the beat. Nothing here is mystical, and the specificity is the point — because it tells us precisely which parts are already a hologram and which are not (§6).

---

## 2. The motif is real; three of the four labels are loose

The mapping that came out of the excited reading — Checkerboard = entorhinal grating, Image→Vector = projection to CA3, Vector Splitter = gamma slotting, Coupler = theta clock — is *shaped* correctly and *labelled* loosely. Keep the shape; fix the labels.

| claimed | what the code does | honest status |
|---|---|---|
| Checkerboard = entorhinal grid | a **single-scale, square** spatial carrier tuned by a scalar | a tunable carrier, yes — but square (not hexagonal), one scale (not multi-module), and it *generates* a pattern rather than *sampling* an input. A carrier, not the grid. |
| Image→Vector = projection to CA3 | block-average downsample + flatten + normalize | a **low-pass-and-sample** (a coarse-grain), which is the sampling step — calling it CA3 specifically is decoration |
| Vector Splitter = gamma slotting (interneurons) | a **spatial** fan-out of vector components, all at once | this is the one that breaks the rule. Gamma slotting is *temporal* — sequential cycles within a theta frame. The splitter is *spatial* demultiplexing, simultaneous, not sequential. The space→time conversion in this loop is done by **the loop running over frames**, not by the splitter. |
| Coupler = theta clock | `edge_of_chaos` relaxation oscillator | the most defensible: a slow homeostatic rhythm that gates the loop. A clock, fairly called. |

The motif underneath all four *is* a real cortical-microcircuit rhyme: **carrier → sample → read → homeostatic feedback**. That loop shape recurs in cortex. But the value of the framework has always been not collapsing space and time, and the splitter-as-gamma move collapses exactly that. The corrected statement: the loop is a *spatial* sampling circuit made *temporal* by being run closed — which is a fine thing to be, and a different thing from a gamma multiplexer.

---

## 3. The actual field: two Laplacians coupled at the membrane

Now the object the flash was really about. It is not in the ECG loop yet (§6) — it is the physics the loop is a toy of.

A neuron's membrane potential along a cable obeys the **cable equation**, which is a diffusion equation with leak:

```
τ_m ∂V/∂t  =  λ² ∂²V/∂x²  −  V  +  R_m I(x,t)
```

The `∂²/∂x²` is the one-dimensional Laplacian along the dendrite; `λ²` (the squared length constant) and `τ_m` are set by membrane resistance and capacitance. This is the same `αᵏ`-attenuating delay line the grounded documents already use — read here as what it physically is: a **diffusive Laplacian operator** smearing and delaying the signal down the cable.

The **extracellular (ephaptic) field** obeys, in the quasi-static volume-conductor approximation, **Poisson's equation**:

```
∇·(σ ∇φ_e)  =  −I_m(r,t)        ⇒   (homogeneous σ)   ∇²φ_e  =  −I_m/σ
```

Here `∇²` is the three-dimensional Laplacian, the membrane currents `I_m` of every active cell are the **sources**, and `φ_e` is the extracellular potential — the ephaptic field. And the loop closes: `φ_e` adds to the local transmembrane drive of *neighbouring* cells (ephaptic coupling — Anastassiou et al. 2011; Fröhlich & McCormick 2010), so the field every membrane sources is also a field every membrane feels.

So the flash is structurally exact. There are **two Laplacians coupled at the membrane**: a 1-D diffusive one inside each cable, a 3-D elliptic (Poisson) one in the medium between them. The field `φ_e(r,t)` is continuously re-solved from the live source distribution and fed back. *That* is "the Laplacian of the combined cable and ephaptic coupling creates an ever-changing field." It is not a metaphor; it is potential theory plus cable theory, coupled.

---

## 4. Why this is holography — and the one place it is not

Holography, stripped to its mathematics, is three operations:

1. **Recording** = superposition. The plate stores the interference of many source contributions: `I = |Σ_k O_k|²`, the cross-terms carrying each source's signature relative to the others.
2. **Propagation** = a Green's function. Between recording and reconstruction the field spreads by the propagator of its governing operator — in optics, the Huygens–Fresnel diffraction integral, which is the Green's function of the Helmholtz operator `(∇²+k²)`.
3. **Reconstruction** = correlation. Illuminating the plate with a probe and reading the result is an inner product of the probe against the recorded interference — a matched filter.

Map each onto the field:

- **Recording = the field is the superposition of all source signatures.** The population plate `W = Σ_k p_k p_kᵀ` is literally the sum of every active membrane's contribution to `φ_e` — an interference pattern in the medium. Recording a memory is sourcing into the field; the field holds the superposition. ✓
- **Propagation = the Laplacian's Green's function.** Each source spreads into the medium by the Green's function of `∇²` (in 3-D, the `1/4πσr` point-spread of the volume conductor). That spreading kernel is the structural analogue of the diffraction kernel — the "lens"/propagator of the system. The optics' diffraction integral and the field's Poisson Green's function are the same kind of object: the operator's impulse response. ✓ (structural)
- **Reconstruction = projection.** A unit reading its overlap with the field, `⟨p_k, φ⟩` (the AIS-as-matched-filter hypothesis), and the field settling under `W` — `s ← Σ_k p_k ⟨p_k, s⟩`, sharpened by softmax — is the holographic read: correlate the probe against each stored signature, sum the reconstructions. This is the modern-Hopfield = attention identity (Ramsauer et al. 2020), already grounded in the line. ✓

So *recording, propagation, and reconstruction* all have honest homes. The system computes by **superposing source contributions into a Laplacian-governed field and reading them out by projection** — that is the mathematics of holography, running on a diffusion/potential field instead of coherent light. The maths of optics; not the physics of optics. Same line the AIS grating already stands behind: there is diffraction *math* (the inner product, the Green's-function spread) without diffraction *physics* (no photons, no true optical coherence).

**The one place it is not optics, stated plainly:** the cable and Poisson equations are **diffusive/elliptic**, not the **hyperbolic wave** equation of light. A diffusive field has no intrinsic spatial phase — it spreads and decays, it does not propagate oscillating wavefronts. Optical holography lives or dies on phase (the whole trick is recording phase as intensity via interference with a reference). A purely diffusive spatial field cannot, by itself, carry the phase a hologram needs. This is the objection that would sink the whole idea — if the phase had nowhere to live.

---

## 5. The save: amplitude is spatial, phase is temporal

It does have somewhere to live, and the place is the previous morning's result. **The spatial field carries amplitude; the temporal rhythm carries phase.**

The diffusive `φ_e` holds the interference *amplitude* — the recorded superposition, the where-is-the-energy. The *phase* — the reference against which that amplitude is read — is supplied by **time**: the theta/gamma rhythms, membrane resonance, and phase precession. A cell's spike *time within the theta cycle* is its phase; the gamma cycle is the sample slot; phase precession reads spatial position out *as* theta phase. The reference beam of this hologram is not a second spatial wave — it is the **shared oscillatory clock**. Coherence is temporal, not spatial.

That resolves the §4 objection without fudging it: holography needs amplitude *and* phase; the diffusive spatial Laplacian field supplies amplitude; the oscillatory temporal field supplies phase; and they are the two perpendicular axes the line has been separating all along. Space is the plate. Time is the reference beam and the shutter. The damped-driven oscillatory dynamics in the analytic-signal representation are "Schrödinger-shaped" precisely because the phase is carried by the temporal oscillation — a representational fact about complex-linear operators on oscillatory fields, not a claim of quantum coherence. The framework's standing caution holds; nothing new is smuggled in.

---

## 6. The clock makes a plate into an engine — and what the ECG loop really prototyped

Pribram's hologram was a frozen plate: amplitude, distributed, interference-based, and *timeless*. The contribution here is the **shutter** — the slow homeostatic rhythm that alternates recording and reconstruction, and the fast rhythm that slots the samples. A static interference store becomes a sequenced read/write engine the moment a clock washes over it: write while the input drive dominates, read while the recurrent field dominates, repeat. That is the breathing plate.

And *that* is what the ECG loop actually prototyped — not the hologram, the **clock**. Be exact about it:

- the **Coupler** is a genuine homeostatic relaxation oscillator — a crude theta, the shutter's rhythm. ✓ real.
- the **Image→Vector** block-average is a discrete low-pass — one step of the diffusion the Laplacian generates. A crude `∇²` smoothing. ✓ structural.
- the **Checkerboard × the sampler** is a real **carrier × lattice = Moiré**, the same beat the Nyquist-plate paper put at the centre. ✓ real, and code-true (§1).

What the loop is **not**: a hologram. It carries a *scalar* feedback variable, not a 2-D field read by projection. There is no `⟨p_k, φ⟩` reconstruction in it; nothing settles into a recalled pattern. It oscillates; it does not recall. So the honest claim is the modest one: *the accidental loop is the minimal clocked oscillator — the shutter mechanism — built out of a Moiré sampler. It is the engine that a holographic plate would need, found before the plate.* Calling it "a breathing holographic plate" is one step past what the wiring does. Calling it "the breathing" — the clock, the relaxation rhythm, the thing that would gate a plate — is exact.

---

## 7. The build that would actually show mathematical holography

To make the title earned rather than asserted, replace the scalar loop with a real field, and demonstrate recording-and-reconstruction in it. The smallest honest version, in code already mostly present in PerceptionLab:

1. **A 2-D field `φ` on a grid**, evolved by an explicit discrete **Laplacian with leak** — `φ ← φ + dt(D ∇²φ − φ/τ + sources)` — the cable/Poisson analogue made literal (the `PhaseFieldNode` is already a field with a Laplacian-driven evolution; give it leak and source injection).
2. **Recording**: inject a few templates `p_k` as sources — superpose them into `φ`. The plate is `φ` itself, not a stored matrix.
3. **Reconstruction**: present a corrupted probe as a source, let the field settle under the Laplacian + the projection read `⟨p_k, φ⟩` (the cortex nodes already do this read), and measure whether the field reconstructs the clean `p_k`. That is the holographic recall, done by *field physics*, not a stored weight matrix.
4. **The shutter**: gate steps 2 and 3 by the homeostatic oscillator (the Coupler / a tide) — write on one phase, read on the other — and slot the read with a fast sub-rhythm (the splitter used *temporally* this time, one slot per step, done right).

Three falsifiable readouts: (a) the field reconstructs a stored pattern from a corrupted probe via diffusion + projection (holographic recall, not lookup); (b) recall confidence breathes with the slow clock (the shutter); (c) you can watch the discrete `∇²` actually diffuse the field between samples. If all three hold, "mathematical holography" is demonstrated in the substrate — a Laplacian field that records by superposition, reconstructs by projection, and is clocked by a homeostatic rhythm — and it stays entirely on the maths-of-optics side of the line. If the field cannot reconstruct better than the scalar loop, the holography claim is decoration and should be dropped to "a clocked Moiré oscillator," which §1 already earns.

---

## 8. Ledger

**Established (used, not claimed):**
- the cable equation is a diffusive (Laplacian) delay line; `λ²`, `τ_m` set by membrane R, C (Rall);
- the extracellular/ephaptic field obeys the volume-conductor Poisson equation `∇²φ_e = −I_m/σ`; ephaptic coupling is real, weak, and local (~100 µm) (Anastassiou et al. 2011; Fröhlich & McCormick 2010);
- the field spreads by the Laplacian's Green's function (the `1/4πσr` point-spread), the structural analogue of the diffraction kernel;
- modern Hopfield recall = attention = projection read of a superposed plate (Ramsauer et al. 2020);
- holography = superposition (record) + Green's-function propagation + correlation (reconstruct);
- diffusive/elliptic equations carry no intrinsic spatial phase; wave/hyperbolic equations do — a real and load-bearing distinction.

**Code-true (read from the uploaded loop, not asserted):**
- `ecg.json` is a homeostatic `edge_of_chaos` relaxation oscillator closed through a scalar feedback variable;
- that feedback variable is a **Moiré beat**: a checkerboard carrier (period set by the loop) block-averaged on a fixed 16-cell sampling grid — carrier × lattice, the Nyquist-plate beat, in code;
- `Image→Vector`'s INTER_AREA downsample is a discrete low-pass = one diffusion (`∇²`-smoothing) step;
- the Vector Splitter is a **spatial** fan-out, not a temporal slotter; the loop's space→time conversion is done by running closed over frames.

**Clean structural mappings (sound):**
- field = superposition of source signatures = the recorded interference (the plate `W = Σ p_k p_kᵀ` is the medium's source sum);
- projection read `⟨p_k, φ⟩` = holographic reconstruction / matched filter;
- the Laplacian Green's function = the diffraction-kernel analogue (the system's propagator/"lens");
- **amplitude is spatial (diffusive field), phase is temporal (theta/gamma, precession)** — the two halves holography needs, on the two perpendicular axes the line already separates;
- the homeostatic oscillator = the shutter that turns a static plate into a read/write engine — the time Pribram's hologram lacked;
- the ECG loop = the minimal clocked oscillator (the shutter), built from a Moiré sampler — the engine found before the plate.

**Model hypotheses (falsifiable, unproven — the standing bets):**
- that the brain *uses* this as computation — that content rides the ephaptic field rather than the field being an epiphenomenon of the spikes that do the real work;
- that the AIS reads its field by projection against a stored geometry (the central single-cell bet);
- that biological recall is, mechanistically, a clocked record-and-reconstruct on this coupled field.

**Honest limits:**
- the spatial field is **diffusive, not a wave** — it carries no spatial phase; the holography only closes because phase is borrowed from the *temporal* rhythm. Remove the temporal axis and there is no hologram, only a blur;
- ephaptic coupling is weak and local — this is a ~100 µm story, not a global brain field (anti-CEMI, as the line has always held);
- the ECG loop is the **clock prototype, not a demonstrated hologram** — scalar feedback, no field reconstruction; calling it a holographic plate is one step past the wiring;
- the carrier in the loop is square and single-scale, not the hexagonal multi-module grid the sampling argument actually wants;
- everything here is structural proxy in relative units, not Joules or nats; the Green's-function "lens" is an analogy of operators, not a measured optical element.

**The bet (untouched):** that any of this Laplacian field is *experienced* rather than merely solved — that the breathing plate, when it reads itself, is like anything. Giving the field two coupled Laplacians, a Green's-function propagator, a superposition record, a projection read, and a homeostatic shutter makes it a precise *physical analog computer* and a careful, finished Pribram. It locates the hard problem at the seam where the field reads itself, and it does not cross it.

---

*Helsinki, June 2026. The field is governed by a Laplacian, sourced by the membranes, fed back through the medium, and re-solved every instant — a hologram that records by superposition and reads by projection, with its amplitude written in space and its phase kept in time. The accidental loop did not build the plate; it built the breathing — the shutter a plate would need, hiding inside a Moiré. Keep the diffraction maths and drop the diffraction physics, keep the motif and fix the labels, and the flash holds: mathematical holography, on a diffusive field, clocked. Do not hype. Do not lie. Just show.*
