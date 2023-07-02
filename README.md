# Audify

## Overview
Audify is a web application that allows users to convert videos in various formats to audio files and add comments at specific timestamps.

## Description
This web application provides the following features:
- Conversion of uploaded videos or video links to audio files.
  - Users can upload videos from their devices in any video file format, such as .mp4 or .mov.
  - Video links from platforms like YouTube, Facebook, or Twitch can also be provided.
- User authentication for secure access.
- View and manage previous uploads.
- Add captions or comments to audio files at specific timestamps.

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Django)
- Database: SQLite

## Necessary Libraries
The following libraries need to be installed to run the code:
- Django: Use the command `pip install django`.
- Pytube: Use the command `pip install pytube`. Please note that there is a small bug in pytube related to extracting videos from YouTube links. You can refer to this [fix](https://github.com/pytube/pytube/issues/1678) for resolving the issue.
- Youtube-dl: Use the command `pip install youtube_dl`.
- Moviepy: Use the command `pip install moviepy`.
- Pydub: Use the command `pip install pydub`.
- Mutagen: Use the command `pip install mutagen`.
- FFMPEG: Refer to this [guide](https://ffmpeg.org/about.html) for installation instructions.

Please make sure to install these libraries before running the code.

## Instructions
1. Clone this repository to your local machine.
2. Install the necessary libraries as mentioned above.
3. Run the Django server using the command `python manage.py runserver`.
4. Access the web application through your web browser by visiting `http://localhost:8000`.

Enjoy using Audify and convert your videos to audio with ease!
