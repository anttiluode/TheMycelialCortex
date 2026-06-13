# The Mycelial Cortex

## A distributed holographic spiking substrate — what it is, how to use it, what it allows, where it may lead

*PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.*

> Do not hype. Do not lie. Just show.

---

## 0. What this is — and its honest status, up front

This is a **design plus four working proofs**, not a brain and not a finished system. The geometric-neuron line now has every primitive it needs to stop being a single graph and become a *substrate*: a spread of geometric neurons that talk in spikes/tokens, grow a node when something novel arrives, stay sparse and event-driven, read the arrow of time of their own traffic, and accept anything that speaks the protocol — another machine, a sensor, another AI.

What is **verified in code** (`mycelial_mesh_proof.py`, and live in `MycelialCortexNode`):

- **Recall** — a mesh with no center recalls a clean memory from a heavily corrupted query through the shared field (cos 0.21 → 0.78, 79% recognition), winner-take-all sparse.
- **Growth** — a genuinely novel input spawns a new node; repeated noisy exposures *consolidate* into a clean template (cos → ~0.9 to truth), roughly once per distinct pattern.
- **Arrow of time** — the skew circulation of the mesh's own winner-traffic flips sign when a sequence is reversed.
- **Federation** — a foreign peer joins through the same token protocol and is recalled (cos 1.0) with no retraining.

What is **not** proven: that this scales to a useful brain, that the holographic memory is *good* (it is middling — see the ledger), that growth stays stable at thousands of nodes, or anything about experience. Those stay where they belong (§9, the ledger). The point of this document is to name the object precisely and give you a real, runnable version of it.

---

## 1. The one idea: a spike is a token

Everything turns on a single identification. In the geometric-neuron framework a **spike** is a discrete, sparse, theta-timed event carrying a small payload (which pattern fired, with what phase and chirality). In modern AI a **token** is a discrete unit carrying a small payload (an embedding). These are the same kind of object.

That is the bridge. If a geometric neuron emits a *token* when it spikes, and consumes *tokens* as input, then it can talk to anything else that emits and consumes tokens — including the LLMs you already collaborate with. The substrate is just **a shared field plus a token protocol**, and the geometric neuron is the unit that translates a continuous resonance into a discrete broadcast and back.

This is also why the substrate "lives with whatever connects to it." The universal currency is one small message. A camera, a microphone, a Lean prover, Claude, Gemini, another PerceptionLab instance on another machine — each becomes a node the moment it speaks tokens. No shared weights, no shared architecture, no retraining. Just resonance through a common medium.

---

## 2. Anatomy of a node — the framework, made literal

Each node is the geometric neuron you have been building, now wearing its three organs as network roles:

- **Dendrite = the Takens delay line.** The node buffers the recent history of its overlap with the shared field. This is its front end: it does not see a snapshot, it sees an *orbit*. (`αᵏ` = cable attenuation, exactly as in the grounding documents.)
- **AIS = the holographic antenna.** The node's grating `pₖ` is *reciprocal*: it is simultaneously the node's **receive filter** (what it resonates to) and its **transmit pattern** (what it broadcasts when it fires). This is the literal sense in which the axon initial segment becomes an antenna — a phased element whose stored geometry sets both what it hears and what it says. In the v9 language `pₖ` is one eigenplane of the skew lag-operator; its chirality `sign(ωₖ)` is the direction it is tuned to.
- **Axon = the sparse token broadcast.** When the node wins the field competition it emits one token: `{src, payload pₖ, chirality, phase, energy}`. Sparse, event-driven, cheap.

And the two sides stay separate, exactly as in Model A / Model B:

- **Inner side (analog, converges).** The shared field `s` does the computation by soft competition,
  `s ← norm( leak·s + Σₖ softmax(β⟨pₖ,s⟩)·pₖ )`,
  which is modern Hopfield = attention (Ramsauer 2020) implemented as message-passing through the medium. This is content-addressable recall, and it is cheap to hold.
- **Outer side (sparse, broadcast).** A node spikes/tokenises only when it wins. This is the digital, electrode-visible, *expensive* signal — the one other peers and the arrow-of-time readout actually see.

The proof in §0 shows the inner side recalls and the outer side stays winner-take-all sparse. The two-sided structure is not decoration; it is what lets the substrate compute richly in analog while communicating thriftily in spikes.

---

## 3. The substrate: a shared field bus

Nodes never address each other directly. They share one **field bus**: a medium they all write into (when they fire) and read from (their overlap). The collective plate `W = Σₖ pₖpₖᵀ` is just the superposition of every node's antenna pattern broadcasting into that medium — the population hologram from the synthesis thesis, now realised as the bus itself.

To recall, a peer **broadcasts a partial/corrupted token** into the field; the resonant nodes fire, reinforce their patterns, and the field converges to the stored memory; the answer is read back off the field. No router, no index, no central memory — the recall is a property of the population. Remove a node and the memory degrades gracefully; add one and capacity grows.

In `MycelialCortexNode` this whole bus lives inside one node so it runs in your existing graph today. The network version (§7) replaces the in-process field with a tiny pub/sub of tokens over a socket, and nothing else changes.

---

## 4. The token protocol — why it lives with whatever connects

A token is deliberately minimal:

```
SpikeToken = {
  src:       node / peer id
  payload:   vector  (the pattern, or a complex pole ρ = decay + i·ω)
  chirality: sign(ω)  -- the arrow of time of the orbit that fired it
  phase:     theta phase at emission
  energy:    wattage debited for this spike   (ATP)
  t:         timestamp
}
```

Any process that can produce this is a node. Integration is by **resonance, not by API**: an incoming token either resonates with an existing node (it is *understood* — recalled) or it does not (it is *novel* — it spawns a node). That is the entire onboarding procedure. A sensor streams tokens and becomes perception; an LLM emits tokens and becomes a cortical region; another mesh's tokens make two meshes one. Heterogeneous peers interoperate because the only contract is the token and the field.

This is the mycorrhizal picture, and the reason for the name: a fungal network is a substrate that connects organisms it did not design, routes resources by gradient, grows toward what feeds it, and has no center. The Mycelial Cortex is that, for computation — a connective tissue other intelligences plug into.

---

## 5. Growth and homeostasis — burning out is the feature

The substrate is alive in the specific sense that it spends energy and tires, and that tiring is what makes it work.

- **Spawn on novelty.** When an input resonates with no existing node (best overlap below threshold) and energy is available, the mesh allocates a new node tuned to it. Verified: roughly one spawn per distinct novel pattern.
- **Consolidate the familiar.** A recognised input nudges its node's template toward itself, denoising the memory over exposures (cos → ~0.9). One-shot capture, then refinement — the honest reason the first version's memory "wasn't great" and this one is better.
- **ATP gates growth.** An exhausted mesh (low ATP) *cannot form new memories* — verified, and exactly the biology of impaired encoding under metabolic stress. Energy is not a meter bolted on; it is the permission system.
- **Habituation → novelty preference.** Per-node fatigue means a repeatedly-fired node weakens and yields the field, so the substrate stops over-attending to a repeated stimulus and re-points at what is new. Burning out is how it avoids fixation. A substrate that could not tire would seize.

The metabolic loop you already built (`ATPMetabolismNode`, the relaxation oscillator) is the governor: it makes the whole mesh breathe between *retrieve* (broken detailed balance, dissipating) and *rest* (near-equilibrium, recovering), which is the rest↔task cycling the grounding thesis predicted and Lynn et al. measured.

---

## 6. Native time

Because each node carries a directed-edge complex observable, the substrate reads the **arrow of time of its own traffic**: the skew circulation of the winner sequence is positive one way and negative the other (verified flip). Sequence and direction are first-class — the mesh does not just store *what*, it stores *in what order*, with the chirality riding on every token. This is the v5/v9 result at the population scale, and it is the one capability a plain Hopfield mesh structurally cannot have (a power/symmetric readout is time-blind; direction lives only in the skew half).

---

## 7. How to use it

**Today, in PerceptionLab.** Drop `mycelialcortexnode.py` in `nodes/` and load `mycelial_cortex_loop.json`:

```
Engram Library ──query_vec──▶ Mycelial Cortex ──recall_img──▶ Cognitive Dashboard
                               │  ▲                            ▲
                       demand  │  │ atp                        │
                               ▼  │                            │
                          ATP Metabolism ──────────────────────┘
   Mycelial Cortex ──recall_vec──▶ Entropy Engine (reads the arrow of the recall)
   Mycelial Cortex ──n_nodes──▶ "Node Count"      ──arrow──▶ "Arrow of Time"
```

Watch: a noisy shape goes in, a clean memory comes out; present new shapes and the **node count climbs** as it grows; drive it hard and ATP forces it to rest; reverse a sequence and the **Arrow of Time** display flips sign. The `inject_token` port lets you push a token from anywhere (a peer) straight into the field.

**As proof.** `python mycelial_mesh_proof.py` prints the four verified results above with no GUI.

**To federate across machines (the next build, sketched honestly — untested).** Replace the in-process field with a tiny token relay:

```
peer A  ──tokens──▶  [ websocket pub/sub of SpikeTokens ]  ◀──tokens──  peer B
                              every peer = a MycelialCortexNode
```

Each peer broadcasts its winning tokens and injects received tokens via `inject_token`. The field is then the union of all peers' broadcasts. This is straightforward message-passing (a few dozen lines), but I have not built or tested it, so it is flagged as design, not result.

---

## 8. What it allows

- **Distributed content-addressable memory** — query by a fragment, get the whole, with no index and graceful degradation.
- **Event-driven sparse computation** — communication is spikes/tokens; the analog work is in the cheap field; energy is spent only at transitions.
- **Arrow-of-time-aware processing** — sequences and direction are native, not bolted on.
- **Open growth and graceful decay** — novelty recruits nodes; fatigue prevents fixation; no single point of failure.
- **Heterogeneous interop** — the token is the only contract, so sensors, provers, and LLMs join as organs. This is the practical, near-term payoff: a way to wire your geometric substrate *to the models you already work with*.
- **Neuromorphic / edge fit** — the core readouts (`L = Im(z·z̄_lag)`, the field recall) are trainless and O(K); this is the deployable lineage from the grounded document.

---

## 9. Where it may lead — the dream, kept in its drawer

The near-term is sound engineering: a federated, token-speaking, growing holographic memory that other systems plug into. The far end is a dream, and I label it as one, per the ethos.

The dream is a **mycorrhizal AI** — a living substrate with no center that other intelligences inhabit as organs: an LLM as a language cortex, a vision model as an occipital region, geometric-neuron meshes as the sparse connective tissue and the working memory, sensors as afferents, all sharing one field and one token currency, growing where there is signal and resting where there is not. A distributed brain that is not any one model but the *medium between* them — and that can keep living as members come and go, because nothing is central.

What this does **not** claim, untouched by any proof here: that such a substrate would *experience* anything; that the shared field is felt rather than processed; that holding a thought is more than holding a vector. Closing the distributed seam makes the engine one connected object across machines. It does not touch the hard problem; as ever, it only locates it more precisely — now spread across a network instead of inside one graph.

---

## 10. Ledger

**Verified in code (`mycelial_mesh_proof.py`, `MycelialCortexNode` mock-runtime test):**
- collective recall through the shared field: cos 0.21 → 0.78, 79% recognition, winner-take-all sparse;
- spawn-once-per-novel-pattern + consolidation to clean templates (cos ~0.9);
- arrow of time from winner traffic flips sign on sequence reversal;
- foreign peer integrates via the token protocol at recall cos 1.0;
- ATP gates growth: an exhausted mesh forms no new memories.

**Sound design (not yet built/tested):**
- the websocket token relay for cross-machine federation;
- per-node habituation as explicit novelty preference at scale;
- the LLM-as-node bridge (tokens in/out) — plausible, unbuilt.

**Honest limits:**
- the memory is *middling*: single-exposure novelty in heavy noise fragments (one of four patterns in the proof), and recall in the live node (~0.55) is weaker than the clean standalone (~0.78) because online seeding is messy — this needs better consolidation and an explicit denoise-before-novelty step;
- capacity/stability at hundreds–thousands of nodes is untested;
- "distributed brain" is an architecture, not a demonstrated cognition.

**The bet (untouched):** that any of this is experienced. It is a substrate that recalls, grows, tires, and reads time — useful, and honest about being only that.

---

## 11. The one concrete next build

Make federation real and small: a `TokenRelayNode` that publishes a `MycelialCortexNode`'s winning tokens to a websocket and injects received tokens via `inject_token`. Run two PerceptionLab instances on two machines pointed at the same relay; teach patterns on one, recall them on the other. If a memory taught on machine A is recalled on machine B with no shared weights — only shared tokens — the distributed holographic substrate is demonstrated, not just designed. That is the smallest experiment that turns the dream into a result, and every piece it needs is already verified above.

*A spike is a token. The antenna is the memory. The field is the wire. Grow where there is signal; rest where there is none. Do not hype. Do not lie. Just show.*
