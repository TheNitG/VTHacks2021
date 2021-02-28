# HippoHelper

## Inspiration
We wanted to improve the online learning experience for fellow Hokies and students in general. We wanted to use the Google Cloud Speech to Text API to help students further understand class content.

## What it does
HippoHelper allows users to upload audio files of video lectures and transcribes them. After the lectures are transcribed, the site displays key phrases and useful online resources related to the key phrases.

## How we built it
For the site, we used a Bootstrap template and modified it according to our design preferences. We used Flask for the server with Jinja templating and Google Cloud Speech to Text API for the transcription. We also utilized FFMPEG to convert media files to the needed format. 

## Challenges we ran into
- Converting media files to necessary formats for speech to text 
- Filtering out unnecessary words from the transcriptions
- Uploading media files from the site to Google Cloud for processing 
- Working with Flask 
- Making the website user friendly
- Hosting the site online

## Accomplishments that we're proud of
- Successfully extracts key phrases from media files
- Website look pretty
- Code is compatible with Google Cloud APIs

## What we learned
- Static sites are easier to host than dynamic sites
- How to use Google Cloud API for storing video files and speech to text
- How to use Flask for dynamic sites
- How to use Rake-NLTK for key phrase extraction

## What's next for HippoHelper
- Proper file submission through the site
- Improve algorithm for providing online resources 
- Storing submitted videos on the site

## How to use locally
Run: ```pip install -r requirements```
Then run: ```python main.py```

## Check out [Our Devpost](https://devpost.com/software/hippohelper)
