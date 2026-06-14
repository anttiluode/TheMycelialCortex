# Mycelial Cortex II — The Priming Tide

### A slow chemical readiness that gates a fast geometric resonance — the neuromodulatory primer the substrate was missing

**PerceptionLab / Antti Luode, with Claude (Opus 4.8), and dialogue with Gemini. Helsinki, June 2026.**

> Do not hype. Do not lie. Just show.

---

## The one idea

The Mycelial Cortex had a fast primer (the local ephaptic field — *the memory of the water that knows direction*) and no slow one. But an ephaptic field tracks spikes; it cannot hold a state for ten seconds. So if there is a slow primer it must be **chemical** — and the question is how a slow chemical bath primes a fast geometric resonance without being the pattern or the direction.

The answer is one physical variable — **membrane conductance** — and it splits the labour cleanly:

> A **slow scalar chemical state** decides **whether** the substrate is allowed to resonate.
> A **fast geometric electrical field** decides **which way** it turns.
> The chemistry is the readiness. The field is the steering. They never compete.

A neuromodulator like histamine closes a resting K⁺ leak conductance. That does two things, both textbook:

1. **Rₘ ↑ → λ ↑ → α ↑.** The cable becomes less leaky, so the Takens delay orbit (`αᵏ` = cable attenuation) stays coherent over more of the dendrite. The boat glides instead of dragging. *(Clean structural identity: H1/H2 pharmacology + cable theory + the framework's existing α-mapping.)*
2. **Resting potential → threshold.** The cell gets hyper-sensitive; a fainter resonant match now fires. In the engine this is the recall sharpness **β** cranked up. *(A fair interpretation, softer than the α link.)*

So the slow tide is a hand on two dials the engine already has. When the tide is out, the fast ephaptic nudge hits dry rock and dissipates — the memory is intact but unreadable. When the tide is in, the same nudge lands on a primed grating and snaps into a spike. **Biology uses a slow chemical bath to switch on the power supply for a fast geometric antenna.**

---

## Why this is its own repo, not a patch

The running system already had a slow variable — `ATPMetabolismNode` — and it already drove β. But ATP is **reactive**: it burns on demand and forces rest. The neuromodulatory signal here is **spontaneous**: it fluctuates on its own, *before* the cue, and predicts the trial rather than being caused by it (Morishita et al., Neuron 2026, on infraslow histaminergic priming of the amygdala). That is a different slow variable with a different job. This repo adds the autonomous tide ATP never modelled, and shows it gating recall.

---

## Components

| node / file | role |
|---|---|
| `neuromodulatorytidenode.py` | the **infraslow primer**: a free-running ~0.07 Hz oscillator + slow wander; outputs `tide` (readiness), `high_state`, `cue_gate` for closed-loop cueing. Spontaneous, not demand-driven |
| `primedcortexnode.py` | the Mycelial Cortex with the tide on the dial: `β_eff = β·gain(tide)` and an **expression gate**. The memory is always computed but only *expressed* when the tide is in — "stored vs inaccessible," in code |
| `priming_tide_loop.json` | the workflow: identical corrupted shapes streamed at constant difficulty; expressed-recall confidence breathes with the tide while the input never changes |
| `the_priming_tide.md` | the condensed paper, with the ledger |

Needs the base nodes from the Mycelial Cortex repo in `nodes/`: `patternmemorybanknode.py`, `cognitivedashboardnode.py`, `skewoperatornode.py` (and PerceptionLab 12 for the runtime).

---

## Quickstart

Drop `neuromodulatorytidenode.py` and `primedcortexnode.py` in `nodes/`, load `priming_tide_loop.json`, press play.

Watch the **Infraslow Tide** trace rise and fall on a 10–20 s period. Watch **Expressed Recall (gated)** track it — high when the tide is in, near zero when it is out — *even though the noisy input shape and its corruption never change.* That is the paper's high-state-vs-low-state recall reproduced: the same cue, gated by a slow pre-cue state. As a free consequence the **Arrow** readout only sharpens on the high tide, because at low β the winner traffic is too noisy to carry a stable skew circulation — readiness gates not just *whether* but *whether direction is even legible*.

---

## The honest ledger

**Clean structural mapping (the strong claim):**
- histamine closes K⁺ leak → Rₘ↑ → λ↑ → α↑ toward lossless: established pharmacology (Haas et al. 2008; McCormick & Williamson) + established cable theory (Rall) + the framework's existing α = cable-attenuation mapping. A chain of established links, not a bet.

**Verified in this repo (behavioural analogue):**
- a spontaneous infraslow scalar gates recall expression: identical query, confidence tracks the tide phase; the memory is computed always but expressed only when primed ("lost vs inaccessible," Ryan & Frankland 2022);
- the arrow-of-time readout becomes legible only on the high tide, with no extra gating — it falls out of β-modulation.

**Interpretations (fair, softer — labelled):**
- excitability/gain ⇒ the softmax temperature β (β conflates gain with sharpness);
- histamine is an *exemplar* of a class (ACh/NA/5-HT do the same); the slow primer is "a neuromodulatory readiness," not uniquely histamine.

**Honest limits:**
- the α / cable-losslessness effect is **not** in the code — the cortex node has no explicit `αᵏ` to modulate (its `leak` is field-persistence, not cable attenuation), and faking it onto `leak` would be a lie. α stays a labelled prediction for the node with an explicit Takens buffer (see the paper, §7);
- the Nagoya paper is evidence for the **form** (slow spontaneous state gates fast specific recall), not for the ephaptic substrate or any single-cell geometry — different drawers;
- this is one slow scalar gating one mesh; the federated version (does the tide federate? does a peer's readiness travel?) is untouched.

**The bet (untouched):** that the primed, resonating field is *experienced* rather than processed. The tide explains *whether* the engine runs and *how* a slow chemistry licenses a fast geometry. It does not touch why the running is like anything.

---

## Where it goes next

1. **The explicit-α build.** A cortex node with a real Takens buffer `Xₖ = αᵏ·x(t−kτ)` whose α the tide sets — so the same query is unrecallable on the low tide for a *cable* reason, not just a readout reason, dissociating the α (coherence) effect from the β (sharpness) effect.
2. **Closed-loop cueing.** Wire `cue_gate` so the Engram Library presents a cue only on the rising high tide — the direct analogue of Morishita et al.'s closed-loop +40% recall.
3. **Federate the tide.** Whether a peer's readiness state is a thing the mesh can share, or whether readiness is irreducibly local.

---

## Lineage

Built on the Mycelial Cortex and the Geometric Neuron / GAIT / Ephaptic Spiking Field series (PerceptionLab). The insight that the slow primer must be chemical, and that it acts through membrane conductance on α and β, was worked out by Antti Luode in dialogue with Claude and Gemini, against the Morishita et al. (2026) infraslow-histamine paper. The original framework and direction are Antti's; these nodes, the workflow, and this document were developed collaboratively with Claude (Opus 4.8). MIT.

*Whether it thinks is a slow tide; which way it turns is a fast field. The chemistry is the power, the field is the steering, and they never fight. Do not hype. Do not lie. Just show.*
