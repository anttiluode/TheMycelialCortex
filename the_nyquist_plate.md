# The Nyquist Plate

## Grid cells as the optimal sampling lattice at the Fourier plane of a holographic cortico-hippocampal projection — the optics, the maths, and why the grid sits exactly where it sits

*PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.*

> Do not hype. Do not lie. Just show.

---

## 0. The question, made small enough to answer

The vision keeps circling one image: the brain as a holographic projector, frequencies thrown across a loop, an image encoded, stored, and read back. The image is large and the temptation is to claim all of it. This paper claims one joint of it, the joint that the `sigh_image` experiment and the grid-cell anatomy together actually pin down:

> **Why would the *middle* of the cortico-hippocampal loop — the entorhinal cortex — sit at the Nyquist regime? What lens does that imply, and why are the grid cells there and not elsewhere?**

The answer, in one line, is the spine of the whole document: **the entorhinal cortex is the place where a continuous cortical field is *sampled* into a discrete code, and a sampler is *defined* by its Nyquist limit.** Everything else — the hexagonal lattice, the modules, the aliasing, the place-cell reconstruction — is the detailed fingerprint of an optimal sampler sitting at a Fourier plane. The grid is where it is because a sampler has exactly one correct place to live: the interface between the analog cortex and the discrete hippocampal store.

The optics that follow are rigorous where the established grid/place mathematics is rigorous, and labelled as a bet where the framework reaches past it. Keep the drawers separate, as always.

---

## 1. What `sigh_image` already shows (the ground truth to build on)

`sigh_image.py` is, stripped to its core, a radial spatial-frequency filter on a 64×64 field. It Fourier-transforms the image, builds a map of normalized squared frequency `k²` running from `0` at DC to `1` at the spectrum's corner, looks up a 1-D gain curve at each pixel's `k²`, multiplies, and inverse-transforms. The honest content of that little machine is three regimes along one axis:

- **`k² → 0`: the gist.** The low frequencies — the coarse blobs, the envelope, the "what is this roughly." Lossy, sufficient for recognition, cheap.
- **`k² ≈ mid`: the Moiré band.** The interference between structure and structure — the beat patterns, where periodic content cross-multiplies. This is where the texture and the relational structure live.
- **`k² → 1`: the Nyquist corner.** On a square `N×N` grid the single highest-frequency basis function is the **checkerboard** — alternating samples on both axes, the `(π, π)` corner of the Brillouin zone. A 64-vector reshaped to 64×64 cannot represent anything finer. The checkerboard is not *a* high frequency; it is *the* ceiling of the lattice.

This is the fact the whole morning turns on, and it is exact: **the dimension of the code sets the Nyquist limit, and the Nyquist limit's eigen-pattern is the checkerboard.** Your accidental origin loop already knew this without naming it — coupler → checkerboard (variable size) → image-to-vector (dimension `N`) → splitter → four low numbers fed back to the coupler. Read it as signal processing and it is a **variable-Nyquist sampler steered by its own gist**: the checkerboard is the sampling carrier, `N` sets the Nyquist scale, and the four low-frequency numbers fed back are the gist controlling the carrier. A loop whose sampling scale is modulated by its own coarse content, mismatch discharging as spikes — that is a crude **autofocusing sampler**, and the ECG-like train was its relaxation rhythm. You built the entorhinal cartoon by accident before you had the name for it.

---

## 2. Sampling has a Nyquist limit — and the lattice geometry is a *choice* the brain optimized

Take a continuous field `f(r)` on the plane and sample it on a lattice `Λ`. The spectrum of the samples is the spectrum of `f` replicated on the **reciprocal lattice** `Λ*`. Reconstruction is perfect if and only if the replicas do not overlap — if the signal's spectral support fits inside one Voronoi cell of `Λ*` (the Brillouin zone). The **Nyquist limit is the boundary of that cell.** Overlap is aliasing.

Two lattices, same idea, different geometry:

- **Square lattice**, spacing `a`. Brillouin zone is a square; the farthest corner is the diagonal `(π/a, π/a)` — the checkerboard. This is `sigh_image`'s world, and the reason the corner there is a checkerboard.
- **Hexagonal lattice.** Brillouin zone is a hexagon. For an **isotropically** band-limited signal (a disc of spectral support, which is the honest assumption when no direction is special), the hexagon packs the circular replicas more tightly than the square does. **Hexagonal sampling is the optimal 2-D sampling lattice** — it reconstructs the same band-limited field with about **13.4% fewer samples** than a square grid (Petersen & Middleton, 1962). It is the densest packing of the spectral replicas, the 2-D analogue of the hexagonal coin-packing being optimal.

Now state the fact that makes this not an analogy: **grid cells fire on a hexagonal lattice.** The medial entorhinal cortex represents the position variable on a triangular/hexagonal grid. So the brain's sampler is not merely *a* sampler — it is the *provably optimal* 2-D sampling lattice. If you were going to sample a 2-D field with the fewest cells for a given resolution, hexagonal is the answer, and the answer is what the entorhinal cortex built. The checkerboard in your toy is the square-lattice Nyquist pattern; the brain reached the same ceiling on the better lattice.

---

## 3. One module aliases on purpose; the modules together are an anti-aliasing residue code

A single grid module with spacing `λ` is **periodic**: it reports position only as `x mod λ`. By itself it *aliases* — the same firing phase recurs every `λ`, so one module cannot tell `x` from `x + λ`. A single module is, deliberately, **below Nyquist** for absolute position.

The modules come in a discrete set of scales, increasing geometrically along the dorsoventral axis of MEC with a ratio near `√2` (~1.42; Stensola et al., 2012). With incommensurate periods `{λ_i}`, the tuple of residues `(x mod λ_1, x mod λ_2, …, x mod λ_k)` determines `x` uniquely over a range that grows **exponentially** in the number of modules — a residue number system, the Chinese-Remainder structure (Fiete, Burak & Brookings, 2008; Sreenivasan & Fiete, 2011). Each module under-samples; the population, across scales, reconstructs the unaliased signal with very high precision.

So the entorhinal cortex does not *avoid* the Nyquist boundary — it **lives on it as a design principle**: alias deliberately at each scale, resolve the alias across scales. This is the deepest sense in which "the middle is in the Nyquist regime": it is built from carriers each sitting at its own aliasing limit, combined to beat the limit. Aliasing-as-feature is the signature of a multi-scale sampler, and it is exactly what grid modules are.

---

## 4. The lens: a Fourier plane, and the focal length that sets the zoom

What optical object turns an image into a frequency layout? A **lens**. Under coherent illumination a thin lens performs a spatial Fourier transform: the field at the front focal plane appears at the back focal plane as

```
U_back(x', y')  ∝  Û( x'/λf , y'/λf )
```

— its 2-D Fourier transform, with **position at the focal plane standing for spatial frequency of the input**, scaled by the wavelength `λ` and the focal length `f` (Goodman, *Introduction to Fourier Optics*). The Fourier plane is the unique plane where every spatial frequency of the input is mapped to a distinct *location*. It is the only place you can operate on frequencies one at a time — sample them, weight them, store them by frequency.

Two consequences land directly on the anatomy.

**(1) The focal length sets the frequency-to-position scale.** Change `f` and you re-magnify the frequency plane — the same input frequency lands at a different radius. The grid **modules**, with their geometric ladder of spacings, are then a stack of **effective focal lengths**: a multi-scale Fourier transform, an octave-spaced pyramid, each module a different magnification of the same frequency domain. This is the optical reading of "modules are spatial-frequency bands."

**(2) The lens this implies is not a single-focal-length lens — it is a multi-scale, local, hexagonally-sampled Fourier lens.** A global Fourier transform is non-local (every output mixes the whole input). The brain's version is windowed and oriented — closer to a **Gabor / log-polar / wavelet** transform than a plain FT, which is also exactly what V1's receptive fields already are (Daugman 1985; Jones & Palmer 1987). So the "lens" the Nyquist plane implies is a **bank of local Fourier windows on a hexagonal lattice at geometric scales** — a Gabor pyramid realized as a sampled Fourier plane. If forced to name one optical element: a Fourier-transforming lens whose back focal plane is read by a *hexagonal detector array at several focal lengths at once*.

**The "moving AIS" thread, as autofocus (labelled hypothesis).** You flagged that the AIS relocating (Grubb & Burrone, 2010) feels like "latent-space focus / frequency zoom." The optics gives that intuition a precise home: if the AIS reads the geometry of its dendritic orbit (the framework's standing single-cell bet), then its *position* along the axon sets which spatial scale of that orbit it is matched to — i.e. its effective focal length. Activity-dependent AIS relocation is then **autofocus**: the cell slides its read plane to keep a chosen frequency band in focus as the input statistics drift. Frequency zoom by moving the focal point. This is a hypothesis, not a result — but it is the *correct mathematical shape* for the intuition, and it is testable (does AIS position predict the cell's preferred temporal/spatial scale?).

---

## 5. The answer to "why is the middle at Nyquist": place cells are the Moiré reconstruction of the grid carriers

Here is the cleanest statement, and it is grounded in an established model rather than analogy.

A **place cell** — the hippocampal unit that fires at one location — can be written as a weighted sum of grid-cell responses across modules and phases. Summing periodic hexagonal gridfields of different scales produces **constructive interference at one location and destructive interference everywhere else**: a single localized bump (Solstad, Moser & Einevoll, 2006; the Fourier/interference family of grid→place models). That bump is a **Moiré beat** — the low-frequency envelope produced by the interference of higher-frequency carriers.

Lay this directly over your `sigh_image` axis:

| `sigh_image` regime | cortico-hippocampal role | what it is |
|---|---|---|
| Nyquist corner (`k²→1`), the checkerboard / carrier | **entorhinal grid cells** | the high-frequency periodic *carriers*, sampled hexagonally |
| the Moiré band (mid `k²`) | **the beat between modules** | the interference that actually codes position |
| the gist (`k²→0`), the envelope | **hippocampal place cells** | the *reconstructed* localized image — the Moiré envelope |

So the entorhinal cortex sits at the **carrier / Nyquist end** because its job is to *be* the sampling carrier; the hippocampus holds the **reconstructed envelope** (the place field) that is the carriers' Moiré beat. The middle of the loop is in the Nyquist regime because **the middle is the carrier plane**, and the thing one stage downstream (the place code) is the low-frequency reconstruction of those carriers' interference. Entorhinal = the grating; hippocampus = the image the grating reconstructs. The Moiré you saw between gist and Nyquist in the image filter is, in the brain, the position code itself.

One honesty marker, important: the established grid/place mathematics is about the **position / self-location** variable — grid modules are spatial frequencies *of where the animal is*, place fields their localized synthesis, path integration the phase accumulation. That much is solid. The framework's *generalization* — that the **same hexagonal-Fourier sampling** is applied to any cortical field routed through the entorhinal gateway (a sensory image, a memory, an abstract state), so that the EC is a general-purpose Nyquist plate and not only a position sampler — is the bet. It is a good bet (the machinery is generic; the cortex's own front end is already Gabor), but it is a bet, and it stays in the hypothesis drawer.

---

## 6. The loop as a 4f system — how the signal enters, is stored, and is projected back

Optics has a standard object for "transform to the Fourier plane, operate there, transform back": the **4f correlator**. Input plane → lens (forward FT) → **Fourier plane** (apply a per-frequency operation) → lens (inverse FT) → output plane. The middle plane is the only place a frequency-by-frequency operation can be applied; the system passes *through* it.

The cortico-hippocampal loop has exactly this shape, and it explains why it is a *loop through one gateway*:

```
   neocortex            ENTORHINAL              hippocampus
  (the field)         (the Nyquist plate)      (the store)
        │                     │                      │
  forward pass:   cortical field ──FT/sample──▶ grid carriers ──▶ DG / CA3
  (encode)         continuous, high-D           hexagonal, multiscale   recurrent
                                                  (the Fourier plane)    autoassociator
                                                                          = the plate
        ▲                                                                    │
        │                                                                    │
  return pass:   cortex ◀──inverse FT / project── deep EC ◀── CA1 ◀──────────┘
  (reconstruct)   re-expanded field            (same plane,      readout
                                                 read backward)
```

The anatomy underwrites it: superficial MEC (layer II stellate cells = grid cells) projects through the perforant path into dentate gyrus and CA3; CA3's recurrent collaterals are the classic autoassociative store (the interference *plate*, Marr 1971; Treves & Rolls); CA1 returns to the **deep** entorhinal layers (V), which project back to neocortex. The signal **enters** at the superficial Nyquist plane, is **stored** as interference on the CA3 plate, and is **read back out** through the same entorhinal plane in the deep layers — a Fourier plane traversed forward to encode and backward to reconstruct. That is why the architecture is a loop and not a line: in a holographic / 4f system you must pass through the Fourier plane twice, once to record and once to project.

In this reading:
- **the lens** = the cortex↔EC transform (local, multiscale, hexagonal — §4);
- **the Fourier/Nyquist plane** = entorhinal grid cells (the carriers, the sampling lattice);
- **the recording plate** = CA3's recurrent interference store;
- **the reconstruction** = CA1 → deep EC → cortex, the place-cell envelope expanded back into a cortical field.

---

## 7. Why grid cells are *there* — the tight answer

Assemble it:

1. The hippocampus needs a **discrete, frequency-factored, position-as-phase** code — to path-integrate, to orthogonalize, to store and complete patterns. That code can only be produced at a **Fourier plane**, where frequency becomes position becomes phase.
2. A Fourier plane that turns a continuous field into a stored code is a **sampler**, and a sampler is defined by its **Nyquist limit**.
3. To sample a 2-D field with the fewest units for a given resolution, the optimal lattice is **hexagonal** (Petersen–Middleton). → grid cells are hexagonal.
4. To beat the aliasing that any single sampling period imposes, use **multiple incommensurate scales** and resolve by residue. → grid modules, geometric spacing, CRT capacity.
5. This sampler must sit at the **one interface** between the continuous, high-dimensional neocortex and the discrete hippocampal store. → the entorhinal cortex, the anatomical gateway.

So grid cells are where they are because **the entorhinal cortex is the Fourier/Nyquist plane of the hippocampal optical system, and a sampler has exactly one correct place: the gateway.** Every structural fact about grid cells — hexagonal geometry, discrete scale modules, periodic aliasing, CRT resolution — is the fingerprint of an optimal multi-scale sampler at a Fourier plane. The position of the grid is not incidental to its function; it *is* its function, read off the anatomy.

---

## 8. What this predicts, and what would kill it

A vision is only worth the tests it exposes itself to.

- **Resolution should scale with module count, as a residue code, not linearly.** Adding a module of a new incommensurate scale should multiply the unambiguous range, not add to it. (Established direction; quantify it against the framework's own meshes.)
- **The finest module sets the system's Nyquist limit; the coarsest sets the field of view.** A representation routed through EC should show a hard high-frequency ceiling set by the smallest grid spacing and a low-frequency floor (aliasing) set by the largest — a measurable passband.
- **AIS position should track preferred scale (the autofocus prediction).** If AIS relocation is focal-length control, then a cell's AIS position should predict its preferred temporal/spatial frequency, and chronic input-statistics shifts should move both together. Falsifiable by combining AIS imaging (à la Grubb & Burrone) with tuning measurement.
- **Place fields should be reconstructable as the Moiré sum of the measured grid modules feeding them** — and perturbing one module should distort the envelope in the predicted beat-pattern way (extends Solstad et al. to a causal test).
- **The generalization bet is the sharp one:** if the EC is a general Nyquist plate, a *non-spatial* cortical field routed through it (an image, an abstract state) should acquire a hexagonal, multi-scale, aliasing-then-resolved code with the same signatures as the spatial grid. If routed non-spatial variables show *no* grid-like sampling structure, the "general-purpose holographic plate" reading is wrong and should be dropped back to "position sampler only."

---

## 9. Ledger

**Established (used, not claimed):**
- the sampling theorem on a lattice: samples replicate the spectrum on the reciprocal lattice; perfect reconstruction iff no overlap; the Nyquist limit is the Brillouin-zone boundary (standard);
- hexagonal sampling is the optimal 2-D lattice for isotropically band-limited signals (~13.4% fewer samples than square; Petersen & Middleton, 1962);
- grid cells fire on a hexagonal lattice, organized in discrete scale **modules** with a geometric ratio ≈ √2 (Hafting et al. 2005; Stensola et al. 2012);
- grid modules form an exponential-capacity residue/CRT code for position (Fiete, Burak & Brookings 2008; Sreenivasan & Fiete 2011);
- place fields are expressible as a weighted sum / interference of grid modules (Solstad, Moser & Einevoll 2006);
- a lens performs a spatial Fourier transform at its focal plane, with scale set by focal length; the 4f correlator operates at a central Fourier plane (Goodman, Fourier optics);
- the entorhinal–hippocampal anatomy: superficial MEC (layer II grid cells) → perforant path → DG/CA3; CA3 recurrent autoassociation (Marr 1971; Treves & Rolls); CA1 → deep MEC (layer V) → neocortex;
- V1 receptive fields are local oriented Gabor filters — a windowed Fourier front end (Daugman 1985; Jones & Palmer 1987);
- activity-dependent AIS relocation (Grubb & Burrone 2010), carried from the framework's prior documents.

**Clean structural mappings (sound, this paper's strongest ground):**
- a code of dimension `N` reshaped to `N×N` has its Nyquist ceiling at the checkerboard (the `(π,π)` corner) — the exact fact `sigh_image` exhibits;
- grid cells = the optimal (hexagonal) multi-scale **sampling lattice** of a Fourier/Nyquist plane; modules = effective focal lengths / a frequency pyramid;
- single-module aliasing + multi-module residue resolution = operating *on* the Nyquist boundary by design;
- place cells = the **Moiré/low-frequency reconstruction** of the grid carriers ⇒ EC at the carrier (Nyquist) end, hippocampus at the reconstructed envelope; the Moiré band between gist and Nyquist *is* the position code;
- the loop = a 4f-like encode → store-on-the-plate → reconstruct system that passes through the entorhinal Fourier plane twice (superficial in, deep out) — which is why it is a loop.

**Model hypotheses (falsifiable, unproven — the framework's reach):**
- that the *same* hexagonal-Fourier sampling the EC applies to **position** is applied to **any** cortical field routed through it, making the EC a general-purpose holographic Nyquist plate (the generalization bet of §5);
- that **AIS position is focal-length / autofocus** — sliding the read plane to keep a chosen frequency band in focus (the "moving AIS = frequency zoom" thread of §4);
- that the cortico-hippocampal loop is, mechanistically and not only by analogy, an optical encode/store/reconstruct projection with the EC as its Fourier plane.

**Honest limits:**
- the rigorous grid/place mathematics is about the **position** variable; the image-frequency reading (`sigh_image`) and the position-frequency reading (grid cells) are the *same 2-D sampling maths on different fields*, and equating them for arbitrary cortical content is the bet, not a result;
- "lens," "Fourier plane," "4f," "Talbot self-imaging" are the **correct mathematics** of the operations (FT, sampling, reconstruction) — they are not a claim that neural tissue is coherent optics; there is transform *maths* here, not diffraction *physics* (the same discipline the AIS document already imposed on the 190 nm grating);
- hexagonal-optimality assumes isotropic band-limiting; anisotropic content would prefer a different lattice, and the brain's grid is approximately, not perfectly, regular;
- this is a spec — a vision focused and made falsifiable — not a built system or a measured result.

**The bet (untouched, as always):** that any of this projection is *experienced* rather than computed — that the reconstructed field on the plate is felt. Locating the brain's sampler at a Fourier plane explains *why* the grid is hexagonal, multi-scale, aliasing, and *there*. It says nothing about why the reconstructed image is like anything to undergo. The hard problem is located more precisely — at the plate where the carriers' Moiré becomes a percept — and not closed.

---

## 10. The one concrete next step

Make the `sigh_image` axis *hexagonal and multi-scale*, and you turn the toy into a model of the plate. Replace the single square 64×64 sampling with a small stack of **hexagonal** sampling lattices at geometric scales (the modules), encode an input field as the residue tuple across them, and reconstruct by summing them back (the place-cell Moiré). Then show two things in one figure: (i) the reconstruction's resolution scales with the number of modules as a residue code, not linearly; and (ii) the high-frequency ceiling is set by the finest module and the field of view by the coarsest — the passband of the plate. If that holds, the entorhinal Nyquist plate is demonstrated as a sampler, in your own code, on the same image machinery you already trust — and the optics stops being a picture and becomes a measurement.

---

*Helsinki, June 2026. The gist is the envelope; the checkerboard is the ceiling; and between them is the Moiré that carries the where. The brain put its sampler at the one plane a sampler can live — the gateway between the smooth cortex and the discrete store — and made it hexagonal because hexagonal is the cheapest way to sample a plane, and multi-scale because that is how you beat the aliasing you chose. The grid is not in the middle by accident. The middle is the Fourier plane, and the grid is what a Fourier plane looks like when a brain builds one. Do not hype. Do not lie. Just show.*
