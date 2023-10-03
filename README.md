### 新增flask_專案及repo
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