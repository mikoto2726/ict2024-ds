import json
import requests
import pandas as pd

# URLへアクセスしてデータを取得
url = requests.get(
    "https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_information.json")
text = url.text

# 変換したいJSONファイルを読み込む
df_json = pd.read_json(text)

# ネスト（入れ子）構造になっている"data"という項目を展開する
df_data = pd.json_normalize(df_json['data'][0])

# JSONをCSVへ変換して文字コードをutf8で出力
df_data.to_csv("hellocycling_station.csv", encoding='utf8', index=False)
