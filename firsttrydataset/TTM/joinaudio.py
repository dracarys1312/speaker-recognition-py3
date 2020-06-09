from pydub import AudioSegment
combined = AudioSegment.empty()
for n in range(1, 30):
    path = 'TTM_{}.wav'
    print(path.format(n))
    realpath = path.format(n)
    sound = AudioSegment.from_wav(realpath)
    combined += sound

combined.export("s6.wav", format="wav")

