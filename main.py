from video import render
import youtube_dl, multiprocessing
import utils


def download(title):
     
    with youtube_dl.YoutubeDL(utils.ydl_opts) as ydl:
        ydl.download([title])

if __name__ == "__main__":
    download("Masayoshi Takanaka - ALONE")
    download("Hikaru Utada - Beautiful World")
    #render('thumb.png', ['alone.mp3', 'beautiful.mp3'])
