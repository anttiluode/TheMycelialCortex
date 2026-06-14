# The Local Tilt — making *which way* real

## Addendum to The Priming Tide: the applied skew operator, gated by the tide

*PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.*

> Do not hype. Do not lie. Just show.

---

## What the screenshots showed, and what they didn't

The Priming Tide loop ran and reproduced the result: identical corrupted input, recall expressed only on the high tide (tide 0.16 → conf 0.00, blank recall; tide 0.80 → conf 1.00, a clean recovered shape). That is the *whether*, working.

But the arrow barely moved — `+0.000` on the low tide, `+0.001` on the high. That is honest and it is the point: the Primed Cortex could resonate or not, but its recall was a **symmetric gradient settle** — it falls into a basin and stops. Nothing drove a current, so there was no direction to read. The tide gave the water. It did not give the tilt.

This version adds the tilt.

---

## The three roles, now all in code

- **tide** — slow scalar, the chemical primer — *whether* it can resonate. (β and the expression gate.)
- **content** — the stored patterns `P_k`, the islands — *what* there is to recall. (The symmetric field, `W = Σ pₖpₖᵀ`.)
- **tilt** — a fast, applied skew operator `A`, the ephaptic field — *which way* the recall runs.

The operator is not invented. Built cyclically over the cortex's own nodes, `A` is the antisymmetric transition connectivity of Sompolinsky & Kanter (1986) / Kleinfeld (1986) — the textbook sequence-memory operator, the same skew `A` the rotation-half document grounded. The only new move is to **apply** it as a drift term in the recall instead of merely reading it back off the winner traffic:

```
s ← norm( leak·s + content(w·P) + tilt · normalize(A·(P·s))·P )
                   \___ settle ___/   \________ steer ________/
```

The symmetric term settles the field into a basin — the gradient, curl-free, cheap half. The skew term adds a divergence-free **current** that pushes the descent from one basin toward its successor — the solenoidal half, the arrow, the part you pay to turn. That is the gradient/curl split of `the_unnatural_direction.md` made into a single line of the recall loop.

And the tilt is **gated by the tide**: `tilt_eff = tilt · tide`. No water, no steering — you cannot turn a boat stranded on dry rock. *Whether* gates *which way*. Flip the tilt sign and the recall walks the cycle the other way; the winner-traffic arrow flips with it (forward vs reverse replay — Foster & Wilson 2006).

---

## What the loop shows

Let it warm up until all the patterns have spawned as nodes. Then, on the **high tide**, the recall both expresses *and* walks the cycle in the tilt's direction, and the arrow goes strongly `+` or `−` — no longer pinned near zero. When the Ephaptic Tilt auto-reverses, the recall reverses and the **arrow flips sign**, live. On the **low tide**, everything freezes: no expression and no steering, because the tilt is gated by the tide. The three knobs are visibly separable: the tide turns the whole thing on, the content is what comes back, the tilt sets which way it goes.

---

## Ledger

**Clean structural identity (the strong claim):**
- the applied operator `A`, built cyclically over the stored patterns, is the Sompolinsky–Kanter / Kleinfeld antisymmetric sequence connectivity (1986). Using it as a drift term = sequence recall = a probability current = the arrow. Established mechanism, applied; not a new object.
- settle-plus-steer = the gradient (curl-free, cheap) plus solenoidal (curl, the arrow) decomposition — the same split already grounded in the rotation-half and unnatural-direction documents.

**Modeling choices (fair, labelled):**
- the tide gating the tilt (`tilt_eff = tilt · tide`) — "whether gates which way." Consistent with the conductance story (no resonance, no steering), but a modeling choice, not a measurement.
- the Ephaptic Tilt node supplies a signed **strength + chirality** only; the operator's *geometry* lives in the cortex's own patterns. A fast field sets amplitude and sign; the carved structure sets the shape.

**Honest limits:**
- the cyclic **order** is seeded from the node spawn order (= presentation order), not learned from STDP in this node. The learned-from-experience version is the transition memory `T` in `predictivecortexnode.py`; folding that in makes the order *earned* rather than configured — the obvious next step.
- costs and dynamics remain structural proxies in relative units, as everywhere in this line — not Joules, not nats.
- this is one mesh; whether the tilt (the direction) federates across peers is still the open federation question (`the_unnatural_direction.md`, build c).

**The bet (untouched):** that the biological ephaptic field *is* this applied `A`, and that any of it is experienced rather than processed. The tilt makes *which way* real in the engine. It does not make it real in tissue, and it does not touch the hard problem.

---

## The next two, after this

1. **Earn the order.** Replace the seeded cyclic `A` with the learned transition memory `T` from `predictivecortexnode.py`, so the direction the cortex steers is the direction it actually experienced — STDP writing `A`, not a config writing it.
2. **Local budgets.** Replace the single global ATP pool with per-region pools (local cerebral blood flow / neurovascular coupling) — many small breathing budgets instead of one global tide — so a hard-working island tires and yields the field while its neighbours stay primed.

*The tide is the water; the content is the islands; the tilt is the current that runs between them. Whether, what, which way — three knobs, three marks on the page, and now three lines in the loop. Do not hype. Do not lie. Just show.*
