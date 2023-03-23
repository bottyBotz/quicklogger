"""
This module provides a simple way to set up a logger with both file and console handlers for Python applications.

It is designed to help developers quickly configure logging with minimal effort. The logger instance created by
the setup_logger function will have two handlers: one for writing log messages to a file, and another for
printing log messages to the console (stdout). The log format is standardized as:
'%(asctime)s - %(name)s - %(levelname)s - %(message)s'

Users can choose from five logging levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL. By default, the logging level
is set to INFO. To change the logging level, simply pass a different level (e.g., logging.DEBUG or logging.WARNING)
as the level argument when calling the setup_logger function.

Example usage:

logger = setup_logger()
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

To customize the logger name or log file path, pass the desired values as arguments to the setup_logger function.

For more advanced logging configurations, consider using the built-in logging module directly and refer to the
official Python documentation:
https://docs.python.org/3/library/logging.html

"""

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
def setup_logger(name=__name__, level=logging.INFO, log_file=None):
    """
    Set up a logger with file and console handlers.
    
    :param name: The name of the logger, defaults to the name of the calling module.
    :param level: The logging level, e.g., logging.DEBUG, logging.INFO, logging.WARNING, etc., defaults to logging.INFO.
    :param log_file: The path to the log file, defaults to None which creates a log file with the name of the calling module.
    
    :return: A configured logger instance.
    
    The logger will have two handlers:
    1. A file handler that writes logs to a file with the specified path or a default log file named '{name}.log'.
    2. A console handler that prints logs to the console (stdout).
    
    The log format is: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    """
    ...
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler to write logs to a file
    if log_file is None:
        log_file = f'{name}.log'
    file_handler = logging.FileHandler(log_file)
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


