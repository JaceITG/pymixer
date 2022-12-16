from video import render
import multiprocessing, sys
import utils
import yt_dlp as youtube_dl


def download(title, index):
    opts = utils.ydl_opts.copy()
    opts['outtmpl'] = f"data/{index} {title}.%(ext)s"
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


    #render('thumb.png', ['alone.mp3', 'beautiful.mp3'])
