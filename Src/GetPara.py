import sys


def getDSJobPara():
    para = {}
    para.setdefault('DBNAME', sys.argv[1])
    para.setdefault('DBUSER', sys.argv[2])
    para.setdefault('DBPASSWD', sys.argv[3])
    para.setdefault('TABLE', sys.argv[4])
    para.setdefault('DB2ENV', sys.argv[5])
    para.setdefault('WKDIR', sys.argv[6])
    return para
