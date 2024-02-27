#Flaskのライブラリをインポート
from flask import Flask, render_template, request, redirect, url_for, flash
import detector

#Flaskオブジェクトの生成
app = Flask(__name__)

#urlのルーティングを作成
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    if request.method == 'POST':
        # フォームから送られたデータを取得
        img = request.form['img']
        # detector.pyのtable_detection関数を呼び出し
        result = detector.table_detection(img)
        return render_template('result.html', result=result)


    

