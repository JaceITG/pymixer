from video import render
import os, sys
import utils
import yt_dlp as youtube_dl


def download(title, index):
    opts = utils.ydl_opts.copy()
    opts['outtmpl'] = f"songs/{index} {title}.%(ext)s"

    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([title])

if __name__ == "__main__":

    playlist = "playlist.txt"
    skip_dl = False

    args = sys.argv

    if "-s" in args:
        skip_dl = True
        args.remove('-s')

    if len(args) > 1:
        playlist = args[1]
    
    with open('data/'+playlist, 'r') as f:
        song_titles = [l.strip() for l in f.readlines()]

    if not skip_dl:
        print("Downloading songs:")
        for s in song_titles:
            print(f"\t~{s}")

        for i in range(len(song_titles)):
            download(song_titles[i], i)


    #Validate all songs were downloaded
    songs_dir = os.listdir('songs')

    missing = False
    downloaded_indices = [int(e[:e.index(' ')]) for e in songs_dir]

    for i in range(len(song_titles)):
        if i not in downloaded_indices:
            print(f"Missing song download for {song_titles[i]}")
            missing = True
    
    if missing:
        input("Place missing audio files in songs directory and press enter...")
    
    #get updated song dir and prepend folder path
    songs_dir = os.listdir('songs')
    song_fps = ['songs/'+s for s in songs_dir]

    render('data/thumb.png', song_fps)

    if not utils.render_opts['keep_mp3s']:
        for e in songs_dir:
            os.remove('songs/' + e)
    
