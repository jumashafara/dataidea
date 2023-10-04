from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:pk>/<str:option>/', views.download_transcription, name='download_transcription'),
]
