import time
import os
import subprocess
from datetime import datetime
from Tool.Log import logger


class Timeit(object):
    def __init__(self, func):
        self._wrapped = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        logger("Job start time is %s " % datetime.now())
        result = self._wrapped(*args, **kwargs)
        logger("Job end time is %s " % datetime.now())
        logger("elapsed time is %s " % round(time.time() - start_time, 3))
        return result


def read_conf(conf):
    para = {}
    with open(conf, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            if len(line.strip()) == 0:
                break
            kv = line.strip().split('=')
            para.setdefault(kv[0], kv[1])

    return para


def write_conf(content, filename):
    with open(filename, 'w+') as f:
        lines = content.split('\n')
        for line in lines:
            if len(line.strip()) == 0:
                break
            f.write(line)


def exe_com(commdstr, path):
    logger(commdstr)
    env = os.environ.copy()
    p = subprocess.Popen(commdstr, shell=True, cwd=path, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.communicate()
    logger(result)
    p.wait()
    status = p.returncode
    logger(status)
    return status