import moviepy.editor as ed
import moviepy.video.VideoClip as vd
import moviepy.audio.io.AudioFileClip as au
import moviepy.audio.AudioClip as aucomp

from utils import render_opts

def render(bg, audio_clips, opts=render_opts):
    #TODO: render onscreen elements like audio visualizer or song info
    video = vd.ImageClip(bg)

    clips = [au.AudioFileClip(c) for c in audio_clips]

    desc = []

    #TODO: normalize audio volume? trim quiet intro/outro?
    end = 0
    for i in range(len(clips)):

        #extract song name
        name = clips[i]
        name = name[name.index((' '))+1:name.rindex('.')]

        #build description
        time = end
        hours = time//3600
        time -= hours*3600
        minutes, seconds = time//60, time%60

        desc.append(f"{hours:02}:{minutes:02}:{seconds:02} // {name}")

        clips[i] = clips[i].set_start(end)
        end += clips[i].duration + 0.5
    
    #remove padded hours from timestamps if last video starts before one hour
    if end - clips[-1].duration < 3600:
        desc = [t[t.index(':')+1:] for t in desc]
    

    audio_track = aucomp.CompositeAudioClip(clips)
    video = video.set_audio(audio_track)
    video = video.set_duration(end)
    video.write_videofile('data/generated.mp4', fps=1, codec='libx264')

    print("Done rendering video: ")
    print('\n'.join(desc))

    if render_opts['desc_file']:
        with open('data/description.txt', 'w') as f:
            f.write('\n'.join(desc))

if __name__ == "__main__":
    render('data/thumb.png', ['data/alone.mp3', 'data/beautiful.mp3'])
