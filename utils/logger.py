import logging
import os
from datetime import datetime

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

# Log file name with timestamp
log_filename = f"logs/mediscan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — [%(levelname)s] — %(message)s",
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

# Expose logger instance
logger = logging.getLogger("mediscan_logger")
