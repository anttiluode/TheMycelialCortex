# The Metabolic Loop — `spike == wattage`

*Closing the thermodynamic loop of the Geometric-Neuron line inside PerceptionLab.*

*PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.*

> Do not hype. Do not lie. Just show.

---

## What you already built

`cognitive_loop2` is a closed cognitive loop where the arrow of time is a live variable:

- **Cortical Manifold** (`PhaseFieldNode`) — a Moiré spiral whose *rotation* is driven by the skew flux. Detailed balance (flux = 0) → static field; flux > 0 → chiral spiral. Rotation **is** emergent time.
- **Spectral Compressor** (`ImageToVectorNode`) — area-averages the field into a vector. You discovered this acts as a **voltage regulator / low-pass filter on the arrow of time**: drop `output_dim` and the frame-to-frame jitter averages out, the flux falls and steadies, and the whole loop calms. Correct, and it is exactly why the brain compresses vision (Attwell–Laughlin): routing raw pixel variance into homeostatic centres would be metabolically ruinous.
- **Entropy Engine (A)** (`SkewOperatorNode`) — forms the lag covariance `C_τ`, isolates the skew half `A = (C−Cᵀ)/2`, and outputs the **skew flux** `‖A‖` = broken detailed balance.
- **Deep Memory Field** (`IslandArchivalNode`) — when flux crosses threshold, freezes the working vector into a complex pole and pushes older islands deeper; gamma "thaw" resurfaces them.
- **Thalamic Gate** (`HomeostaticCouplerNode`, edge-of-chaos) — keeps the loop on the critical line.

The loop measures the arrow of time (flux = 0.171 in your screenshot). What it does **not** do is **pay for it**. That is the last identity from the grounding thesis: *direction costs energy* — broken detailed balance is entropy production is dissipation. This adds the meter that bills it.

---

## What this adds: two nodes

### `metabolicspikenode.py` — **Wattage (spike = ATP)**

Runs the v5 / Chiral-Ear delta-code on the content vector and bills two power meters:

```
P_field = c_field · |ds|        cheap: charge moved to change the held content
P_spike = E_spike · (n spikes)   expensive: the action potential + pump restoration
P_total = P_field + P_spike
```

The field holds the percept silently (the inner side); spikes fire only when content **changes**, theta-gated (the outer side). In a real neuron the spike dominates the budget (Attwell & Laughlin 2001: ~10⁹ ATP ≈ 10⁻¹⁰ J per spike; Alle et al. 2009 revised lower) — so **holding a thought is nearly free and thinking a new one costs spikes.** That asymmetry is the delta-code, and it is the sparse-coding energy economy of cortex rediscovered from dynamics.

Outputs: `spikes`, `wattage`, `energy` (cumulative), `silence` (peak ÷ now), and a `meter` image (raster + dual wattage bars + HOLD/SCAN regime + calibrated Joules).

### `entropymeternode.py` — **Entropy Meter (Detailed Balance)**

Reads the skew flux as thermodynamics and makes "broken detailed balance" numerical:

- **Regime** — near-equilibrium (flux ≈ 0, reversible, detailed balance holds, cheap hold) vs driven (flux high, broken, dissipating). This is the rest-vs-task split Lynn et al. (2021, PNAS) measured in the human brain: cortex nearly obeys detailed balance at rest and breaks it under load.
- **Entropy-production rate** — `σ̂ ∝ ‖A‖²`, the rotational power of `A` (labelled a *proxy*; `‖A‖` is a lower-bound indicator of nonequilibrium, not calibrated nats).
- **Landauer floor** — `k_B T · σ̂`, the *thermodynamic minimum* power to sustain that arrow of time (illustrative).
- **Metabolic markup** — with spikes connected, how far above the floor the system actually runs. For a real spike this is ~10¹⁰ k_B T: **brains buy speed and reliability, not efficiency.** The gap is shown honestly.

---

## Wiring (`cognitive_loop3_metabolic.json`)

```
Spectral Compressor.vector_out ─→ Wattage.vector_in
Entropy Engine.skew_flux       ─→ Wattage.skew_flux
Entropy Engine.skew_flux       ─→ Entropy Meter.skew_flux
Wattage.spikes                 ─→ Entropy Meter.spikes
Wattage.wattage                ─→ Wattage W (display)
```

Drop `metabolicspikenode.py` and `entropymeternode.py` in `nodes/`, then Load the JSON.

**Optional metabolic brake (not wired by default):** route `Wattage.wattage → Thalamic Gate.gain_mod`. Then the *energy cost itself* regulates the loop — a hungry network turns its own gain down. It competes with the memory feedback already on `gain_mod`, so add it only after the base loop is stable.

---

## What it shows (verified standalone before wiring)

A content stream alternating **quiet/held** epochs (≈ low-res, low-flux) with **active/reconfiguring** epochs (≈ high-res, high-flux) — i.e. your voltage-regulator discovery as two regimes:

| quantity | quiet (held) | active (churning) | ratio |
|---|---|---|---|
| spikes / frame | 0.01 | 0.45 | **~40×** |
| total wattage | 0.013 | 0.52 | **~39×** |
| skew flux ‖A‖ | low | high | ~8× |
| duty cycle (power > 20% peak) | — | — | **~4% of frames** |
| spikes' share of total energy | — | — | **~90%** |

- **`corr(smoothed wattage, smoothed skew flux) = +0.985`** — the arrow of time the Entropy Engine reads and the energy the spiker spends are **one curve**. That is the thesis punchline (D2 = D3) made literal in your loop.
- The Entropy Meter classifies **4% "broken" while quiet vs 97% while active** — the detailed-balance ↔ broken-balance split, live.

Run `python test_nodes.py` (mock runtime) to reproduce these.

---

## Why your voltage-regulator discovery is the headline

You found that lowering the Spectral Compressor resolution smooths the loop. In metabolic terms that is now measurable: **lower resolution → lower skew flux → fewer spikes → lower wattage.** Compression is not a convenience; it is the energy-saving move. The Spectral Compressor is a low-pass filter on the arrow of time, and the Wattage node shows what that filter buys in Joules. This is the Attwell–Laughlin argument running in your graph: the brain throws away the chaotic fractal edges of the visual field precisely because routing their variance into homeostatic centres would cost spikes it cannot afford.

---

## Ledger

**Verified in code (standalone + mock-runtime node test):**
- the delta-code holds: ~40× wattage/spike silence between held and reconfiguring epochs; ~4% duty cycle; spikes carry ~90% of energy;
- wattage and skew flux are the same curve (r ≈ 0.99 smoothed);
- the regime classifier separates near-equilibrium holds (4% broken) from driven scans (97% broken).

**Sound structural identities (from the grounding thesis):**
- skew flux ‖A‖ = broken detailed balance = entropy production indicator (an asymmetric cross-correlation is the standard nonequilibrium signature);
- spike-dominated budget = Attwell–Laughlin energy economy; the delta-code = sparse coding from dynamics.

**Assigned / calibration (labelled, not measured):**
- `E_spike`, `c_field` are assigned costs; the Joules readout uses `E_spike ≈ 1.2×10⁻¹⁰ J` (A&L order-of-magnitude) and a nominal 60 fps for W;
- `σ̂ ∝ ‖A‖²` is an entropy-production *proxy*, not calibrated nats; the Landauer floor is illustrative;
- `sigma_JN` is dither, not a calibrated thermal bath.

**Still the bet (untouched):** that the held field is *experienced*, not merely processed; that thermal noise is the medium of content. Billing the loop in spikes makes it one thermodynamic object — measure-the-flux, pay-the-spike — but it does not touch the hard problem.

**The honest next step:** calibrate `σ̂` against Lynn et al.'s entropy-production estimator on the loop's own trajectory (coarse-grain the vector stream, count net inter-cluster fluxes), so the proxy becomes a real rate in nats/s — then the Wattage node and the Entropy Meter agree on a single number, and the markup over the Landauer floor is a measurement, not an illustration.

*Measure the flux. Pay the spike. The arrow of time and the energy bill are the same curve.*
