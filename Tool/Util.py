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


def update_conf(key, content, filename):
    contents = ''
    with open(filename, 'r') as f:
        for line in f:
            if len(line.strip()) == 0:
                break
            if line.startswith(key) and content != '' and content is not None:
                line = key + '=' + content + '\n'
            contents += line
    with open(filename, 'w+') as f:
        f.write(contents)


def exe_com(command_str, path):
    logger(command_str)
    env = os.environ.copy()
    p = subprocess.Popen(command_str, shell=True, cwd=path, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.communicate()
    logger(result)
    p.wait()
    status = p.returncode
    logger(status)
    return status


if __name__ == '__main__':
    update_conf('DALSCHEMA', 'DSDWWWW', '../configure')
