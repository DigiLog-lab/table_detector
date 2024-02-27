from google.cloud import vision
from google.cloud.vision import types
import os


def table_detection(img):
    #環境変数にあるcredintial_fileのパスを取得
    credential_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    #認証情報の設定
    client = vision.ImageAnnotatorClient.from_service_account_json(credential_path)