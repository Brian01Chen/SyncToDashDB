import os
import sys
import socket
import getpass
import platform
import datetime
import logging


class Log:

    def __init__(self, basedir=None, name=None):
        if basedir:
            self.basedir = basedir
        else:
            self.basedir = os.path.split(os.path.realpath(__file__))[0]
        if not self.basedir.endswith("/"):
            # linux directory need add /
            if platform.system() != 'Windows':
                self.basedir += "/"

        # create log directory
        # default use parent directory

        if platform.system() == 'Windows':
            self.log_dir = os.path.dirname(self.basedir) + "\log\\"
        else:
            self.log_dir = os.path.dirname(self.basedir) + "/log/"
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # remove file suffix
        if name:
            self.name = name
        else:
            self.name = os.path.splitext(os.path.split(os.path.realpath(__file__))[1])[0]

        # get current date
        self.today = datetime.datetime.now()
        self.today = str(self.today).replace(" ", ".").replace(":",".")

        # create log file
        self.logName = "%s%s_%s.txt" % (self.log_dir, self.name, self.today)

        # remove log file at first
        if os.path.exists(self.logName):
            try:
                os.remove(self.logName)
            except PermissionError as e:
                pass

        host = socket.gethostname()
        current_job = os.path.basename(os.path.realpath(sys.argv[0]))
        self.extra = {'host': host, 'user': getpass.getuser(), 'jobname': current_job}
        self.logger = self.logger_inst()

    def logger_inst(self):

        u_format = '%(asctime)-15s %(host)s %(user)s %(jobname)s: %(message)s'
        logging.basicConfig(format=u_format, filename=self.logName, filemode='w', datefmt='%Y-%m-%d %H:%M:%S')
        logger_inst = logging.getLogger('apt_log')
        logger_inst.setLevel(logging.DEBUG)
        return logger_inst

    def info(self, text):
        return self.logger.info(text, extra=self.extra)

    def debug(self, text):
        return self.logger.debug(text, extra=self.extra)

    def warning(self, text):
        return self.logger.warning(text, extra=self.extra)

    def error(self, text):
        return self.logger.error(text, extra=self.extra)


def log_factory(text, logtype=None):
    logger = Log()
    if logtype is None:
        logtype = 'info'
    return getattr(logger, logtype)(text)


def log_factory_path(basedir=None, name=None, text=None, logtype=None):
    logger = Log(basedir=basedir, name=name)
    if logtype is None:
        logtype = 'info'
    return getattr(logger, logtype)(text)


if __name__ == '__main__':
    log_factory('first', 'debug')
    log_factory('second', 'error')
    log_factory('third', 'info')
