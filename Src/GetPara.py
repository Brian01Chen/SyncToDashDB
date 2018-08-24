import sys
from Tool.Util import *


def get_dsjob_para():
    conf = ''
    if os.path.exists():
        conf = 'configure'
    else:
        logger('configure file not found !', 'error')
    para = {}
    # DSW DB2 Database
    para.setdefault('DBNAME', sys.argv[1])
    update_conf('DBNAME', sys.argv[1], conf)
    # DSW DB2 Username
    para.setdefault('DBUSER', sys.argv[2])
    update_conf('DBUSER', sys.argv[2], conf)
    # DSW DB2 Password
    para.setdefault('DBPASSWD', sys.argv[3])
    update_conf('DBPASSWD', sys.argv[3], conf)
    # CEDP DASHDB Database
    para.setdefault('BLUCEDPNAME', sys.argv[4])
    update_conf('BLUCEDPNAME', sys.argv[4], conf)
    # CEDP DASHDB Username
    para.setdefault('BLUCEDPUSER', sys.argv[5])
    update_conf('BLUCEDPUSER', sys.argv[5], conf)
    # CEDP DASHDB Password
    para.setdefault('BLUCEDPPASSWORD', sys.argv[6])
    update_conf('BLUCEDPPASSWORD', sys.argv[6], conf)
    # DSW DB2 Extracted Table
    para.setdefault('SRCTABLE', sys.argv[7])
    update_conf('SRCTABLE', sys.argv[7], conf)
    # CEDP DASHDB Loaded Table-Schema
    para.setdefault('BLUTBSCHEMA', sys.argv[8])
    update_conf('BLUTBSCHEMA', sys.argv[8], conf)
    # CEDP DASHDB Loaded Table
    para.setdefault('BLUTABLE', sys.argv[9])
    update_conf('BLUTABLE', sys.argv[9], conf)
    # DSW DB2 INSTANCE Path
    para.setdefault('DB2ENV', sys.argv[10])
    update_conf('DB2ENV', sys.argv[10], conf)
    # CURRENT Scripts Path
    para.setdefault('WKDIR', sys.argv[11])
    update_conf('WKDIR', sys.argv[11], conf)
    return para
