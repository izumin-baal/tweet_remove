# tweet_remove
Twitterのツイート削除用API

## 必要パッケージのインストール
```
pip install -r requirements.txt
```

## TweetのIDを取得する
- Twitterの設定よりデータのアーカイブを申請し、アーカイブデータをDLする
- アーカイブデータの`tweet-headers.js`を下記のようなJSONに変更して拡張子もJSONに変更する
```
{
  "data": [
    {
      "tweet": {
        "tweet_id": "XXXXXXXXXXXX",
        "user_id": "XXXXXXXXXXXX",
        "created_at": "Wed May 24 13:26:05 +0000 2023"
      }
    },
    {
      "tweet": {
        "tweet_id": "XXXXXXXXXXXX",
        "user_id": "XXXXXXXXXXXX",
        "created_at": "Tue May 23 14:25:43 +0000 2023"
      }
    }
  ]
}
```

## .env
- 削除したいアカウントのTwitterのDevelop Pageより利用の申請をし、API用のappを作成しTokenを入手する。
- 必要なのは下記の四つ
```
API_KEY="XXXXXXXXXXX"
API_KEY_SECRET="XXXXXXXXXXX"
ACCESS_TOKEN="XXXXXXXXXXX"
TOKEN_SECRET="XXXXXXXXXXX"
```

## 実行
- APIで50ツイートが削除される。
- Freeプランでのツイート削除APIの上限が50/day
- cronやらfunctionやらで適当に毎日動かしておけば良い
```
python3 delete.py
```