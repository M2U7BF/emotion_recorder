import datetime
from django.shortcuts import render
from django.urls import reverse_lazy

from website.models import Emotion, EmotionRecords
from .const import common

def index(request):
    ctxt = common.PARAMS
    if request.method == "POST":
        data = request.POST
        emotion_id = data.get("emotion_id")
        emotion = Emotion.objects.get(pk=emotion_id)
        emotion_cause = data.get("emotion_description")
        now = datetime.datetime.now()

        emotion_record = EmotionRecords(emotion_id=emotion, emotion_cause=emotion_cause, entered_at=now)
        # emotion_record.emotion_cause = emotion_cause
        # emotion_record.entered_at = now

        emotion_record.save()
    return render(request, "index.html", ctxt)

def timeline(request):
    common.PARAMS["emotion_records"] = EmotionRecords.objects.all()
    ctxt = common.PARAMS
    return render(request, "timeline.html", ctxt)
