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
#
# # logger = logging
# #
# logging.basicConfig(level=logging.ERROR) # # defined a logger with level as ERROR
# logging.basicConfig(level=logging.DEBUG) # # defined a logger with level as Dbug - the lowest one
# logging.basicConfig(level=logging.CRITICAL) # # defined a logger with level as Dbug - the lowest one
# logging.basicConfig(format='%(asctime)s : %(levelname)s  : %(name)s : %(message)s ',level = logging.INFO)
# logging.basicConfig(format='%(asctime)s : %(levelname)s  : %(name)s : %(message)s ',
#                     datefmt='%a %m/%d/%Y %I:%M:%S %p',
#                     level = logging.INFO)
# logging.basicConfig(format='%(asctime)s : %(levelname)s  : %(name)s : %(message)s ',
#                      datefmt='%a %m/%d/%Y %I:%M:%S %p',
#                      filename="example1.log",
#                      level = logging.INFO)
logging.basicConfig(format='%(asctime)s : %(levelname)s  : %(name)s : %(message)s ',
                     datefmt='%a %m/%d/%Y %I:%M:%S %p',
                     filename="example1.log",
                     filemode="w",
                     level = logging.INFO)


logging.warning("This is a warning message")  # default value
logging.info("This is a info message")  # have not been printd
logging.error("This is a error message")
logging.debug("This is a debug message ")
logging.critical("This is a critical message ")