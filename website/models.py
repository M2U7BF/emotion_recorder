from django.db import models

class Emotion(models.Model):
    emotion_name = models.CharField(max_length=50)
    emotion_type = models.CharField(max_length=50)
    emotion_point = models.SmallIntegerField()

class EmotionRecords(models.Model):
    emotion_id = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    emotion_cause = models.CharField(max_length=200)
    entered_at = models.DateTimeField('date entered')
