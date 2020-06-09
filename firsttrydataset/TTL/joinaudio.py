from pydub import AudioSegment
combined = AudioSegment.empty()
for n in range(1, 30):
    path = 'TTL_{}.wav'
    print(path.format(n))
    realpath = path.format(n)
    sound = AudioSegment.from_wav(realpath)
    combined += sound

combined.export("s7.wav", format="wav")

