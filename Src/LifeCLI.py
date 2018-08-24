
from Tool.Util import *
from Tool.Log import *


para = read_conf('configure')




@Timeit
def lift_ext(schema, tabname, trgtfile):
    ext_command = 'lift extract -ss #SCHEMA -st #TABLE -sd #DATABASE -su #USER -sp #PASSWORD -sh #HOST -sdp #PORT ' \
                  '-sdt db2 -ssl ' \
                  '-f #TRGTFILE -rp'
    ext_command = ext_command.replace('#SCHEMA', schema).replace('#TABLE', tabname).replace('#TRGTFILE', trgtfile) \
        .replace('#DATABASE', para['DATABASE']).replace('#HOST', para['HOST']).replace('#PORT', para['PORT'])    \
        .replace('#USER', para['USER']).replace('#PASSWORD', para['PASSWORD'])

    exe_com(ext_command, '.')


@Timeit
def lift_put(datafile):

    ext_command = 'lift put -f #TRGTFILE -tu #DALSUSER -tp #DALSPASSWORD --target-host #DALSHOST -rp'
    ext_command = ext_command.replace('#TRGTFILE', datafile)
    ext_command = ext_command.replace('#DALSUSER', para['DALSUSER']).replace('#DALSPASSWORD',para['DALSPASSWORD'])\
        .replace('#DALSHOST', para['DALSHOST'])

    exe_com(ext_command, '.')


@Timeit
def lift_load(datafile):

    ext_command = 'lift load -f #TRGTFILE -ts #DALSCHEMA -tt #DALTABLE -tu #DALSUSER -tp #DALSPASSWORD \
                   -th #DALSHOST -fo db2 -a replace'
    ext_command = ext_command.replace('#TRGTFILE', os.path.basename(datafile))
    ext_command = ext_command.replace('#DALSCHEMA', para['DALSCHEMA']).replace('#DALTABLE', para['DALTABLE'])\
        .replace('#DALSUSER', para['DALSUSER']).replace('#DALSPASSWORD', para['DALSPASSWORD']) \
        .replace('#DALSHOST', para['DALSHOST'])

    exe_com(ext_command, '.')


@Timeit
def lift_ls():

    ext_command = 'lift ls -tu #DALSUSER -tp #DALSPASSWORD -th #DALSHOST '
    ext_command = ext_command.replace('#DALSUSER', para['DALSUSER']) \
        .replace('#DALSPASSWORD', para['DALSPASSWORD']) \
        .replace('#DALSHOST', para['DALSHOST'])

    exe_com(ext_command, '.')


@Timeit
def lift_rm(datafile):

    ext_command = 'lift rm -f #TRGTFILE -tu #DALSUSER -tp #DALSPASSWORD -th #DALSHOST '
    ext_command = ext_command.replace('#TRGTFILE', os.path.basename(datafile))
    ext_command = ext_command.replace('#DALSUSER', para['DALSUSER']) \
        .replace('#DALSPASSWORD', para['DALSPASSWORD']) \
        .replace('#DALSHOST', para['DALSHOST'])

    exe_com(ext_command, '.')

if __name__ == '__main__':
    p = lift_ext('DWDM2', 'APPL_DATA_RECENCY', r'C:\Users\SongChen\WorkSpace\Data\temp.csv')