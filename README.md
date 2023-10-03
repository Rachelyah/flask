### 新增flask_專案及repo
- 建立python web server的程式有兩種：flask、django
- flask就是連結python跟網頁的結合

### 在VS CODE一次開啟兩個專案資料夾
- 將資料夾新增至工作區＞開啟兩個想要的資料夾＞兩個專案的虛擬環境跟套件各自獨立
- 新的flask檔案，透過終端機git init新增.git檔案
- 建立index.py檔案
- 新增README檔案
- 建立虛擬環境(名字可以自己取)、.gitinore檔案裡面放虛擬環境資料夾名稱
- (.的意思在linux代表隱藏的資料夾意思，未來上傳到雲端95%都使用linux)
- 透過終端機，用GitHub cli功能新增一個repo資料夾
```
gh repo create flask --public --source=. --remote=origin
```
- [GitHub cli的語法忘記可以查這邊](https://cli.github.com/)

### 在虛擬環境下載套件Falsk
- 新增requirement.txt 裡面寫你下載的套件：套件名稱==版本(為避免執行錯誤版本也可以不要寫)
- 直接在虛擬環境裡，執行requirement.txt檔案內的套件下載
- 備註：軟體版本怎麼查？去pypi查，所有的套件都會在那邊更新
- [pypi](https://pypi.org/project/Flask/)
```
pip install -r requirements.txt
```

### 建立最小的應用程式
- [在flask官網內看程式碼](https://flask.palletsprojects.com/en/3.0.x/)
- 輸入最小的應用程式代碼
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
- 透過終端機執行，執行代碼
- return裡面的字串，就已經是html語法，顯示網頁中的內容

```
$ flask --app hello run #hello是自己的檔名
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```
- 會run出一個結果，並且出現你現在網頁的網址
- 如果按ctrl+c就會離開執行狀態

- Debug mode:off #代表我不會即時更新python上面修改的結果
- 即時更新修改結果到網頁上：關掉執行狀態，重新執行並加入：
```
$ flask --app index run --debug
```

### 在網頁上查看編輯狀態
- chrome瀏覽器：右邊功能＞開發人員工具＞就可以看到你在python檔案上編輯的html語法

### 透過flask跑我的頁面、並註冊更多頁面
```
@app.route("/") ＞app裡面有一個實體方法，其實不是方法，是註冊
def index():    
    return:<h1>hello</h1>
```
- route代表註冊route()->decorate，要註冊要加@
- /是根目錄，後面可以加上其他我要去的路徑

```
@app.route("hello_world")
def hello_world():
    return:<h1>hello</h1>
```
- 同上面註冊的方法，我再註冊一個叫做hello_world的分頁
- 原本的起始網址，我再/hello_world就可以過去
- 網址裡面有寫:5000，代表虛擬執行的狀態，如果是線上的網頁會是:80

### 透過新增樣板把html掛上
```
from flask import render_template
```
- 我今天使用了這個flask的render_template
- 所以我創立一個templates資料夾，裡面可以放css、圖片等靜態圖片
- 但是要透過template的語法連結(url...)

```
def index(): #方法叫做index，也就是我的首頁
    return render_template("index.html") 
```
- 我有一個index.html的首頁，我要透過py把它掛在網頁上
- ("index.html")是我的網頁名稱

### static files 是掛入圖片&連結css
- 在最外面新增static資料夾＞裡面建立css資料夾＞建立css頁面(index.css)
- 回到html，在body地方用link:css語法
    ```url_for('static', filename='style.css')```
- 套用static files的教學用法放入路徑，有兩種方式：絕對&相對路徑
    1. 相對路徑(前面要加兩個大括號，請參考語法模板Jinja)：
    ```href="{{url_for('static', filename='css/index.css')}}">```
    - 語法的模板：有一個日本人把它全部寫出來(真瘋)，可以參考
    - [Jinja-Template Designer Documentation](https://jinja.palletsprojects.com/en/3.1.x/)
    2. 絕對路徑：
    ```href="/static/css/index.css"```

### 使用Render工具把網頁變成正是可上線的網頁
[Render](https://dashboard.render.com/)
