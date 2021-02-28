# Imports the Google Cloud client library
import os

from dotenv import load_dotenv
import google.cloud.speech as speech


load_dotenv()
TOKEN = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# The name of the audio file to transcribe
gcs_uri = "gs://spotify-transcriber/output.flac"


def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        language_code="en-US"
    )
    config.audio_channel_count = 2
    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=6000)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    with open('transcript.txt', 'w+') as file:
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            file.write(u"{} ".format(result.alternatives[0].transcript))
