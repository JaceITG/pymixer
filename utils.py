class MyLogger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
        'format': 'worst',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': None,
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'default_search': 'ytsearch',
        'match-filter': 'duration<600',
    }