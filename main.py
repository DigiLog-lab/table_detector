#Flaskのライブラリをインポート
from flask import Flask, render_template, request, redirect, url_for, flash

#Flaskオブジェクトの生成
app = Flask(__name__)

#urlのルーティングを作成
@app.route('/')
def index():
    return render_template('index.html')


    

