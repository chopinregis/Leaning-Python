"""
Exercise 5: Implement Logging in a Simple Function
Create a Python function that logs different types of messages.
The function should attempt to open a file and read its contents.
Use logging to:
Log an INFO message before attempting to open the file.
Log a DEBUG message to show file contents.
Log an ERROR message if the file doesn't exist.
"""

import logging

# Configure logging at the beginning of your script
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def read_file(filename):
    logger = logging.getLogger(__name__)  # Create a logger object
    logger.info(f"Attempting to open the file: {filename}")  # Log an INFO message before attempting to open the file
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            logger.debug(f"File contents: {content}")  # Log a DEBUG message to show file contents
    except FileNotFoundError:
        logger.error(f"The file {filename} was not found.")  # Log an ERROR message if the file doesn't exist

# Call the function with a filename that likely does not exist to demonstrate error logging
read_file('example.txt')

# Output:
# Attempting to open the file: example.txt

"""
Testing the Script:
When example.txt exists, the content will be logged at the DEBUG level.
When example.txt does not exist, it logs an ERROR indicating the file was not found.

Use in AWS Lambda:
When adapting this for AWS Lambda, ensure that CloudWatch logging permissions are correctly configured so that your Lambda function can write logs to CloudWatch. 
This setup allows you to monitor and troubleshoot your function's behavior in the AWS environment effectively.
"""