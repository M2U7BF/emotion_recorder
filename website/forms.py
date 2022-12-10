from django.forms import ModelForm
from website.models import Emotion, EmotionRecords

class RecordEnterForm(ModelForm):
    """
    docstring
    """
    class Meta:
        model = EmotionRecords
        fields = ['emotion_id','emotion_cause','entered_at']