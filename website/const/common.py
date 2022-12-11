# from . import works, activities, study, vision

# 全般
from website.models import Emotion


app={
    "title": "きもちレコーダー"
}
# TODO page.titleとする
title={
    "index": "トップページ",
    "timeline": "過去データ一覧画面"
}
emotions=["ワクワク","のどか","怒り","悲しい","虚無"]

text={
    "select_emotion" : "感情を選択",
    "emotion_description" : "くわしく",
    "copy_right": "© : 2022 | AllRights Reserved."
}
error={
    "cannot_load_image":"画像が読み込めませんでした",
}

PARAMS ={
    "app": app,
    "title": title,
    "emotions": Emotion.objects.all(),
    "username": "kamei-apple-monster",
    "text": text,
    "error": error,
}