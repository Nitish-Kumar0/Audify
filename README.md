# Audify
## Overview
A web application that converts videos in various formats to audio with the ability to add
comments at specific timestamps.
<br/>
<br/>
## Description
- This website is capable of extracting audio from uploaded videos or links.
   - Uploaded from device and can be given in any video file format like .mp4 or .mo9
   - Given in the form of a video link ( It can be a YouTube video link or a Facebook video link or a Twitch stream link).
- It has User Authentication.
- Users can view their previous uploads.
- In addition to that they can also add captions to audio at specific timestamps.
<br/>
<br/>
**Tech StackFrameworks:**
  <br/>
- Frontend : HTML CSS JS
- Backend : Python (Django)
- Databasee : SQLite
<br/>
<br/>
### Necessary libraries to install for the above code:
<br/>
- Django
    - use command "pip install django"
- Pytube
    - use command "pip install pytube"
    - there is a small bug in pytube which makes it unable to extract video given a youtube link you can resolve it by refer this [Fix](https://pages.github.com/](https://github.com/pytube/pytube/issues/1678)https://github.com/pytube/pytube/issues/1678).
- Youtube-dl
    - use command "pip install youtube_dl"
- Moviepy
    - use command "pip install moviepy"
- Pydub
    - use command "pip install pydub"
- Mutagen
    - use command "pip install mutagen"
- FFMPEG
    - refer this [guide](https://ffmpeg.org/about.html)
