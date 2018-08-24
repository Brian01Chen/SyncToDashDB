import Src.GetPara as getpara
import Src.DB2CLI as db2
import Src.FileTransfer as filedtl
import Src.LiftCLI as lift
from Tool.Log import *


def put_file_to_lift_server():
    para = getpara.get_dsjob_para()
    print(para)
    exp_file = db2.exeExport(para['TABLE'], '.', para['DB2ENV'], db2.export(**para))
    gz_file = filedtl.compress(exp_file)
    conn = filedtl.ssh_conn('pdydaldal1302.sl.bluecloud.ibm.com', 'dswusr1', 'Get1ndsw')
    os.chdir(para['WKDIR'])
    logger(os.getcwd())
    filedtl.scp_put(conn, gz_file, gz_file)
    return gz_file


def lift_load_to_cedp(gz_file):
    csv_file = filedtl.decompress(gz_file)
    lift.lift_put(csv_file)
    lift.lift_ls()
    lift.lift_load(csv_file)
    lift.lift_rm(csv_file)


if '__name__' == '__main__':
    gz_file = put_file_to_lift_server()
    lift_load_to_cedp(gz_file)
