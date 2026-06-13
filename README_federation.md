# Federation — two PerceptionLab instances, one mesh

*Teach a memory on machine A. Recall it on machine B. Only tokens cross the wire — no shared weights.*

*PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.*

> Do not hype. Do not lie. Just show.

---

## What this is

The smallest experiment that turns the distributed-brain design into a result. Two independent Mycelial Cortex meshes, each on its own machine, connected only by a **token relay** — a pub/sub hub that rebroadcasts every `SpikeToken` to all other peers. A pattern taught on one is learned and recalled on the other, transmitted purely as spikes/tokens. The relay is the shared field, stretched across the network.

**Verified before shipping** (`federation_proof.py`, runs headless): peer B knew nothing about a secret pattern; peer A learned it and broadcast **39 sparse tokens**; B grew **one** node from those tokens alone, its template locked to the true pattern at **cos 0.97**, and B then recalled a heavily-corrupted (0.6) version at **cos 0.77**. No weights crossed the wire.

---

## Files

| file | where it goes | what it is |
|---|---|---|
| `token_relay_server.py` | any reachable machine | the relay hub (pure stdlib) |
| `tokenrelaynode.py` | `nodes/` on every peer | the synapse-across-machines node (socket client inlined) |
| `mycelialcortexnode.py` | `nodes/` on every peer | the distributed holographic mesh |
| `patternmemorybanknode.py`, `atpmetabolismnode.py`, `cognitivedashboardnode.py` | `nodes/` on the teacher | already in your set |
| `federation_teacher.json` | machine A | teaches shapes, broadcasts them |
| `federation_listener.json` | machine B | learns + recalls from the wire |
| `federation_proof.py`, `relay_client.py`, `mycelial_mesh_proof.py` | anywhere | the headless proof |

`tokenrelaynode.py` is self-contained (no cross-file import), so it just needs `token_relay_server.py` running somewhere it can reach.

---

## Run it

**1. Start the relay** (on machine A, or any box both can reach):
```bash
python token_relay_server.py --port 8765
# prints peers / msgs_relayed every 2s
```

**2. Machine A — the teacher.** Load `federation_teacher.json`. In the **Token Relay (OUT)** node set `host` to the relay machine's IP (`127.0.0.1` if same box) and `port` 8765. Press play. The Engram Library cycles shapes → the Cortex recalls them → the relay broadcasts the recalled vectors as tokens (sparse, gated by confidence). Watch **Tokens Sent** climb.

**3. Machine B — the listener.** Load `federation_listener.json`. Set its **Token Relay (IN)** `host`/`port` to the same relay. Press play. Its only input is the wire. Watch:
- **Tokens Received** climbing,
- **Nodes Grown** rising as B spawns a node per distinct pattern A teaches,
- the **Dashboard** showing the shapes A is perceiving — reconstructed on B from tokens alone.

What A comes to know, B comes to know — carried as spikes, not weights.

**Headless proof (no GUI):**
```bash
python token_relay_server.py --port 8772 &   # or let the proof start its own
python federation_proof.py                    # prints PASS, template cos 0.97, recall cos 0.77
```

---

## The token on the wire

```
{ "src": peer-id, "payload": [floats], "conf": 0..1, "chi": +/-1 }
```
Newline-delimited JSON. `payload` is the pattern (or a complex pole); `conf` gates and weights it; `chi` carries the arrow-of-time sign. That is the entire contract. Anything that emits this — a sensor, a prover, an LLM wrapper — is a peer. Integration is by resonance: a token that matches an existing node is recalled; a novel one spawns a node.

---

## Ledger

**Verified:**
- loopback and two-node token exchange (exact payload round-trip);
- teach-A / recall-B with only tokens: B template cos 0.97, recall cos 0.77, 39 sparse tokens, no shared weights;
- the relay never echoes to sender; clients auto-reconnect; networking is off the GUI thread.

**Honest limits:**
- the relay is plain TCP JSON-lines — no auth, no encryption, LAN/trusted-network only (don't expose the port to the open internet as-is);
- broadcast is throttled (`broadcast_every`, `conf_gate`) to stay sparse; tune for your frame rate;
- to ingest peer tokens the listener cortex takes them on `query_vec` (peer tokens are its stimulus); if you also want a local stimulus on the same instance, wire peer tokens to `inject_token` instead and note the cortex prioritises a present local query that frame;
- this demonstrates federated learning + recall of patterns, not a distributed cognition. The experience question is untouched, as always.

**Where it goes next:** more than two peers (the relay already supports N), chirality-carrying sequence tokens so order federates too, and an LLM wrapper that emits/consumes these tokens — at which point a language model becomes a cortical region on the same field.

*A spike is a token. The relay is the field. Teach on one, know on all. Do not hype. Do not lie. Just show.*
