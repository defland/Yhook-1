# coding:utf-8
from flask import Flask,request
app = Flask(__name__)

import commands,os

# 全局变量
DEV_PROJECT_PATH = '/Users/yg/Documents/code/Project/Yhook'
D_PROJECT_PATH = '/Users/yg/Documents/code/Project/leanroom'
WEB_PROJECT_PATH = '/home/yg/www/leanroom/'


# 接受到消息
@app.route('/',methods=['POST','GET'])
def webhook():

    if request.method == "GET":
        return "pelase use POST"

    x = request.form
    pull_code()
    print x
    x = str(x)
    return 'Receive successful %s ' % x

# 拉取gitpull
def pull_code():

    # 执行
    # cd /home/yg/www/leanroom/
    # git reset --hard
    # git pull

    comm = 'cd %s && ls -l && git status && git reset --hard && git pull' % WEB_PROJECT_PATH
    print comm
    (status, output) = commands.getstatusoutput(comm)
    print status, output
    
    # (status, output) = commands.getstatusoutput('pwd')
    # print status, output
    
    # (status, output) = commands.getstatusoutput('git add . ')
    # print status, output
    

    # (status, output) = commands.getstatusoutput('git commit -m "added:test"') 
    # print status, output


# 重启服务器
def restart_server():

    pass


if __name__ == '__main__':
   
    app.run()

