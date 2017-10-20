# coding:utf-8
from flask import Flask,request
app = Flask(__name__)

import commands,os

# 全局变量

# learoom项目系统路径
PROJECT_A_PATH = '/home/yg/www/learoom/'
PROJECT_A_DEV_PATH = '/Users/yg/Documents/code/Project/learoom'

PROJECT_B_PATH = '/home/yg/server/Yhook'
PROJECT_B_DEV_PATH = '/Users/yg/Documents/code/Project/Yhook'


SYSTEMD_PROJECT_A = 'learoom.service' # web网站项目的自启动服务名称
SYSTEMD_PROJECT_B = 'yhook.service' # yhook的自启动服务名

# 负责项目A的消息接受,webhook的路径 域名:端口/learoom
@app.route('/',methods=['POST','GET'])
@app.route('/index',methods=['POST','GET'])
@app.route('/learoom',methods=['POST','GET'])
@app.route('/learoom/',methods=['POST','GET'])
def learoom():

    if request.method == "GET":
        return "pelase use POST"

    # x = request.form
    # print x
    # x = str(x)
    
    print "pull code ing ...."
    # 拉取代码和重启web服务
    comm = 'cd %s && ls -l && git status && git reset --hard && git pull' % PROJECT_A_PATH
    pull_code(comm)
    print "pull code done!"

    print "restart serve  ing ...."
    comm2 = 'sudo systemctl restart %s && sudo systemctl status %s'  % (SYSTEMD_PROJECT_A,SYSTEMD_PROJECT_A)
    restart_server(comm2)
    print "restart serve done!"

    return 'Receive successful' 

# 负责项目B的消息接受
@app.route('/yhook',methods=['POST','GET'])
@app.route('/yhook/',methods=['POST','GET'])
def yhook():

    if request.method == "GET":
        return "pelase use POST"

    # x = request.form
    # print x
    # x = str(x)
    
    # 拉取代码和重启web服务
    comm = 'cd %s && ls -l && git status && git reset --hard && git pull' % PROJECT_B_PATH # 同步项目代码
    pull_code(comm)
    
    comm2 = 'sudo systemctl restart %s && sudo systemctl status %s'  % (SYSTEMD_PROJECT_B,SYSTEMD_PROJECT_B) #  重启服务
    restart_server(comm2)

    return 'Receive successful' 




# 拉取gitpull
def pull_code(comm=''):

    # 执行
    # cd /home/yg/www/leanroom/
    # git reset --hard
    # git pull

    print comm
    (status, output) = commands.getstatusoutput(comm)
    print status, output


# 重启服务器
def restart_server(comm=''):


    print comm
    (status, output) = commands.getstatusoutput(comm)
    print status, output


if __name__ == '__main__':
   
    app.run()

