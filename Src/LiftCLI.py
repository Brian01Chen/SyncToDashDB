
from Tool.Util import *
from Tool.Log import *


para = read_conf('configure')


def lift_ext():

    tgt_file = para['TMPFILE']
    ext_command = 'lift extract -ss #SCHEMA -st #SRCTABLE -sd #DSWDB -su #DBUSER -sp #DBPASSWD -sh #DBHOST -sdp #PORT ' \
                  '-sdt db2 -ssl ' \
                  '-f #file -rp'

    ext_command = ext_command.replace('#SCHEMA', para['SRCSCHEMA']).replace('#SRCTABLE', para['SRCTABLE'])\
        .replace('#file', tgt_file) \
        .replace('#DSWDB', para['DSWDB']).replace('#DBHOST', para['DBHOST']).replace('#PORT', para['PORT'])    \
        .replace('#DBUSER', para['DBUSER']).replace('#DBPASSWD', "'" + para['DBPASSWD'] + "'")
    return ext_command


def lift_put(datafile):

    ext_command = 'lift put -f #TRGTFILE -tu #BLUCEDPUSER -tp #BLUCEDPPASSWORD --target-host #BLUCEDPHOST -rp'
    ext_command = ext_command.replace('#TRGTFILE', datafile)
    ext_command = ext_command.replace('#BLUCEDPUSER', para['BLUCEDPUSER'])\
        .replace('#BLUCEDPPASSWORD', "'" + para['BLUCEDPPASSWORD'] + "'")\
        .replace('#BLUCEDPHOST', para['BLUCEDPHOST'])
    return ext_command


def lift_load(datafile):

    ext_command = 'lift load -f #TRGTFILE -ts #BLUTBSCHEMA -tt #BLUTABLE -tu #BLUCEDPUSER -tp #BLUCEDPPASSWORD \
                   -th #BLUCEDPHOST -fo db2 -a replace'
    ext_command = ext_command.replace('#TRGTFILE', os.path.basename(datafile))
    ext_command = ext_command.replace('#BLUTBSCHEMA', para['BLUTBSCHEMA']).replace('#BLUTABLE', para['BLUTABLE'])\
        .replace('#BLUCEDPUSER', para['BLUCEDPUSER'])\
        .replace('#BLUCEDPPASSWORD', "'" + para['BLUCEDPPASSWORD'] + "'") \
        .replace('#BLUCEDPHOST', para['BLUCEDPHOST'])
    return ext_command


def lift_ls():

    ext_command = 'lift ls -tu #BLUCEDPUSER -tp #BLUCEDPPASSWORD -th #BLUCEDPHOST '
    ext_command = ext_command.replace('#BLUCEDPUSER', para['BLUCEDPUSER']) \
        .replace('#BLUCEDPPASSWORD', "'" + para['BLUCEDPPASSWORD'] + "'") \
        .replace('#BLUCEDPHOST', para['BLUCEDPHOST'])
    return ext_command


def lift_rm(datafile):

    ext_command = 'lift rm -f #TRGTFILE -tu #BLUCEDPUSER -tp #BLUCEDPPASSWORD -th #BLUCEDPHOST '
    ext_command = ext_command.replace('#TRGTFILE', os.path.basename(datafile))
    ext_command = ext_command.replace('#BLUCEDPUSER', para['BLUCEDPUSER']) \
        .replace('#BLUCEDPPASSWORD', "'" + para['BLUCEDPPASSWORD'] + "'") \
        .replace('#BLUCEDPHOST', para['BLUCEDPHOST'])

    return ext_command


if __name__ == '__main__':
    p = lift_ext('DWDM2', 'APPL_DATA_RECENCY', r'C:\Users\SongChen\WorkSpace\Data\temp.csv')
