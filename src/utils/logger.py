import logging

# Setting up the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler to store logs
file_handler = logging.FileHandler('/var/log/intrusion_detection.log')
file_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the file handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Create console handler for outputting to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

# Function to log info messages
def log_info(message):
    logger.info(message)

# Function to log error messages
def log_error(message):
    logger.error(message)
