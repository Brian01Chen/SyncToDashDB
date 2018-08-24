
from Tool.Util import *
from Tool.Log import *


@Timeit
def export(**kwargs):
    conn_str = 'connect to @t_db_name user @t_user using @t_pwd @'
    export_str = 'export to @t_table.csv of del select * from @t_table @'
    if 't_db_name' not in kwargs.keys():
        print('t_db_name is NULL !')
    if 't_user' not in kwargs.keys():
        print('t_user is NULL !')
    if 't_pwd' not in kwargs.keys():
        print('t_pwd is NULL !')
    if 't_src_table' not in kwargs.keys():
        print('t_table is NULL !')
    conn_str = conn_str.replace('@t_db_name', kwargs['DBNAME']).replace('@t_user', kwargs['DBUSER']) \
        .replace('@t_pwd', kwargs['DBPASSWD'])
    export_str = export_str.replace('@t_db_name', kwargs['DBNAME']).replace('@t_user', kwargs['DBUSER']) \
        .replace('@t_pwd', kwargs['DBPASSWD']).replace('@t_table', kwargs['TABLE'])
    dbsql = '\n'.join((conn_str, export_str))
    return dbsql


@Timeit
def exeExport(exptable, workpath, db2envpath, dbsql):

    exe_com(''.join((os.path.dirname(db2envpath), '/db2profile'), '.'))

    os.chdir(workpath)
    sqlfile = '.'.join((exptable, 'sql'))
    with open(sqlfile, 'w+') as f:
        f.write(dbsql)
    if os.path.exists(sqlfile):
        if os.path.getsize(sqlfile):
            logger(sqlfile + 'write successful! ')

    commstr = ''.join(('db2 -td@ -f ', sqlfile, ' > 1.out'))
    exe_com(commstr, '.')

    expfile = ''.join((exptable, '.csv'))
    if os.path.exists(expfile):
        if os.path.getsize(expfile):
            return expfile
        else:
            logger('empty file:' + expfile, 'error')
            return None
    else:
        logger(expfile + ' generate error! ', 'error')
        return None

