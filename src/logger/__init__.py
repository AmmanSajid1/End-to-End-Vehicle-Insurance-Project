import logging
import os 
from logging.handlers import RotatingFileHandler
from from_root import from_root 
from datetime import datetime 

# Constants for log configuration 
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1025 * 1024 # 5 MB
BACKUP_COUNT = 3 # Number of backup log files to keep 

# Construct log file path
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler
    """

    # Create a custom logger 
    logger = logging.getLogger()
    logging.getLogger('pymongo').setLevel(logging.CRITICAL) # Supress excessive pymongo logs
    logging.getLogger("multipart").setLevel(logging.ERROR) # Supress excessive python multipart logs
    logging.getLogger('boto').setLevel(logging.CRITICAL) # Supress excessive boto3 logs
    logging.getLogger('botocore').setLevel(logging.CRITICAL) # Supress excessive botocore logs
    logger.setLevel(logging.DEBUG)

    # Define formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s -%(levelname)s - %(message)s")

    # File handler with rotation
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    # Add handlers to the logger 
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Configure the logger
configure_logger()