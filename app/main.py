import logging
import random
import time
logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("PyWatch")
events = [
    ("info", "User login successful"),
    ("info", "Payment request received"),
    ("info", "Order processed successfully"),
    ("warning", "Database response time is high"),
    ("error", "Database connection failed"),
    ("error", "Payment service unavailable")
]
while True:
    level, message = random.choice(events)
    try:
        if message == "Database connection failed":
            raise ConnectionError("Unable to connect to database")
        if message == "Payment service unavailable":
            raise RuntimeError("Payment service is not responding")
        if level == "info":
            logger.info(message)
        elif level == "warning":
            logger.warning(message)
    except Exception:
        logger.exception(message)
    time.sleep(2)
