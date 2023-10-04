import os
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from .models import Transcription
from .forms import AudioUploadForm, TranscriptionOptionsForm
import assemblyai as aai

aai.settings.api_key = f"3282ce6eca0a47519f6f69dbbaa38da6"

def upload_file(request):
    if request.method == 'POST':
        audio_form = AudioUploadForm(request.POST, request.FILES)
        options_form = TranscriptionOptionsForm(request.POST)

        if audio_form.is_valid() and options_form.is_valid():
            audio_file = audio_form.cleaned_data['audio_file']
            transcript_option = options_form.cleaned_data['transcript_option']

            # Save the uploaded audio file
            transcription = Transcription(audio_file=audio_file)
            transcription.save()

            # Transcribe the audio file
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(
            data=transcription.audio_file.path,
            config= aai.TranscriptionConfig(
                summarization= True,
                summary_model=aai.SummarizationModel.informative,
                summary_type=aai.SummarizationType.bullets
            ))
            
            transcription.summary_text = transcript.summary
            transcription.transcription_text = transcript.text
            # Save transcription
            transcription.save()


            return redirect(to='download_transcription', 
                            pk=transcription.pk, 
                            option='text' if transcript_option == 'text' else 'summary')
            



    else:
        audio_form = AudioUploadForm()
        options_form = TranscriptionOptionsForm()

    return render(request, 'tools/upload.html', {'audio_form': audio_form, 'options_form': options_form})

def download_transcription(request, pk, option):
    transcription = Transcription.objects.get(pk=pk)
    response = HttpResponse(content_type='text/plain')

    if option == 'text':
        response['Content-Disposition'] = f'attachment; filename="transcription_text.txt"'
        response.write(transcription.transcription_text)
    else:
        response['Content-Disposition'] = f'attachment; filename="transcription_summary.txt"'
        response.write(transcription.summary_text)
    return response
