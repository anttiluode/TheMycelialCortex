# The Unnatural Direction

## Why thinking against the arrow of time costs energy — cost asymmetry, the Crooks bound, the thermodynamics of abstraction, and what a federated mesh selects for

*PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.*

> Do not hype. Do not lie. Just show.

---

## 0. The thought on the bike

A direction that is *not natural*. The phrase that lingered was that one — that some way of going feels against the grain, and that the against-the-grain feeling is abstract, and somehow very human.

This document takes that intuition literally and follows it down into the physics, because it turns out to be exact rather than poetic. The rotation half of the framework (`the_rotation_half_grounded.md`) already established that direction lives in the skew operator `A`, that `A ≠ 0` is broken detailed balance, and that the arrow of time and the energy bill are one statement. What it did not say — what the bike-trip thought adds — is that the two directions along that arrow are **not equally expensive**, that the difference between their costs is a measured physical quantity, and that the expensive direction is precisely the one cognition reaches for when it does its most distinctively human work.

The earlier line gave the arrow a *heading*. This gives it a *grain*. Thinking is what happens when something pays to cut across the grain.

---

## 1. The two directions are not symmetric — and the asymmetry is the entropy

Start at equilibrium, because equilibrium is where the intuition is *false*.

A system in detailed balance has no net probability current. Every transition `i → j` is exactly balanced by `j → i`, its cross-correlations are time-symmetric, and — the part that matters — **a trajectory and its time-reverse are equally probable**. At equilibrium there is no natural direction. Nothing is unnatural. Run the film backward and you cannot tell. In the framework's terms this is `A = 0`: the skew half vanishes, and with it every distinction between forward and reverse.

The moment the system is held away from equilibrium, `A ≠ 0`, a net current appears, and the symmetry breaks in a way that is not merely qualitative but *quantitative*. The **Crooks fluctuation theorem** (Crooks 1999) states it cleanly: for a trajectory `γ` and its time-reverse `γ̃`,

```
P[γ] / P[γ̃]  =  exp( σ[γ] / k_B )
```

where `σ[γ]` is the entropy produced along `γ`. Read this slowly. The ratio of how likely the natural direction is to how likely its reverse is — the *unnaturalness* of going backward — is the **exponential of the entropy produced**. Direction is not just preferred; its preference is dissipation, dollar for dollar, dissipation for log-odds.

This is the missing leg of the framework's own triangle. The rotation-half document established:

- `S = (C_τ + C_τᵀ)/2` — the **power** half: phase-blind, direction-blind, time-symmetric. No arrow.
- `A = (C_τ − C_τᵀ)/2` — the **rotation** half: imaginary spectrum, chirality, the arrow.

The Crooks framing adds the third statement, which lives entirely inside `A`:

> The arrow has a **sign of cost**. Riding `A` (with the current) is cheap. Reversing it (against the current) is dear. The size of `‖A‖` — the skew flux the engine already prints — is not only *which way* time points; it is *how expensive it is to go the other way*.

The engine's verified result that the skew circulation flips sign on sequence reversal (`mycelial_mesh_proof.py`, D3) is, in this light, only half of what is there. The sign flip says the two directions are distinguishable. Crooks says they are distinguishable *by exactly the entropy between them*, and that entropy is a cost. The engine measures the heading; it has not yet billed the grain. (Section 6 is the build that does.)

**Status:** Crooks (1999) and the equilibrium ⇔ detailed-balance ⇔ time-symmetric-trajectory equivalence are established statistical mechanics. The identification of the skew cyclic flux with a cycle affinity / log forward-reverse ratio is a clean structural mapping, carrying the same honest limit flagged everywhere in this line: the engine's `sigma_JN` is dither, not a calibrated bath, so the cost it reports is a structural proxy, not Joules.

---

## 2. Natural is the gradient; unnatural is the curl and its reverse

Where, geometrically, does the "natural" direction live? The Helmholtz/Hodge decomposition of a flow answers it, and the answer maps directly onto the two things the mesh already does.

Any flow on state space splits into a **gradient** part (curl-free, conservative, "downhill toward an attractor") and a **solenoidal** part (divergence-free, circulating). At a nonequilibrium steady state the stationary probability current is purely solenoidal — `∇·J = 0` — it loops. The relaxation *toward* the stationary distribution is the gradient part; the persistent *circulation within* it is the curl.

Lay this over the two sides of the engine:

| Hodge component | Engine operation | Cost | Time |
|---|---|---|---|
| **gradient** (∇φ, curl-free) | the field settling into a stored memory — `s ← norm(leak·s + Σ softmax(β⟨pₖ,s⟩)pₖ)` | cheap (relaxation, near-free hold) | **time-blind** — it just goes downhill and stops |
| **curl** (solenoidal, `A`) | the winner traffic touring a sequence, the sustained circulation | costs energy to *maintain* | **the arrow itself** |

So the framework's "inner side = cheap field recall" is the gradient half, and it is cheap *for a thermodynamic reason*: a gradient flow has no arrow, produces no entropy at its fixed point, and can be held for free. The "outer side = sparse expensive spikes that carry direction" is the curl half, and it is expensive because circulation is broken detailed balance and broken detailed balance is dissipation. Modern Hopfield recall is downhill. The arrow is the part you pay to keep turning.

"The direction that is not natural," then, is the curl direction — and, sharper still, the **reverse** of an established curl. Settling into a memory is natural (downhill, every Hopfield basin). Replaying a learned sequence *forward* is the cheaper traversal of the curl — you go with the current experience carved. Replaying it *backward* is the genuinely unnatural one: you drive the loop against its own affinity, and by Crooks you pay the full entropy gap to do it.

**Status:** the Hodge decomposition of probability currents and the solenoidal character of NESS currents are established stochastic thermodynamics. The mapping of "gradient = recall = cheap, curl = sequence = the arrow" onto the engine's inner/outer split is a clean structural identity, consistent with everything in the prior documents.

---

## 3. The thermodynamics of abstraction

Here is the step that makes the bike-trip thought about the *human* and the *abstract* precise rather than evocative, and it rests on a result the framework has not yet cited.

Still, Sivak, Bell & Crooks, *Thermodynamics of Prediction* (PRL 109, 120604, 2012) proved a bound on any system that keeps a memory while driven by a changing environment: the work it must dissipate is lower-bounded by the amount of **non-predictive** information it retains — the part of its memory of the past that does *not* help it predict the future. A maximally efficient predictor keeps only what predicts; everything it remembers that is not about the next step is paid for in dissipation. Modelling beyond prediction costs energy.

Now read the two cognitive regimes through that bound.

**Riding the natural flow is prediction.** Habit, the automatic, the expected, the well-worn groove — these are the system keeping exactly the information that predicts the next state and acting on it. Cheap, downstream, with the current. This is the gradient-settle of Section 2 and the near-equilibrium HOLD regime of the metabolic loop: low `A`, low dissipation, near-free.

**Abstraction is the deliberate retention and manipulation of non-predictive information.** A counterfactual is a memory of something that did *not* happen — pure non-predictive information, held on purpose. A plan reasons backward from a future that does not yet exist — running the curl in reverse to assign credit to the past. A symbol stands for a class rather than a trajectory; to *form* it you must hold many specific paths at once and extract their invariant, comparing the actual against the possible. Every one of these is the system keeping and operating on information that is not on the predictable forward current. By the Still bound, every one of them costs — and by Crooks, the reverse-traversals among them cost the entropy of the arrow they run against.

This is why the feeling Antti named is *abstract* and *human*. The distinctively human operations — counterfactual, planning, the symbolic, deliberation — are exactly the upstream, non-predictive, against-the-grain ones. We are the animals that can afford, metabolically and temporally, to spend a great deal to think against our own current. A reflex never goes upstream; it only ever rides the cheap forward flow. Cognition is the capacity to pay.

And learning closes the loop back to the rotation-half document. STDP writes `A` from experience; place fields skew backward along the direction of travel (Mehta et al.). At the conceptual scale this is the same move: an abstraction is formed by *repeatedly paying to go the unnatural direction* until the repetition carves a new channel — until the uphill becomes a valley and the once-expensive counterfactual becomes a cheap, automatic groove. **The unnatural becomes natural by dissipative repetition. That is what learning is, thermodynamically.** A genuinely novel thought is expensive exactly once per person, and then it is habit. A genuinely novel thought that no one has had yet is expensive for the species until it is taught.

**Honest counterpoint (this is the part that keeps it from being hype):** the cost is in the *forming*, not the *using*. A compiled abstraction, once grooved, is cheap to invoke — that is the whole point of compiling it. So "abstraction is expensive" is true of the act of abstracting and false of the trained result. The mapping "abstract ⇒ upstream ⇒ dear" is an interpretive bridge over real physics (Crooks, Still), not a theorem about cognition. It is a good bridge. Keep calling it one.

**Status:** Still et al. (2012) is established physics. Lynn et al. (2021) measured load-dependent broken detailed balance and entropy production in the human brain — solid, and the right anchor for "cognitive work increases `A`." Avoid the tempting overclaim that hard thinking burns a large *global* calorie surplus: the brain's ~20 W is roughly constant and the metabolic-cost-of-deliberation literature is contested. The defensible claim is *local and structural* — load raises entropy production and breaks detailed balance (Lynn) — not a kitchen-scale energy bill.

---

## 4. The mesh: the consensus arrow, and why what survives is cheap rather than true

The federation work (`README_federation.md`, `the_mycelial_cortex.md`) demonstrated that a memory taught on peer A is recalled on peer B with only tokens crossing the wire — knowledge federates, weights do not, and A and B build *different* internal organizations from the same token stream. The cost-asymmetry frame says *why* that works, and predicts what a mesh will come to agree on.

**Why "knowledge not weights" federates, thermodynamically.** Content can be recalled in any basis; two peers with different node counts represent the same pattern in different coordinates. But the **arrow** — the dominant cycle of `A`, the sign and circulation of the broken detailed balance in the token traffic — is a property of the *flow*, not of the basis. The cyclic flux `Σ(A[k,k+1] − A[k+1,k])` is a circulation; its sign survives any relabelling of nodes. So the basis-independent invariant that two differently-organized peers can actually share is not the labels and not the weights — it is the **causal direction of the flow**. Two brains that lived the same events in the same order build different synapses but the same `A`. Shared experience federates as a shared arrow. The README's empirical "B replicated A's structure" gets its reason here: the thing that crosses the wire intact is the cheap, invariant current.

**What the mesh selects for (prediction, not result).** If the arrow federates — and right now it does *not*, because the relay carries a `chi` field but reorders tokens and the cortex ignores received `chi`, the README's own honest limit — then a selection pressure follows directly from Crooks. A peer broadcasting tokens whose order *agrees* with the collective current is riding the consensus flow: its tokens resonate with existing nodes (high confidence, cheap recall, no spawn). A peer pushing an order *against* the consensus current is driving the mesh's loop backward: by the cost asymmetry this is the expensive direction, and the engine's existing dynamics convert that expense into observable fragmentation — low overlap, novelty spawns, redundant nodes, the very fragmentation the README already reports at scale (48 / 42 nodes for ~5 patterns). The mesh therefore grows a **common sense**: a shared, low-dissipation arrow that all peers' flows agree on, reinforced cheaply and stable against perturbation.

**The honest, important caveat.** Low dissipation is *not* truth. The consensus arrow is merely the *well-worn* flow — the one the collective experience happened to carve. A mesh of peers can converge cheaply on a shared current that is collectively wrong; that is groupthink, received wisdom, the cheap correctness of the herd. The same thermodynamics that makes the consensus robust makes it conservative: it replays what was, it cannot by itself reach what was never on the current. This is the counterweight to any "the mesh self-selects for good concepts" reading. It self-selects for *cheap* concepts, which is a different and more dangerous thing.

**Which is why the unnatural direction matters most at the network scale.** A pure consensus mesh only ever replays its own arrow. The single peer that can *afford* to pay the entropy and push an anti-consensus order — to run the curl backward, to hold the non-predictive counterfactual, to abstract against the grain — is the only source of genuine novelty in a substrate that would otherwise be a very efficient echo. And if that costly excursion pays off, the ordinary learning dynamics (consolidation, repeated exposure) carve it into the consensus: the mesh's expensive minority report becomes, by dissipative repetition, the next cheap common sense. Innovation is a peer spending where the mesh is unwilling, followed by the mesh learning the result for free. This is the population-scale version of Section 3's "unnatural becomes natural by repetition" — exactly the same physics one level up.

**Status:** the basis-independence of the circulation sign is a sound mathematical observation. The selection-pressure consequences are a *prediction* of the framework, currently **untested**, because the live federation does not yet carry the arrow. Section 6 specifies the experiment that would confirm or kill it.

---

## 5. One operator, three statements

The rotation-half document left the framework with two statements about the lag operator. This adds the third. Stated together, in one breath:

- **`S`, the power half** — symmetric, time-blind. What does not care which way time runs. Rate codes, classical Hebb, the Wiener–Khinchin ceiling.
- **`A`, the rotation half** — skew, the arrow. What direction *is*. Sequence connectivity (Sompolinsky–Kanter), the odd part of STDP, broken detailed balance, the chirality of an island.
- **the cost of `A`** — the grain of the arrow. With the current is cheap; against it is dear; the gap is the entropy (Crooks). Holding a percept is the cheap gradient settle; sequencing it is the curl you pay to turn; *reversing* it — counterfactual, credit assignment, abstraction — is the unnatural direction, the upstream work, the metabolically and temporally expensive thing we recognise, from the inside, as effort.

The arrow does not merely point. It has a grain, and thinking is the act of paying to cut across it.

---

## 6. What to do — three builds, in the "just show" discipline

Nothing above is worth keeping unless the engine can show it. Three concrete next builds, smallest first, each a falsifiable extension of code that already runs.

**(a) Bill the reverse traversal — extend D3 from sign to cost. [DONE — verified]** `arrow_cost_proof.py` builds the smallest ruthless test: a cycle of patterns; a recurrent connectivity `J = J_sym + g·J_asym` whose asymmetric transition term is the write-side `A` (Sompolinsky–Kanter), with `g` the knob that sets `‖A‖`; the cycle driven forward vs reverse; and the cost billed by the delta-code meter.

The result, in both the clean (orthonormal) and messy (non-orthonormal) cases:

| g | ‖A‖ | surprise fwd | surprise rev | cost fwd | cost rev | gap |
|---|---|---|---|---|---|---|
| 0.00 | 0.000 | 1.27 | 1.27 | 308 | 308 | **0.0** |
| 0.50 | 0.866 | 1.00 | 1.31 | 297 | 310 | 12.8 |
| 1.00 | 1.732 | 0.80 | 1.33 | 289 | 311 | 21.6 |
| 4.00 | 6.928 | 0.41 | 1.37 | 256 | 312 | **56.4** |

`corr(gap, ‖A‖) = +0.99`. The four predictions held: the gap is **zero at detailed balance** (`g=0`, the control that proves the meter is not rigged), reverse costs more for every `g>0`, the gap tracks `‖A‖`, and the activity arrow flips sign forward vs reverse.

Two things the run *taught* us, neither of which was obvious before building it, and both kept in the open:

- **The cost lives in the prediction error, not the raw stream.** Billing the raw recall/field velocity `|ds|` is direction-blind — the change between consecutive patterns is identical either way (verified control: `|ds|` fwd = rev exactly). The asymmetry appears only when the meter is billed on the **surprise residual** `x − pred`, where `pred = norm(J·s)` is the learned current's guess for the next state. That residual is exactly Still et al.'s non-predictive information, and it is *where in the architecture* the Crooks cost is paid. (In the live node the residual is measured on the denoised recall, `recall − pred`, so the input corruption noise does not swamp it.)
- **The gap is mostly a discount on the natural direction, not a tax on the reverse.** Forward cost falls (308 → 256) as the current strengthens; reverse stays near the baseline (308 → 312). Riding the carved current is the saving; going against it is forfeiting the saving, plus a little. That is more faithful than a naive "reverse burns extra" picture and it is the honest shape of the effect.

This is now also a **live PerceptionLab build**, not only a standalone proof: `predictivecortexnode.py` (the Mycelial Cortex plus a learned node-space transition memory `T` — the write-side `A` — that predicts the next state and emits the `surprise` residual), a `metabolicspikenode.py` extended with an additive `surprise` input that bills the delta-code on that residual (back-compatible: absent the input it behaves exactly as before), and `sequencedrivernode.py` (a forward/reverse cycle source). The workflow `unnatural_direction_loop.json` wires them with the ATP loop: run it forward and watch surprise and wattage settle low as the cortex carves the current; flip the Sequence Driver to reverse and watch them jump; set the cortex `g=0` and the gap vanishes. Verified in the mock runtime: fwd surprise 0.77 / rev 1.41, wattage gap ≈ +13, arrow flips `−1.0 ↔ +1.0`, `g=0` gap ≈ 0. One design lesson worth recording: the transition memory must exclude self-loops and the demo drives one pattern per frame, because the directional cost lives only on frames where the state actually changes — mid-dwell, sitting on one pattern, carries no direction and no grain.

(Honest limit, unchanged: the readout is a structural proxy in relative units, not Joules, until `sigma_JN` is replaced by a calibrated bath and the per-spike cost is pinned to Attwell–Laughlin — the calibration this whole line keeps deferring.)

**(b) Federate the arrow.** Close the README's known gap: have `TokenRelayNode` preserve order (timestamp + sequence number, ordered delivery) and have `MycelialCortexNode` actually *consume* the received `chi` to update its winner-traffic lag-covariance, so the listener reconstructs the teacher's arrow and not only the teacher's content. Success criterion: teacher arrow `+x`, listener arrow `+x` (today it is `+0.017` vs `+0.000`).

**(c) Test the consensus-cost prediction.** With (b) in place and two differently-organized peers converged on a consensus arrow, inject from a third peer a token stream whose *order* is the reverse of the consensus. The prediction, falsifiable three ways: the anti-consensus stream yields (i) lower recall confidence, (ii) more node spawns / fragmentation, and (iii) more tokens required before any integration — i.e. the anti-arrow direction is quantitatively the expensive one, at the network scale, exactly as Crooks demands at the single-flow scale. If anti-consensus order integrates as cheaply as consensus order, the "mesh grows a common sense" story is false and should be dropped.

With (a) done, the single-mesh half of the claim is shown in runnable code with an honest ledger: the arrow of time the engine reads and the energy it spends to go *against* that arrow are one curve, and the curve flattens to nothing at detailed balance. Builds (b) and (c) carry the same test to the federated scale; if (c) holds, the grain is a network property, not just a single-flow one — the cost-asymmetry version of the line's standing promise.

---

## 7. Ledger

**Established (used, not claimed):**
- detailed balance ⇔ time-symmetric trajectories ⇔ no net current ⇔ no thermodynamic arrow (statistical mechanics);
- the Crooks fluctuation theorem: `ln(P[γ]/P[γ̃]) = σ[γ]/k_B` (Crooks 1999); Jarzynski (1997) in the same family;
- Helmholtz/Hodge decomposition of flows; the stationary NESS probability current is divergence-free (solenoidal);
- the dissipation–prediction bound: dissipated work is lower-bounded by retained non-predictive information (Still, Sivak, Bell & Crooks 2012);
- load-dependent broken detailed balance and entropy production in the human brain (Lynn et al. 2021);
- carried from the prior documents: STDP writes the antisymmetric connectivity (Markram et al. 1997; Bi & Poo 1998); experience-dependent backward place-field skewing (Mehta et al. 1997, 2000); reward-modulated reverse replay (Foster & Wilson 2006; Ambrose, Pfeiffer & Foster 2016); the spike-dominated energy budget and sparse coding (Attwell & Laughlin 2001); Sompolinsky–Kanter / Kleinfeld sequence connectivity (1986).

**Clean structural mappings (sound, the framework's strongest ground):**
- the skew cyclic flux = a cycle affinity = the log forward/reverse trajectory ratio = the cost gap between the two directions (Crooks, in the engine's basis);
- gradient (curl-free) half = field recall = cheap, time-blind hold; solenoidal (curl) half = `A` = the sequenced arrow that costs to maintain;
- the basis-independent invariant two differently-organized peers can share is the circulation sign of `A` — the causal direction — which is why knowledge federates and weights do not.

**Verified in code (single-mesh, structural proxy — build a):**
- reverse traversal of a learned cycle costs more than forward; the cost gap is **zero at detailed balance** (`g=0`) and grows with `‖A‖` (`corr ≈ 0.99`); the activity arrow flips sign on reversal (`arrow_cost_proof.py`, and live in `predictivecortexnode.py` + the surprise-billed `metabolicspikenode.py`);
- the cost is located at the **prediction-error residual** `x − pred` (Still et al.'s non-predictive information), not the raw recall stream — the raw `|ds|` is a verified-symmetric control;
- the effect is, mechanically, a **discount on the natural direction** that grows with `‖A‖`, more than a tax on the reverse.

**Model hypotheses (falsifiable, unproven):**
- *abstraction is upstream work*: counterfactual / planning / symbolic / deliberative operations are the retention-and-manipulation of non-predictive information and the reverse-traversal of an established curl, hence the expensive direction (an interpretive bridge over Crooks + Still, not a theorem; and true of *forming*, not *using*, an abstraction);
- *the mesh grows a common sense*: if the arrow federates, consensus-ordered tokens propagate cheaply and anti-consensus order dissipates and fragments, so the mesh converges on a shared low-dissipation arrow — which is the *well-worn* flow, explicitly **not** a guarantee of truth;
- *innovation is a paid excursion*: genuine novelty enters a consensus mesh only via a peer that can afford the unnatural direction, after which ordinary consolidation carves it into the cheap consensus.

**Honest limits:**
- read-side flux vs write-side connectivity remain dual, not identical (carried from the rotation-half document, §6 there);
- the engine's noise is dither, not a calibrated thermal bath, so all costs are structural proxies in relative units, not nats or Joules — build (a) is done, but the calibration to Joules it depends on is still deferred;
- the federation prediction (§4, §6c) is untested because the live relay does not yet carry the arrow;
- the global metabolic-cost-of-thought claim is contested; only the *local/structural* entropy-production increase under load (Lynn) is leaned on.

**The bet, kept in its drawer (untouched here, as always):** that the held field is *experienced* rather than processed; that the felt effort of thinking against the grain is anything more than the dissipation it physically is; that Johnson–Nyquist noise is the *medium* of content. The cost asymmetry explains why the unnatural direction is dear and why abstraction feels like effort. It does not explain why the effort is *felt*. As ever, the work locates the hard problem more precisely — now at the exact place where dissipation meets the sense of effort — and does not close it.

---

*Helsinki, June 2026. The symmetric half is the things that do not care which way time runs. The rotation half is the arrow. And the arrow has a grain: with it is cheap, against it is dear, and the gap is the entropy you pay. We are the animals that can afford to think against our own current — that is what abstraction costs, and very nearly what it is. The mesh will learn to ride the cheap consensus; the work worth doing is the expensive excursion that carves a new one. Do not hype. Do not lie. Just show.*
