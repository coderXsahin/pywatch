def analyze_root_cause(message):
    if message == "Database connection failed":
        return "Database server may be unavailable or unreachable"
    if message == "Payment service unavailable":
        return "Payment service may be down or experiencing connectivity issues"
    return "Unknown root cause"
