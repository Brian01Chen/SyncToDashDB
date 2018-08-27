import sys
sys.path.insert(0, '../Tool')
from Tool.Util import *
from Tool.Log import *


def get_dsjob_para():
    conf = ''
    if os.path.exists('configure'):
        conf = 'configure'
    else:
        log_factory('configure file not found !', 'error')


    len_argv = len(sys.argv)
    argv = []
    for i in range(12):
        if i < len_argv:
            argv.append(sys.argv[i])
        else:
            argv.append('')
    # DSW DB2 Database
    update_conf('DBNAME', argv[1], conf)
    # DSW DB2 Username
    update_conf('DBUSER', argv[2], conf)
    # DSW DB2 Password
    update_conf('DBPASSWD', crypt(argv[3]), conf)
    # CEDP DASHDB Database
    update_conf('BLUCEDPNAME', argv[4], conf)
    # CEDP DASHDB Username
    update_conf('BLUCEDPUSER', argv[5], conf)
    # CEDP DASHDB Password
    update_conf('BLUCEDPPASSWORD', crypt(argv[6]), conf)
    # DSW DB2 Extracted Table
    update_conf('SRCTABLE', argv[7], conf)
    # CEDP DASHDB Loaded Table-Schema
    update_conf('BLUTBSCHEMA', argv[8], conf)
    # CEDP DASHDB Loaded Table
    update_conf('BLUTABLE', argv[9], conf)
    # DSW DB2 INSTANCE Path
    update_conf('DB2ENV', argv[10], conf)
    # CURRENT Scripts Path
    update_conf('WKDIR', argv[11], conf)

