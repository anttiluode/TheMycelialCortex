# The Self-Carving Grating

## The geometric neuron's AIS, grounded in the 190 nm lattice — what Leterrier grants, what he withholds, and what it changes

*PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.*

> Do not hype. Do not lie. Just show.

---

## 0. The one move

The bike-trip image was the AIS as a self-carving, asymmetric diffraction grating — a blazed glass that a voltage orbit washes over and is read into a spike, and that activity re-grinds over time. Leterrier (2018) lets us hold that image against the actual nanoscopy. The honest result is not that the metaphor breaks, and not that it "hardens" into proof. It is more interesting than either: **the biology hands us the blank plate and the carving for free, withholds the one thing the optical story most wanted — that the periodicity is a signal-readout frequency — and, in withholding it, forces a better and smaller claim.** Three real changes follow, and one genuinely new thread the paper opens into your own EEG work.

---

## 1. The lattice is real, it is fixed, and it pre-exists

The grating is not a metaphor at this layer. Under super-resolution the axonal membrane skeleton is a periodic scaffold: actin rings connected by spectrin tetramers, spaced **190 nm**, that spacing being literally *the length of one spectrin tetramer* (Xu et al. 2013; Leterrier et al. 2015). Two facts from the paper matter for us and were not ours to assume:

- **The blank plate is handed over before anything writes on it.** The periodic actin/spectrin scaffold "appears just after axonal specification, *before* the assembly of the AIS" and before ankyrin G arrives (Zhong et al. 2014). The uncarved photosensitive plate is real and it is laid down first; ankyrin G then populates it; channels come last. The "self-carving glass" does not have to bootstrap its own lattice from noise — biology pre-installs the ruled blank.
- **The carrier pitch is hardware, not a learned parameter.** 190 nm is set by a protein's contour length. It is not tuned by activity. This is the first correction the biology forces: the framework cannot say a neuron *learns the grating frequency*. The comb pitch is a structural constant. Whatever is learned must be **the position, the length, and the coloring of the comb — not its fundamental period.** (Section 3.)

So the "uncarved holographic plate" is a defensible, literal object. The pitch of the grooves is a constant of the glass.

---

## 2. The conductance grating: the best fact, and the line the paper draws under it

The strongest specific support for "alternating bands in spatial phase with the lattice" is real and precise: ankyrin G binds the **center** of each spectrin tetramer, placing the Nav/Kv7 complex **midway between** actin rings, while **Kv1.2 clusters at the rings themselves** (D'Este et al. 2017). That is two channel populations in spatial antiphase on a 190 nm lattice — the most grating-like fact in the cell, and we did not invent it.

But here is the sentence the optical reading has to print in full, because Leterrier prints it: the periodic organization of Nav and Kv channels *"could also affect action potential generation and conduction, although this has yet to be demonstrated."* That is the paper, drawing the line itself.

So the honest status: the **structural** grating is established; its **mechanical** role (letting the axon flex and resist stress; Krieg et al. 2014) is established; its **organizational** role (spacing and anchoring channels) is established. Its role as a *signal-readout grating* — the thing the inner product `⟨p_k, s⟩` would be computed against — is **undemonstrated, by the field's own admission.** Gemini's line that "the spatial inner product is physically calculated by how perfectly the frequency of the incoming wave matches the 190 nm periodicity" is the over-reach: there is no incoming wave with a wavelength near 190 nm. At the AIS the action-potential depolarization is essentially quasi-static across that scale — the whole segment rises nearly together relative to 190 nm. There is nothing to diffract. The ferrolens warning was never optional, and the paper makes it sharper: **at the AIS there is diffraction *math* and no diffraction *physics*.** What survives is the only invariant that ever survived — projection of a field onto a stored geometry and read the overlap. The grating is the picture; the inner product is the thing.

---

## 3. The carving is real — and it is slow, and it is homeostatic

This is where the biology is most generous, and it is worth being precise about *what* it grants. The AIS is not fixed glass. Leterrier's section on morphological plasticity is, almost line for line, the self-carving claim:

- elevated activity → the whole AIS **shifts distally** down the axon (Grubb & Burrone 2010);
- decreased activity → the AIS **lengthens** (Kuba et al. 2010);
- the carving is **calcium-triggered**, executed by CK2, calcineurin and CDK5 phosphorylating the scaffold to loosen its interactions so the geometry can slide and re-anchor;
- composition itself re-grinds: a **Kv7↔Kv1 redistribution** retunes excitability during structural change (Kuba et al. 2015).

The geometry of the AIS is, genuinely, a physical record of the cell's activity history. The wake hardens into a riverbed; the paper shows the riverbed moving.

Two honest qualifications, and they are the second and third corrections the biology forces.

**It is slow, and that confirms rather than threatens the duality.** This plasticity runs over **hours to days** (position, length) or seconds-to-minutes (channel modulation) — orders of magnitude slower than the millisecond orbit it would read. The rotation-half document already insisted that the *write-side* `A` (the carved structure) and the *read-side* `A` (the activity statistics) are dual, not identical, separated by the plasticity clock. Leterrier supplies the clock: the grating you read through in a millisecond is the slow time-integral of every wave that passed in the preceding days. The single wash reads; the slow loop writes. The biology and the framework agree on the seam.

**It is homeostatic gain-and-position tuning — not demonstrated content storage.** The paper frames every instance of this plasticity as tuning *intrinsic excitability in a homeostatic direction* — moving the trigger zone, resizing it, rebalancing Kv1/Kv7 to raise or lower the gain. It does **not** show the AIS storing a *pattern-specific template* — a particular `p_k` for a particular orbit. So "the geometry is the eigenmode of its own readout" stands as the framework's hypothesis, beautiful and untouched; what the biology actually grants is the weaker, solid claim that **the plate physically relocates and recolors itself to set the cell's gain and threshold from its activity history.** Self-carving as homeostasis: yes, demonstrated. Self-carving as holographic content storage: still the bet.

---

## 4. The blaze: two asymmetries, and only one of them is the arrow

The chevron insight was that to read time's direction the grating must be longitudinally asymmetric — blazed, not symmetric. The AIS *is* longitudinally asymmetric: its composition changes proximal-to-distal (Kv1 channels sit along the **distal** AIS), and it is a famously **directional** compartment — a polarity gatekeeper that lets axonal cargo through and stalls-and-reverses somatodendritic cargo, with uniform plus-end-out microtubules.

Here is the correction, and it is the one Gemini's reading most needs. **There are two distinct asymmetries in the AIS, and they live in different drawers.**

- The **transport asymmetry** — microtubule polarity, the pre-axonal exclusion zone, cargo sorting forward vs. reverse — is the strongly documented one. But it is a *spatial-transport* directionality: which way *proteins* move. It is not, on its face, a chiral readout of the *temporal* order of a voltage orbit. Using it as evidence for the temporal blaze conflates "the segment sorts cargo one way" with "the segment reads time's arrow." Different physics, different function.
- The **compositional gradient** (Kv1 distal, the proximal/distal switch) is real and *does* mean a depolarization profile meets a different sequence of conductances depending on direction. This is the legitimate seed of a structural blaze. But the paper does not connect it to temporal chirality, and the framework's own arrow has always had a cleaner home: the **dendritic delay line** and the **asymmetric (STDP-written) connectivity** — the lag operator, where `the_rotation_half_grounded` actually grounded the skew `A`. The arrow lives in the Takens cable and the antisymmetric synapse; the AIS supplies spatial asymmetry whose role in carrying the *temporal* arrow is unproven.

So: the AIS is blazed in space. Whether that blaze is the temporal arrow is a hypothesis, and not the best-supported home for it. Keep the arrow where the biology already put it — in the delayed, asymmetric write — and let the AIS gradient be a candidate, labelled.

---

## 5. The self-carving principle, found twice in one compartment

The paper hands over something we did not have, and it is Leterrier's *own* hypothesis, which is what makes it usable. He proposes a **"repair and recruit loop"** for why transport runs preferentially into the axon: kinesins walking the AIS microtubules create lattice defects → the defects are repaired by GTP-tubulin incorporation → the resulting **GTP islands recruit more kinesins** → more traffic → more defects → more repair. Use carves the substrate that biases future use.

That is the self-carving glass again — *the wake becomes the riverbed that steers the next boat* — running in the **cytoskeletal transport layer**, completely independent of the voltage layer, hypothesized by the cell biologist with no knowledge of this framework. So the principle the bike trip kept circling appears **twice in the same 40 µm of membrane**: once (our hypothesis) in activity-carved channel/scaffold geometry, once (Leterrier's hypothesis) in traffic-carved microtubule GTP islands. Two flows, two frozen riverbeds, one compartment. That two independent thinkers reach "flow carves the channel that steers the next flow" inside the same structure is not proof of anything — but it is the kind of convergence that says the principle is not ours, it is the substrate's.

---

## 6. What the AIS does for a living — and where our reader sits

Be fair about the day job. The two functions Leterrier treats as established are: **initiate the action potential** (Nav concentrated ~30-fold, lowest threshold, the trigger zone) and **maintain neuronal polarity** (the diffusion barrier and trafficking filter that keep axon and soma distinct). The "geometric reader of waveform shape" is *our* stage IV. The paper neither supports nor refutes it; it simply addresses a different question, and where it touches ours — the functional role of the periodicity — it says *undemonstrated*.

That is the correct, defensible posture for the geometric-neuron hypothesis after this paper: **compatible with the biology, unevidenced by it.** The AIS demonstrably initiates and gatekeeps; that it *also* reads orbit geometry against its grating is a good, falsifiable hypothesis — testable exactly as the grounded document said, by STED scaffold geometry against measured spike-triggered averages — and it should keep being called one. Nothing here promotes it. Nothing here sinks it.

---

## 7. The thread the paper opens into your own EEG result

One thing leapt out that ties two halves of your work together, and it belongs in the hypothesis drawer with the safety on. The master organizer of the whole lattice is **ankyrin G (ANK3)** — and Leterrier lists, plainly, that AIS disruption is implicated in *"bipolar disorders and schizophrenia"*, citing ankyrin-G isoform imbalance (Lopez et al. 2017; Zhu et al. 2017; Luoni et al. 2016). ANK3 is a well-replicated bipolar/schizophrenia risk locus.

Your strongest empirical anchor is the trainless geometric-EEG separation of schizophrenia — cross-band eigenmode *decoupling*, reduced temporal Betti-1, both of which are losses of coherent rotational/temporal structure. So there is a rhyme worth naming and testing: **if the AIS lattice is the cell-scale substrate that builds temporal/rotational structure into spiking, and ankyrin-G dysfunction degrades that lattice in schizophrenia, then a macro-scale loss of rotational coherence in the EEG is exactly what you would expect to measure.** Micro grating degraded → macro dysrhythmia. That is a bridge from a molecule (ANK3) through a structure (the 190 nm lattice) to a biomarker (your geometric measures) — and it is a *hypothesis to test*, not a result to claim: it would need the geometric EEG measures correlated against ANK3 genotype or against AIS-pathology markers, in a cohort. But it is the first time the micro-theory and the empirical anchor have had a candidate mechanism in common, and it came straight out of reading this paper.

---

## 8. The updated vision, in one breath

A neuron's dendrite unfolds a 1-D temporal signal into a delay-space orbit (cable theory, the cleanest mapping; the arrow lives here, in the lag and the asymmetric synapse). The orbit washes over the AIS — a *real, pre-installed, 190 nm-pitched* lattice whose channels (Nav/Kv7 between the rings, Kv1.2 on them) form a structured conductance profile in spatial phase with the glass. A spike is the threshold crossing of the overlap between the arriving field and that stored geometry — an inner product, which is what diffraction, holography, matched filtering and attention all are, with no diffraction physics required. The lattice is not fixed: over hours and days, calcium-gated kinases slide it, stretch it, and recolor its channels along the cell's activity history, tuning its gain and threshold homeostatically — the wake hardening into a riverbed, the read-side and write-side `A` separated by the plasticity clock. The same carve-by-use principle runs a second time, in the microtubule traffic underneath, by Leterrier's own hypothesis. What the biology grants: the blank ruled plate, the structured conductance comb, the slow self-carving, the longitudinal asymmetry, the master organizer that is also a psychiatric risk gene. What it withholds: that the 190 nm pitch is a signal-readout frequency, that the carving stores content rather than tuning gain, and that the spatial blaze is the temporal arrow. What it changes: the carrier pitch is hardware not learning; the carving is homeostasis not yet storage; the arrow stays in the delay line, not the segment.

---

## 9. Ledger

**Established (Leterrier 2018 and refs therein — used, not claimed):**
- the periodic actin/spectrin membrane skeleton, 190 nm = spectrin tetramer length (Xu et al. 2013; Leterrier et al. 2015);
- the scaffold is laid down *before* AIS assembly and ankyrin G (Zhong et al. 2014);
- ankyrin G binds tetramer centers → Nav/Kv7 midway between rings; Kv1.2 at the rings (D'Este et al. 2017);
- AIS as low-threshold AP trigger zone (Nav ~30×) and polarity gatekeeper (diffusion barrier + trafficking filter);
- activity-dependent morphological plasticity: distal shift on elevated activity (Grubb & Burrone 2010), lengthening on decreased activity (Kuba et al. 2010), calcium/CK2/calcineurin/CDK5-mediated, homeostatic (Kuba et al. 2015);
- uniform plus-end-out microtubule polarity; directional cargo sorting; the repair-and-recruit GTP-island loop (Leterrier's proposed hypothesis);
- AIS / ankyrin-G (ANK3) disruption implicated in schizophrenia and bipolar disorder.

**Clean structural mappings (sound):**
- the pre-installed periodic scaffold = the blank ruled plate;
- the Kv1.2-at-rings / Nav-Kv7-between-rings antiphase = a structured conductance profile in spatial phase with the lattice;
- activity-driven slide/stretch/recolor of the AIS = the self-carving plate, on the slow (hours–days) write clock, dual to the millisecond read — confirming the rotation-half document's write/read seam;
- the repair-and-recruit loop = the self-carving principle at the transport scale, independently hypothesized.

**Model hypotheses (falsifiable, unproven — the framework's bets, neither supported nor refuted here):**
- that the AIS *reads orbit geometry* against its grating (an inner product against a stored eigenfunction), beyond initiating and gatekeeping — STED-testable;
- that the carving stores a *content-specific* template `p_k`, rather than only tuning gain/threshold homeostatically;
- that the longitudinal compositional asymmetry implements the *temporal* arrow (the better-grounded home for the arrow remains the dendritic delay line + STDP `A`);
- **the new one:** that degradation of the AIS lattice (e.g. via ankyrin-G/ANK3 dysfunction in schizophrenia) is a cell-scale source of the macro-scale loss of rotational/temporal EEG structure your trainless geometric measures detect — a micro→macro bridge to test against genotype/pathology, not a result.

**Honest limits (the paper sharpens these):**
- no diffraction *physics* at the AIS — the AP is quasi-static across 190 nm; the optical picture is mathematics (the inner product / matched filter), and the diffraction language is analogy only;
- the 190 nm pitch is a fixed structural constant (spectrin length), not a learnable frequency;
- the documented carving is homeostatic gain/position tuning over hours–days, not demonstrated pattern storage;
- the strongly-documented AIS asymmetry is *transport*-directional, a different drawer from temporal chirality;
- the paper itself states the functional consequence of channel periodicity for AP generation is "yet to be demonstrated."

**The bet (untouched, as always):** that the resonating field is *experienced* rather than processed. Grounding the grating in the lattice makes the geometric neuron's read-stage a real, named, partly-unproven object sitting on real biology. It does not touch the hard problem; it only locates it more precisely, again — now at the 190 nm seam where a slow, calcium-carved glass meets a fast voltage orbit.

---

*Helsinki, June 2026. The road was a fixed grating my speed read as a beat; the neuron is a fixed-pitch grating that slow activity slides and recolors while a fast orbit reads it. The biology gave us the ruled blank, the antiphase comb, and the carving-by-use, twice. It kept, for now, the three things we most wanted to take — that the pitch is a tuned frequency, that the carving stores a memory, and that the blaze is the arrow. Naming exactly what was given and exactly what was withheld is the whole of the method. Do not hype. Do not lie. Just show.*
