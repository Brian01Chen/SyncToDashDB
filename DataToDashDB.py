import sys
import Src.GetPara as getpara
import Src.DB2CLI as db2
import Src.FileTransfer as filedtl
import Src.LiftCLI as lift
sys.path.insert(0, 'Tool')
from Tool.Util import *


getpara.get_dsjob_para()
para = read_conf('configure')


# execute on Local Server
def put_file_to_lift_server():

    exp_file = db2.exeExport(para['SRCTABLE'], '.', para['DB2ENV'], db2.export(**para))
    comp_file = filedtl.compress(exp_file)

    remote_path = para['LIFTWKDIR']
    if not remote_path.endswith("/"):
        remote_path += '/'
    remote_full_path = ''.join((remote_path, comp_file))
    log_factory(remote_full_path)
    filedtl.ssh_scp_put(comp_file, remote_full_path, para)

    return comp_file


# execute on Lift server
def lift_load_to_cedp(comp_file):

    # entry to the work_path in Lift Server
    work_path = 'cd ' + para['LIFTWKDIR']
    decompress_command = 'gunzip ' + comp_file
    log_factory(para)
    ssh_exe_com(work_path + ';' + decompress_command, **para)

    # put to DashDB
    csv_file = comp_file.rstrip('.gz')
    exe_env = '. ../.bash_profile'
    ssh_exe_com(work_path + ';' + exe_env + ';' + lift.lift_put(csv_file), **para)
    ssh_exe_com(work_path + ';' + exe_env + ';' + lift.lift_ls(), **para)
    ssh_exe_com(work_path + ';' + exe_env + ';' + lift.lift_load(csv_file), **para)
    ssh_exe_com(work_path + ';' + exe_env + ';' + lift.lift_rm(csv_file), **para)


@Timeit
def all_thr_lift():
    work_path = 'cd ' + para['LIFTWKDIR']
    exe_env = '. ~/.bash_profile'
    # ssh_exe_com(work_path + ';' + exe_env + ';' + lift.lift_ext(), **para)
    csv_file = para['TMPFILE']
    ssh_exe_com(work_path + ';' + exe_env + ';' + lift.lift_put(csv_file), **para)
    ssh_exe_com(work_path + ';' + exe_env + ';' + lift.lift_ls(), **para)
    ssh_exe_com(work_path + ';' + exe_env + ';' + lift.lift_load(csv_file), **para)
    # ssh_exe_com(work_path + ';' + exe_env + ';' + lift.lift_rm(csv_file), **para)


if __name__ == '__main__':
    log_factory('Data Sync To CEDP DashDB Batch Job Start!')
    # com_file = 'DWDM2.APPL_DATA_RECENCY.csv.gz'
    # lift_load_to_cedp(com_file)
    all_thr_lift()
