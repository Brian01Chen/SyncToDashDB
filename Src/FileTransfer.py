import gzip
import shutil
import zipfile
from Tool.Util import *
from Tool.Log import *


@Timeit
def ssh_scp_put(local_file, remote_file, **kwargs):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(kwargs['LIFTSERVER'], 22, kwargs['LIFTUSER'], kwargs['LIFTPASSWD'], timeout=10)
    log_factory(client)
    sftp = client.open_sftp()
    sftp.put(local_file, remote_file)
    message = 'put %s to %s' % (local_file, remote_file)
    log_factory(message)
    client.close()
    return remote_file


@Timeit
def compress(file, ctype='gzip'):
    if file:
        if ctype == 'gzip':
            cp_file = ''.join((file, '.gz'))
            with open(file, 'rb') as f_in:
                with gzip.open(cp_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        elif ctype == 'zip':
            cp_file = ''.join((file, '.zip'))
            f = zipfile.ZipFile(cp_file, 'w', zipfile.ZIP_DEFLATED)
            f.write(cp_file)
            f.close()
        message = 'compress %s using %s' % (file, ctype)
        log_factory(message)
        return cp_file
    else:
        log_factory('compress file not supplyed', 'error')
        return None


@Timeit
def decompress(file, dtype='gzip'):
    if file:
        if dtype == 'gzip':
            csv_file = file.rstrip('.gz')
            g = gzip.GzipFile(mode="rb", fileobj=open(file, 'rb'))
            with open(csv_file, "wb") as f:
                f.write(g.read())
        message = 'decompress %s using %s' % (file, dtype)
        log_factory(message)
        return csv_file
    else:
        log_factory('decompress file not supplyed', 'error')
        return None
