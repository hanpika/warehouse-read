from flask import Flask,send_file
import os
app = Flask(__name__)

PATH = os.path.join(os.path.dirname(__file__),'file')

@app.route("/")
def main():
    return app.send_static_file("index.html") 

@app.route("/file/<path:filename>")
def name(filename):#关键函数
    if os.path.isdir(PATH+"/"+filename):
        file = os.listdir(PATH+"/"+filename)
        re = "<p>目录</p>"
        for i in file:
            re = re +"<a href='/file/"+filename+"/"+str(i)+"'>"+ str(i) + "</a>" + "<br>"
        return str(re)

    return send_file(PATH+"/"+filename)

if __name__ == "__main__":
    app.run("127.0.0.1",80)#运行后直接访问127.0.0.1可查看使用教程与快捷测试，如果不是从127.0.0.1开始访问的，出现任何问题我不负责