from django.shortcuts import render
from .features.spotify.filter import happy_songs,sad_songs,high_energy_songs,calm_songs,cheerful_songs,neutral_songs,disgust_songs
import random

emotion_to_songs = {
    "happy" : happy_songs,
    "sad" : sad_songs,
    "angry" : calm_songs,
    "fear" : cheerful_songs,
    "surprise" : high_energy_songs,
    "neutral" : neutral_songs,
    "disgust" : disgust_songs
}
 
emotion_passed = None


def home(request):
    return render(request , "moodify/home.html",{
        # "emotion" : get_emotion
    })

def recommendation(request):
    
    from .face_detection.testEmotionDetector import  em
    emotion = em 
    # emotion_passed = None
    print("Hello World")
    # emotion = "sad"
    global emotion_passed 
    emotion_passed = emotion

    return render(request , "moodify/recommendation.html",{
        "emotion" : emotion
    }) 

def recommended_songs(request):

    emotion = emotion_passed
    return render(request, "moodify/recommended_songs.html",{
        "songs_list" : emotion_to_songs[emotion], 
        "emotion" : emotion
    })

def recommended_videos(request): 
    return None  