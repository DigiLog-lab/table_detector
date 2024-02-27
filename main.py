#Flaskのライブラリをインポート
from flask import Flask, render_template, request, redirect, url_for, flash
import detector


#Flaskオブジェクトの生成
app = Flask(__name__)

#urlのルーティングを作成
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    if request.method=='POST':
        # フォームから送られたデータを取得
        img = request.files['img']
        # detector.pyのtable_detection関数を呼び出し
        result = detector.table_detection(img)
        return render_template('result.html', result=result)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)


    

