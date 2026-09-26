def get_recommendation(message):
    if message == "Database connection failed":
        return "Check database server status, network connectivity, credentials, and connection pool."
    if message == "Payment service unavailable":
        return "Check payment service health, API connectivity, service logs, and recent deployments."
    return "Review application logs and investigate the affected component."
