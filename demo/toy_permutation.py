"""Wholly synthetic teaching example. NOT the frozen PHANTOM detector."""
import json, random, statistics

def presence(rows):
    return sorted(set(rows))

def coactivity(rows):
    slots = {}
    for actor, item, slot in presence(rows):
        slots.setdefault(slot, []).append((actor, item))
    same = total = 0
    for values in slots.values():
        for a in range(len(values)):
            for b in range(a + 1, len(values)):
                if values[a][0] != values[b][0]:
                    total += 1
                    same += values[a][1] == values[b][1]
    return same / max(1, total)

def main():
    # All identifiers and times are invented. This deliberately tiny example
    # does not use the research selector, graph core, or scientific seeds.
    rows = [(actor, slot % 8, slot) for actor in range(8) for slot in range(32)]
    rng = random.Random(11001)
    null = []
    for _ in range(511):
        shuffled = []
        for actor in range(8):
            items = [slot % 8 for slot in range(32)]
            rng.shuffle(items)
            shuffled.extend((actor, item, slot) for slot, item in enumerate(items))
        null.append(coactivity(shuffled))
    observed = coactivity(rows)
    median = statistics.median(null)
    scale = 1.4826 * statistics.median(abs(x - median) for x in null)
    excess = (observed - median) / scale if scale else None
    assert coactivity(rows + rows[:20]) == observed
    print(json.dumps({"scope": "synthetic teaching illustration, not PHANTOM validation",
        "actors": 8, "slots": 32, "draws": 511, "illustration_seed": 11001,
        "observed_coactivity": observed, "null_median": median,
        "scaled_MAD": scale, "illustrative_robust_excess": excess,
        "exact_duplicate_invariance": True,
        "interpretation": "Unusual alignment under this toy shuffle; no causal label."}, indent=2))

if __name__ == "__main__":
    main()
