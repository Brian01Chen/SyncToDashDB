
from Tool.Util import *
from Tool.Log import *


@Timeit
def export(**kwargs):
    conn_str = 'connect to @t_db_name user @t_user using @t_pwd @'
    export_str = 'export to @t_table.csv of del select * from @t_table @'
    if 'DBNAME' not in kwargs.keys():
        print('DBNAME is NULL !')
    if 'DBUSER' not in kwargs.keys():
        print('DBUSER is NULL !')
    if 'DBPASSWD' not in kwargs.keys():
        print('DBPASSWD is NULL !')
    if 'SRCTABLE' not in kwargs.keys():
        print('SRCTABLE is NULL !')
    conn_str = conn_str.replace('@t_db_name', kwargs['DBNAME']).replace('@t_user', kwargs['DBUSER']) \
        .replace('@t_pwd', kwargs['DBPASSWD'])
    export_str = export_str.replace('@t_db_name', kwargs['DBNAME']).replace('@t_user', kwargs['DBUSER']) \
        .replace('@t_pwd', kwargs['DBPASSWD']).replace('@t_table', kwargs['SRCTABLE'])
    dbsql = '\n'.join((conn_str, export_str))
    return dbsql


@Timeit
def exeExport(exptable, workpath, db2envpath, dbsql):
    command_str = ''
    path = '.'
    if db2envpath == '' or db2envpath is None:

        log_factory('DB2 instance env: ' + 'Not Provided')
    else:
        log_factory('DB2 instance env: ' + ''.join((os.path.dirname(db2envpath), '/db2profile')))
        exe_com(''.join((os.path.dirname(db2envpath), '/db2profile')), '.')

    os.chdir(workpath)
    sql_file = '.'.join((exptable, 'sql'))
    with open(sql_file, 'w+') as f:
        f.write(dbsql)
    if os.path.exists(sql_file):
        if os.path.getsize(sql_file):
            log_factory(sql_file + ' write successful! ')

        command_str += ''.join(('db2 -td@ -f ', sql_file))

    output_file = open('export.out', 'w+')
    exe_com(command_str, path, output_file=output_file, shell=False)

    exp_file = ''.join((exptable, '.csv'))
    if os.path.exists(exp_file):
        if os.path.getsize(exp_file):
            log_factory(exp_file + ' generate successful! ')
            return exp_file
        else:
            log_factory('empty file:' + exp_file, 'error')
            return None
    else:
        log_factory(exp_file + ' generate error! ', 'error')
        return None

