from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name = "home"),
    path("recommendation",views.recommendation,name = "recommendation"),
    path("songs",views.recommended_songs,name = "recommended_songs"),
    path("videos",views.recommended_videos,name = "recommended_videos")
]
