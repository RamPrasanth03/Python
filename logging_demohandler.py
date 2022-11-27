import logging

"""
format='%(asctime)s : %(levelname)s  : %(name)s : %(message)s ',
#                      datefmt='%a %m/%d/%Y %I:%M:%S %p'
We are creating a custom logger to utilise in our code . 
"""


class LoggerDemoConsole():

    def testLog(self):
        # create logger
        # implementing the name of logger as the class name
        logger1 = logging.getLogger(LoggerDemoConsole.__name__)
        logger_basic = logging.basicConfig(level=logging.DEBUG)
        # setting the level of logger
        logger1.setLevel(logging.INFO)

        # create console handler and set level to info
        consoleHandler = logging.StreamHandler()
        # the priority of level is set by the handler , rather than the logger
        consoleHandler.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter(fmt='%(asctime)s : %(levelname)s  : %(name)s : %(message)s ',
                                      datefmt='%a %m/%d/%Y %I:%M:%S %p')

        # add formatter to console handler
        consoleHandler.setFormatter(formatter)

        # add console handler to logger
        logger1.addHandler(consoleHandler)

        # logging messages
        logger1.debug('debug message')
        logger1.info('info message')
        logger1.warning('warn message')
        logger1.error('error message')
        logger1.critical('critical message')



demo = LoggerDemoConsole()
demo.testLog()