import paramiko
import gzip
import shutil
import zipfile
from Tool.Util import *


@Timeit
def ssh_conn(ip, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, user, password)
    message = 'Connect to %s' % ip
    logger(message)
    return ssh


@Timeit
def scp_put(ssh, local_file, remote_file):
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)
    message = 'put %s to %s' % (local_file, remote_file)
    logger(message)
    ssh.close()
    return remote_file

@Timeit
def compress(file, ctype='gzip'):
    if ctype == 'gzip':
        cp_file = ''.join((file.rstrip('.csv'), '.gz'))
        with open(file, 'rb') as f_in:
            with gzip.open(cp_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    elif ctype == 'zip':
        cp_file = ''.join((file.rstrip('.csv'), '.zip'))
        f = zipfile.ZipFile(cp_file, 'w', zipfile.ZIP_DEFLATED)
        f.write(cp_file)
        f.close()
    message = 'compress %s using %s' % (file, ctype)
    logger(message)
    return cp_file


@Timeit
def decompress(file, ctype='gzip'):
    if ctype == 'gzip':
        csv_file = ''.join((file.rstrip('.gz'), '.csv'))
        g = gzip.GzipFile(mode="rb", fileobj=open(file, 'rb'))
        with open(csv_file, "wb") as f:
            f.write(g.read())
    message = 'decompress %s using %s' % (file, ctype)
    logger(message)
    return csv_file
