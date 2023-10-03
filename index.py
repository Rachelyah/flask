from flask import Flask #我從flask套件，import帶入一個Flask
from flask import render_template

app = Flask(__name__) #__name__是網頁名稱 #app是flask應用程式的實體
@app.route("/") 
def index(): #方法叫做index，也就是我的首頁
    return render_template("index.html") #傳回我templats資料夾中的index網頁