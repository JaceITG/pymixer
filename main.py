from video import render
import multiprocessing, os
import utils
import yt_dlp as youtube_dl


def download(title, index):
    opts = utils.ydl_opts.copy()
    opts['outtmpl'] = f"songs/{index} {title}.%(ext)s"

    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([title])

if __name__ == "__main__":
    
    with open('data/playlist.txt', 'r') as f:
        song_titles = [l.strip() for l in f.readlines()]

    print("Downloading songs:")
    for s in song_titles:
        print(f"\t~{s}")

    for i in range(len(song_titles)):
        download(song_titles[i], i)


    #Validate all songs were downloaded
    songs_dir = os.listdir('songs')

    last = -1
    missing = False
    for e in songs_dir:
        if not (int(e[:e.index(' ')]) == last+1):
            print(f"Missing song download for {song_titles[last+1]}, please retreive manually.")
            missing = True
        
        last += 1
    
