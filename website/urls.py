from django.urls import path
from .views import index, timeline

urlpatterns = [
    path("", index, name="index"),
    path("timeline", timeline, name="index"),
]