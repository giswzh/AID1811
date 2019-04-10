import pymysql
import warnings
# 数据库连接对象
db = pymysql.connect('localhost','root','123456',charset='utf8')
# 游标对象
cursor = db.cursor()

# 执行sql命令
c_db = 'create database if not exists tencent charset utf8'
u_db = 'use tencent'
c_tab = 'create table if not exists top_list(\
        name varchar(80), job_name varchar(40),\
        job_type varchar(20),job_number varchar(4),\
        job_address varchar(8), job_time varchar(30),\
        job_duty varchar(500), job_demand varchar(500))'
ins = 'insert into stuinfo values("Tom")'
# 忽略警告
warnings.filterwarnings('ignore')
cursor.execute(c_db)
cursor.execute(u_db)
cursor.execute(c_tab)
# cursor.execute(ins)

# 提交到数据库执行
db.commit()

# 关闭
cursor.close()
db.close()

