# quicklogging
Utilities to quickly setup best practice logging for Python.


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