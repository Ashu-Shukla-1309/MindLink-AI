import time
from agents.coordinator import CoordinatorWithPolicy

def run_tests(cases):
    coord = CoordinatorWithPolicy()
    results = []
    for c in cases:
        t0 = time.time()
        out = coord.ask(c)
        latency = (time.time() - t0) * 1000
        results.append({"input": c, "output": out, "latency_ms": latency})
    return results

if __name__ == "__main__":
    cases = [
        "I want to cancel my subscription.",
        "My invoice amount is wrong: INV-12345",
        "Hi, how do I reset my password?"
    ]
    res = run_tests(cases)
    import json
    print(json.dumps(res, indent=2))
