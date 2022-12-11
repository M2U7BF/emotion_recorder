from django.urls import path
from .views import index, timeline, analysis

urlpatterns = [
    path("", index, name="index"),
    path("timeline", timeline, name="index"),
    path("analysis", analysis, name="analysis"),
]