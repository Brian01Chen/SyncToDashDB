import time
import os
import subprocess
from datetime import datetime
from Tool.Log import log_factory
import hashlib
import paramiko


class Timeit(object):
    def __init__(self, func):
        self._wrapped = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        log_factory(self._wrapped.__name__ + " job start time is %s " % datetime.now())
        result = self._wrapped(*args, **kwargs)
        log_factory(self._wrapped.__name__ + " job end time is %s " % datetime.now())
        log_factory(self._wrapped.__name__ + " job elapsed time is %s " % round(time.time() - start_time, 4))
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
            if line.startswith('WORKDIR') and line.split('=')[1].strip() == '':
                line = key + '=' + os.getcwd() + '\n'
            contents += line
    with open(filename, 'w+') as f:
        f.write(contents)


def exe_com(command_str, path, output_file=None, shell=True):
    log_factory(command_str)
    env = os.environ.copy()
    p = subprocess.Popen(command_str, shell=shell, cwd=path, env=env,
                         stdout=output_file,
                         stderr=subprocess.STDOUT)
    while p.poll() is None:
        # waiting for subprocess finished

        if p.stderr:
            line = p.stderr.readlines().strip()
            log_factory(line)
    if p.returncode == 0:
        log_factory(command_str + ' finish')
    return p.returncode


@Timeit
def ssh_exe_com(command_str, server='Lift', **kwargs):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if server == 'Lift':
        client.connect(kwargs['LIFTSERVER'], 22, kwargs['LIFTUSER'], kwargs['LIFTPASSWD'], timeout=30)
    elif server == 'DB2':
        client.connect(kwargs['DBHOST'], 22, kwargs['DBUSER'], kwargs['DBPASSWD'], timeout=30)
    else:
        log_factory('Error Host Type', 'error')
    log_factory(command_str)
    stdin, stdout, stderr = client.exec_command(command_str, get_pty=True)
    stdin.close()
    for line in stdout.read().splitlines():
        log_factory(line)
    channel = stdout.channel
    status = channel.recv_exit_status()
    log_factory('Command Status: ' + str(status))
    client.close()


def encode_pass(password_str):
    h = hashlib.sha1()
    h.update(bytes(password_str, encoding='utf-8'))
    return h.hexdigest()


def crypt(source, key=''):
    from itertools import cycle
    result = ''
    temp = cycle(key)
    for ch in source:
        try:
            result = result+chr(ord(ch) ^ ord(next(temp)))
        except StopIteration:
            pass
    return result


if __name__ == '__main__':
    new_pass = encode_pass('d3214')
    print(new_pass)
    new_pass = crypt('d3214', 'tt')
    print(new_pass)
    new_pass = crypt(new_pass, 'tt')
    print(new_pass)
