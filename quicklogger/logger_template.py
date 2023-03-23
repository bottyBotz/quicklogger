import logging
import sys

# Possible logging levels and when to use them:
# DEBUG: Detailed information, typically of interest only when diagnosing problems
# INFO: Confirmation that things are working as expected
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low')
# ERROR: Due to a more serious problem, the software has not been able to perform some function
# CRITICAL: A very serious error, indicating that the program itself may be unable to continue running

# You can change the logging level by setting the level argument below to one of the following:
# logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL
def setup_logger(level=logging.INFO, log_file=None):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler to write logs to a file
    file_handler = logging.FileHandler(f'{__name__}.log')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Create a console handler to display logs in the console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()

# Example usage:
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
