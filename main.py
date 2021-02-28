from flask import Flask, render_template, request
from related_mat import process_words
from transcript import transcribe_gcs
import os
from google.cloud import storage


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", words=process_words())


@app.route("/upload", methods=['POST'])
def upload():
    """Process the uploaded file and upload it to Google Cloud Storage."""
    uploaded_file = request.files.get('file')

    if not uploaded_file:
        return 'No file uploaded.', 400

    # Create a Cloud Storage client.
    gcs = storage.Client()

    # Get the bucket that the file will be uploaded to.
    bucket = gcs.get_bucket("gs://spotify-transcriber")

    # Create a new blob and upload the file's content.
    blob = bucket.blob(uploaded_file.filename)

    blob.upload_from_string(
        uploaded_file.read(),
        content_type=uploaded_file.content_type
    )

    os.system(f'ffmpeg -i {uploaded_file.filename} output.flac')
    transcribe_gcs(f'{uploaded_file.filename.replace(".mp4", ".flac")}')
    return render_template("index.html", words=process_words())


if __name__ == "__main__":
    app.run(debug=True)
