import paramiko
import gzip, shutil
import zipfile

def ssh_scp_put(ip,user,password,local_file,remote_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, user, password)
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)
    ssh.close()

def compress(file, ctype):
    if ctype == 'gzip':
        cpfile = ''.join((file.rstrip('.csv'), '.gz'))
        with open(file, 'rb') as f_in:
            with gzip.open(cpfile, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    elif ctype == 'zip':
        cpfile = ''.join((file.rstrip('.csv'), '.zip'))
        f = zipfile.ZipFile(cpfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(cpfile)
        f.close()

def uncompress(file, ctype):
    if ctype == 'gzip':
        cpfile = ''.join((file.rstrip('.gz'), '.csv'))
        g = gzip.GzipFile(mode="rb", fileobj=open(file, 'rb'))
        with open(cpfile, "wb") as f:
            f.write(g.read())
