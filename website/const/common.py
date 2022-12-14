# from . import works, activities, study, vision

# 全般
from website.models import Emotion


app={
    "title": "きもちレコーダー"
}
# TODO page.titleとする
title={
    "index": "トップページ",
    "timeline": "過去データ一覧画面",
    "analysis":"分析画面"
}

placeholder={
    "emotion_description": " "*5+"きもちの原因を記入"
}

text={
    "select_emotion" : "感情を選択",
    "emotion_description" : "くわしく",
    "copy_right": "© : 2022 | AllRights Reserved.",
    "placeholder": placeholder
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