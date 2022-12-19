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

def length(info, *, incomplete):
    duration = info.get('duration')
    if duration and duration > 600:
        return 'Video Too Long, skipping'

ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': None,
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'default_search': 'ytsearch',
        'match_filter': length,
    }

render_opts = {
    'desc_file': True,
}