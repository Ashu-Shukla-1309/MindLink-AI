import logging
logger = logging.getLogger("mindlink.metrics")
logger.setLevel(logging.INFO)

_METRICS = {"requests":0, "errors":0, "avg_latency_ms":0.0}

def record_request(latency_ms: float, success=True):
    global _METRICS
    _METRICS["requests"] += 1
    if not success:
        _METRICS["errors"] += 1
    prev = _METRICS["avg_latency_ms"]
    n = _METRICS["requests"]
    _METRICS["avg_latency_ms"] = ((prev*(n-1))+latency_ms)/n
    logger.info("metrics_update %s", _METRICS)

def get_metrics():
    return _METRICS.copy()
