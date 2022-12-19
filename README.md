# PyMixer
### A Youtube MP3 downloader and compiler designed to quickly assemble mixes of songs for my Youtube Channel

Uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) for download and [MoviePy](https://zulko.github.io/moviepy/) for rendering

## Requirements

A Python Installation >= 3.7.9

The dependencies listed in `requirements.txt`

## Preparing a Playlist

Create a playlist .txt with the desired songs in the `data` folder, in the form

` artist - song title`

separated by newlines.

## Options

Runtime options such as output framerate and description output can be adjusted in the `render_opts` dictionary within `utils.py`

## Running the Script

`python3 main.py`

After Download and Render:

![image](https://user-images.githubusercontent.com/44596843/208339729-f7bb79dc-b7fa-45e7-a9eb-967768d72bd4.png)

The generated video `generated.mp4` and optional description file `description.txt` will be in the data subfolder
