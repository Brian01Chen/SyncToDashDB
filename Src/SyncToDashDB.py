import Src.GetPara as getpara
import Src.DB2CLI as db2
import Src.FileTransfer as transfter
import Src.LiftCLI as lift



def get():
    para = getpara.getDSJobPara()
    dbsql = db2.export(**para)
    print(dbsql)
    p = lift.exeCommand(para['workdir'], para['s_db2env'], dbsql)
    print(p)