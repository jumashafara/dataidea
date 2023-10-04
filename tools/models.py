from django.db import models

# Create your models here.
class Transcription(models.Model):
    audio_file = models.FileField(upload_to='audio_files/')
    transcription_text = models.TextField(blank=True)
    summary_text = models.TextField(blank=True)

    def __str__(self):
        return self.audio_file