"""
Introduction to Logging in Python
Python provides a built-in module called logging that allows you to log messages that can be configured to different severity levels (DEBUG, INFO, WARNING, ERROR, and CRITICAL). 
This makes it easy to differentiate between minor debug messages and serious errors.
"""
# Basic Logging Setup

import logging

# Configure logging to show the logger name and the severity level of the log message
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger object
logger = logging.getLogger(__name__)

# Logging messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Output:
# 2022-10-26 17:33:43,631 - __main__ - DEBUG - This is a debug message

"""
The 'basicConfig' method sets up the basic configuration for logging:

level: Sets the threshold for what levels of messages should be logged. DEBUG is the lowest level, capturing everything.
format: Defines the format of the log messages.
"""