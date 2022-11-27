
"""
Url : https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
url for formatter  :https://docs.python.org/3/library/logging.html#logrecord-attributes
url for datetime  : https://docs.python.org/3/library/time.html#time.strftime
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
# logging.basicConfig(level=logging.ERROR) # append mode
logging.basicConfig(format='%(asctime)s : %(levelname)s  : %(message)s ',
                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.ERROR) # append mode
logging.warning("warning message")
logging.info("info message")
logging.error("error message")
logging.debug("This is a debug message ")
logging.critical("This is a critical message ")