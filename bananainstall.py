# coding=utf-8
# 生成配置文件
import time
import sys
import sqlite3

client_config=\
'''[server type]
type=client

# 客户端默认配置
[client]
# 客户端ID
client_id=%s
# 服务端IP
server_ip=127.0.0.1
# 数据发送端口
server_port=5000
# 发送间隔
second=1'''

server_config=\
'''[server type]
type=server

# 服务端默认配置
[service]
# 内存CPU报警阀值
alarm=60
# 数据接收端口
data_port=5000
# web服务端口
web_port=5001'''

def client_install():
    id = str(int(round(time.time(),3)*1000))
    with open('banana.conf','w',encoding='utf-8') as f:
        f.write(client_config%id)

def server_install():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE realtime
             (Id TEXT primary key, 
             Sysinfo TEXT, 
             Ip TEXT, 
             UpdateTime TEXT, 
             mem TEXT,
             cpu REAL, 
             net TEXT, 
             label TEXT, 
             message TEXT)''')

    c.execute('''CREATE TABLE history
             (UpdateTime TEXT primary key, 
             mem TEXT, 
             cpu REAL, 
             net TEXT)''')

    conn.commit()
    conn.close()
    with open('banana.conf','w',encoding='utf-8') as f:
        f.write(server_config)


if __name__=='__main__':
    install_type = sys.argv[1]
    if install_type == 'client':
        client_install()
    elif install_type == 'server':
        server_install()
    else:
        print('[option error]\n client \n server ')





