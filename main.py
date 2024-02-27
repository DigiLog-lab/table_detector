#Flaskのライブラリをインポート
from flask import Flask, render_template, request, redirect, url_for, flash
#GoogleのAPIの認証関係のライブラリをインポート
from google.cloud import vision
from google.cloud.vision import types

#Flaskオブジェクトの生成
app = Flask(__name__)

def table_detection(img):
    #ディレクトリにある認証情報jsonファイルのパスを指定
    credential_path = 'verify_info/item-management-411810-25ad9e86f8f5.json'
    #認証情報の設定
    client = vision.ImageAnnotatorClient.from_service_account_json(credential_path)
    

