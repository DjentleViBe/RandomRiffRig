from pydub import AudioSegment

audio_1 = AudioSegment.from_wav("./Mixdown/1Open.wav")
audio_2 = AudioSegment.from_wav("./Mixdown/2Open.wav")
audio_3 = AudioSegment.from_wav("./Mixdown/3Open.wav")
audio_4 = AudioSegment.from_wav("./Mixdown/4Open.wav")
audio_5 = AudioSegment.from_wav("./Mixdown/5Open.wav")
audio_6 = AudioSegment.from_wav("./Mixdown/6Open.wav")
audio_7 = AudioSegment.from_wav("./Mixdown/7Open.wav")
audio_8 = AudioSegment.from_wav("./Mixdown/8Open.wav")
audio_9 = AudioSegment.from_wav("./Mixdown/9Open.wav")

audio_open = [audio_1, audio_2, audio_3,
              audio_4, audio_5, audio_6,
              audio_7, audio_8, audio_9]

def combineaudio(files_print):
    combined_audio = 0
    for k in range(len(files_print)):
        combined_audio += audio_open[int(files_print[k]) - 1]
    return combined_audio

def exportaduif(a, b, filename):
    a.export("./RESULTS/" + b + "/" + filename + ".wav", format="wav")

def exportaudiocombi(a, b, filename):
    a.export("./COMBI/" + b + "/" + filename + ".wav", format="wav")