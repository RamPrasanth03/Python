

"""
Url : https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
Logging Demo 1
Logging Levels
DEBUG
INFO
WARNING - default one
ERROR
CRITICAL
"""
import logging

# logger = logging
#
logging.basicConfig(filename="test.log",filemode='w', level=logging.ERROR) # append mode
logging.warning("warning message")
logging.info("info message")
logging.error("error message")
logging.debug("This is a debug message ")
logging.critical("This is a critical message ")
