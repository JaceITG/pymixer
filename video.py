import moviepy.editor as ed
import moviepy.video.VideoClip as vd
import moviepy.audio.io.AudioFileClip as au
import moviepy.audio.AudioClip as aucomp

def render(bg, audio_clips):
    video = vd.ImageClip(bg)

    clips = [au.AudioFileClip(c) for c in audio_clips]

    #TODO: normalize audio volume? trim quiet intro/outro?
    end = 0
    for i in range(len(clips)):
        clips[i] = clips[i].set_start(end)
        end += clips[i].duration + 0.5

    audio_track = aucomp.CompositeAudioClip(clips)
    video = video.set_audio(audio_track)
    video = video.set_duration(end)
    video.write_videofile('data/generated.mp4', fps=1, codec='libx264')

if __name__ == "__main__":
    render('data/thumb.png', ['data/alone.mp3', 'data/beautiful.mp3'])
