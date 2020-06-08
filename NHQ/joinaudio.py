from pydub import AudioSegment
combined = AudioSegment.empty()
for n in range(1, 30):
    path = 'NHQ{}.wav'
    print(path.format(n))
    realpath = path.format(n)
    sound = AudioSegment.from_wav(realpath)
    combined += sound

combined.export("s1.wav", format="wav")

