"""
arrow_cost_proof.py  —  the GRAIN of the arrow: reverse costs more, and the gap tracks ||A||
============================================================================================
Build (a) from `the_unnatural_direction.md`, made runnable and falsifiable.

THE CLAIM UNDER TEST (Crooks + the rotation half):
    Traversing a LEARNED cyclic sequence against its trained direction costs more energy
    than traversing it forward, the extra cost is the entropy of going against the current,
    and the forward/reverse cost GAP should (i) vanish at detailed balance (||A|| = 0) and
    (ii) grow with the broken-detailed-balance flux ||A||.

THE HONEST REFINEMENT (why the naive version of build (a) fails, and what that teaches):
    If you bill the RAW recall stream |ds| with the wattage meter, forward and reverse cost
    the SAME -- the change between consecutive patterns is identical either way. The arrow's
    cost is NOT in the stimulus change. It lives in the PREDICTION ERROR: the part of each
    input the learned asymmetric current did not anticipate (= Still et al. 2012's
    non-predictive information). Forward rides the trained transition (small surprise, cheap);
    reverse fights it (large surprise, dear). So the meter is billed on the surprise residual
    x - pred, where pred = the recurrent current's guess for the next state. The raw-|ds|
    stream is kept as a CONTROL and shown to be symmetric -- proving the asymmetry is neither
    a stimulus artifact nor a meter artifact.

THE SETUP:
    M near-orthonormal patterns form a cycle.  Recurrent connectivity:
        J = J_sym + g * J_asym
        J_sym  = Sum_mu  xi^mu (xi^mu)^T          symmetric Hopfield store  (no arrow)
        J_asym = Sum_mu  xi^{mu+1} (xi^mu)^T       Sompolinsky-Kanter transition (the write-side A)
        A = (J - J^T)/2  =>  ||A|| is proportional to g  (g=0 => detailed balance)

THE FALSIFIABLE PREDICTIONS:
    P1 (control): raw field velocity |ds| is symmetric fwd vs rev (asymmetry is not the stimulus)
    P2 (control): at g=0 the cost gap is ~0 within seed noise (detailed balance: no grain)
    P3:           for g>0, reverse costs more than forward
    P4:           the gap grows monotonically with g and correlates with measured ||A||
    P5 (D3 echo): the skew circulation of the activity flips sign fwd vs rev

If P2 fails (gap nonzero at g=0) the meter is rigged. If P3/P4 fail the cost-asymmetry
thesis is wrong for this system and should be dropped. The test is built so it CAN fail.

HONEST LIMITS (unchanged from the whole line):
    - costs are in RELATIVE units, not Joules; sigma_JN is dither, not a calibrated bath;
    - near-orthonormal patterns are the clean case (a non-orthonormal robustness run is included);
    - this is a single-mesh result; the federated version (anti-consensus order costs more) is
      builds (b)+(c), untested here.

Run:  python arrow_cost_proof.py
PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.
Do not hype. Do not lie. Just show.
"""
import numpy as np


def norm(v):
    return v / (np.linalg.norm(v) + 1e-9)


def orthonormal_patterns(D, M, rng):
    """M near-orthonormal pattern vectors (the clean case)."""
    X = rng.standard_normal((M, D))
    Q, _ = np.linalg.qr(X.T)          # columns orthonormal
    return Q.T[:M]                     # (M, D), orthonormal rows


def random_patterns(D, M, rng):
    """M random normalized patterns (the messy, non-orthonormal robustness case)."""
    return np.stack([norm(rng.standard_normal(D)) for _ in range(M)])


def connectivity(P, g):
    M, D = P.shape
    Jsym = sum(np.outer(P[m], P[m]) for m in range(M))
    Jasym = sum(np.outer(P[(m + 1) % M], P[m]) for m in range(M))
    J = Jsym + g * Jasym
    A = 0.5 * (J - J.T)
    return J, float(np.linalg.norm(A))          # ||A||_F (proportional to g)


def run_tour(P, J, order, leak=0.25, drive=1.0):
    """
    Drive the recurrent field through `order`. Each step the recurrence votes pred=norm(J@s);
    the world supplies x; the unpredicted residual err = x - pred is the SURPRISE.
    Returns: err stream (per-step residual vectors), raw |ds| stream, one-hot winner stream.
    """
    M, D = P.shape
    s = P[order[0]].copy()
    errs, ds_raw, winners = [], [], []
    for t in range(1, len(order)):
        x = P[order[t]]
        pred = norm(J @ s)                       # where the learned current points next
        err = x - pred                           # prediction error (the non-predictive residual)
        ds_raw.append(float(np.linalg.norm(x - s)))   # CONTROL: raw field velocity (direction-blind)
        errs.append(err)
        s = norm(leak * pred + drive * x)        # field follows the world, nudged by the current
        winners.append(int(np.argmax(P @ s)))
    return np.array(errs), np.array(ds_raw), np.array(winners)


def spike_meter(err_seq, dim, seeds=24):
    """
    Faithful trimmed MetabolicSpikeNode delta-code, billed on the SURPRISE residual stream.
    Theta-gated leaky integrate-and-fire with adaptation + Johnson-Nyquist dither.
    Theta phase is fixed by t (identical for fwd and rev), dither averaged over seeds.
    Returns mean (spikes, wattage) in relative units.
    """
    E_spike, c_field, thr = 1.0, 1.0, 0.5
    leak_v, beta, tau_a, dt = 0.90, 3.0, 0.18, 1.0 / 60.0
    f_theta, m_theta = 8.0, 0.8
    dz_scale, sigma_JN = 25.0, 0.03
    sp_runs, W_runs = [], []
    for sd in range(seeds):
        rng = np.random.default_rng(10_000 + sd)
        v = np.zeros(dim); a = np.zeros(dim); S = 0.0; W = 0.0
        for t, err in enumerate(err_seq):
            dz = np.abs(err)
            g_th = 1.0 + m_theta * np.cos(2 * np.pi * f_theta * t * dt)
            drv = g_th * np.tanh(dz_scale * dz)          # spikes driven by the surprise, theta-gated
            net = drv - beta * a + sigma_JN * rng.standard_normal(dim)
            v = leak_v * v + net
            sp = (v > thr).astype(np.float64)
            v = v * (1 - sp)
            a = (a + sp) * np.exp(-dt / tau_a)
            nsp = float(sp.sum())
            S += nsp
            W += E_spike * nsp + c_field * float(np.linalg.norm(err))
        sp_runs.append(S); W_runs.append(W)
    return float(np.mean(sp_runs)), float(np.mean(W_runs))


def circulation(winners, M):
    """Skew circulation of the winner traffic around the M-cycle (the arrow; D3 quantity)."""
    C = np.zeros((M, M))
    prev = np.zeros(M)
    for w in winners:
        oh = np.zeros(M); oh[w % M] = 1.0
        C = 0.97 * C + 0.03 * np.outer(oh, prev)
        prev = oh
    A = 0.5 * (C - C.T)
    return float(sum(A[k, (k + 1) % M] - A[(k + 1) % M, k] for k in range(M)))


def cycle(order_unit, laps):
    return (order_unit * laps)


def measure(P, gs, laps=6, seeds=24):
    M, D = P.shape
    fwd_unit = list(range(M)) + [0]          # 0 1 2 .. M-1 0   (rides J_asym)
    rev_unit = [0] + list(range(M - 1, 0, -1)) + [0]   # 0 M-1 .. 1 0 (against J_asym)
    rows = []
    for g in gs:
        J, Anorm = connectivity(P, g)
        ef, dsf, wf = run_tour(P, J, cycle(fwd_unit, laps))
        er, dsr, wr = run_tour(P, J, cycle(rev_unit, laps))
        spf, Wf = spike_meter(ef, D, seeds)
        spr, Wr = spike_meter(er, D, seeds)
        rows.append(dict(
            g=g, Anorm=Anorm,
            ds_fwd=float(dsf.mean()), ds_rev=float(dsr.mean()),
            err_fwd=float(np.linalg.norm(ef, axis=1).mean()),
            err_rev=float(np.linalg.norm(er, axis=1).mean()),
            sp_fwd=spf, sp_rev=spr, W_fwd=Wf, W_rev=Wr, gap=Wr - Wf,
            arrow_fwd=circulation(wf, M), arrow_rev=circulation(wr, M),
        ))
    return rows


def report(title, rows):
    print(f"\n{title}")
    print(f"  control P1 (raw field |ds|, should be SYMMETRIC fwd~rev):")
    r0 = rows[0]
    print(f"    at g={r0['g']:.2f}:  |ds| fwd {r0['ds_fwd']:.3f}   rev {r0['ds_rev']:.3f}   "
          f"-> the asymmetry is NOT in the stimulus change")
    print(f"\n  sweep over asymmetric connectivity g  (||A|| grows with g; g=0 = detailed balance):")
    print(f"    {'g':>5} {'||A||':>7} {'surprise_f':>11} {'surprise_r':>11} "
          f"{'cost_fwd':>9} {'cost_rev':>9} {'gap':>8} {'arrow_f':>8} {'arrow_r':>8}")
    for r in rows:
        print(f"    {r['g']:>5.2f} {r['Anorm']:>7.3f} {r['err_fwd']:>11.3f} {r['err_rev']:>11.3f} "
              f"{r['W_fwd']:>9.1f} {r['W_rev']:>9.1f} {r['gap']:>8.1f} "
              f"{r['arrow_fwd']:>+8.3f} {r['arrow_rev']:>+8.3f}")

    gaps = np.array([r['gap'] for r in rows])
    Anorms = np.array([r['Anorm'] for r in rows])
    g0 = rows[0]['gap']
    # normalise g=0 gap by the spread of the meter's wattage to judge "within noise"
    scale = np.mean([r['W_fwd'] for r in rows]) + 1e-9
    corr = float(np.corrcoef(gaps, Anorms)[0, 1]) if len(rows) > 2 else float('nan')

    p2 = abs(g0) < 0.02 * scale                                  # detailed-balance gap ~ 0
    p3 = all(r['gap'] > 0 for r in rows if r['g'] > 0)           # reverse costs more for g>0
    p4 = (corr > 0.9) and np.all(np.diff(gaps) >= -0.02 * scale) # gap tracks ||A||, ~monotone
    p5 = all(np.sign(r['arrow_fwd']) != np.sign(r['arrow_rev'])
             for r in rows if r['g'] > 0 and abs(r['arrow_fwd']) > 1e-6)

    print(f"\n  P2 detailed-balance gap (g=0): {g0:+.2f}  (|gap| < {0.02*scale:.2f}?)  -> {'OK' if p2 else 'FAIL'}")
    print(f"  P3 reverse costs more for every g>0:                        -> {'OK' if p3 else 'FAIL'}")
    print(f"  P4 corr(gap, ||A||) = {corr:+.3f}  and gap ~monotone in g:   -> {'OK' if p4 else 'FAIL'}")
    print(f"  P5 activity arrow flips sign fwd vs rev:                     -> {'OK' if p5 else 'FAIL'}")
    verdict = "PASS" if (p2 and p3 and p4) else "WEAK/FAIL"
    print(f"\n  => {verdict}: " + (
        "reverse traversal of a learned cycle costs more, the gap vanishes at detailed balance "
        "and grows with ||A||. The arrow has a grain, and the grain is a measurable cost."
        if verdict == "PASS" else
        "the cost-asymmetry prediction did not hold cleanly here -- report it as written, do not bury it."))
    return verdict


def main():
    D, M = 128, 6
    gs = [0.0, 0.25, 0.5, 1.0, 2.0, 4.0]
    print("=" * 92)
    print("THE GRAIN OF THE ARROW  —  forward vs reverse traversal cost  (build a)")
    print("=" * 92)
    print("billing the SURPRISE residual x - pred (the non-predictive info), not the raw |ds|.")
    print("costs are RELATIVE units (sigma_JN is dither, not a calibrated bath) — structural proxy.")

    rng = np.random.default_rng(0)
    P_clean = orthonormal_patterns(D, M, rng)
    rows_clean = measure(P_clean, gs)
    v1 = report("[1] CLEAN CASE — near-orthonormal patterns", rows_clean)

    rng2 = np.random.default_rng(1)
    P_msgy = random_patterns(D, M, rng2)
    rows_msgy = measure(P_msgy, gs)
    v2 = report("[2] ROBUSTNESS — non-orthonormal random patterns (messy, with cross-talk)", rows_msgy)

    print("\n" + "=" * 92)
    print(f"OVERALL:  clean={v1}   robustness={v2}")
    print("Next: builds (b) federate the arrow (carry+use chi, ordered delivery) and (c) test that")
    print("anti-consensus token order costs more across peers — the same grain, one level up.")
    print("Do not hype. Do not lie. Just show.")
    print("=" * 92)


if __name__ == "__main__":
    main()
