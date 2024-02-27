from google.cloud import vision
from google.cloud.vision import ImageAnnotatorClient
import pandas as pd
import os


def table_detection(img):
    #環境変数にあるcredintial_fileのパスを取得
    credential_path = os.environ['credintial_']
    #認証情報の設定
    client = vision.ImageAnnotatorClient.from_service_account_json(credential_path)
    #引数の画像をapiに送信
    content = img.read()
    response = client.text_detection(image=content)
    texts = response.text_annotations

    df = pd.DataFrame(columns=['locale', 'description'])

    for text in texts:
        df = df.append(
            dict(
                locale=text.locale,
                description=text.description
            ),
            ignore_index=True
        )

    return df.to_csv(index=False)
    

