import pyaudio
from google.cloud import speech # Google Cloud Speech to Text
import base64
import io
 
COMMANDS = "前後左右終"

RECORD_SECONDS = 3       # 録音時間（秒）
FORMAT = pyaudio.paInt16 # 録音フォーマット
CHANNELS = 1             # モノラル
RATE = 16000             # サンプルレート
CHUNK = 1024
 
def read():
    audio = pyaudio.PyAudio() #pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        frames_per_buffer=CHUNK)
 
    print ("recording...")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK, exception_on_overflow = False)
        frames.append(data)
 
    print ("finished")
 
    stream.close()
    audio.terminate()
    snddata = b''.join(frames)
 
# Instantiates a client
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=snddata)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ja-JP",
        )

# Detects speech in the audio data
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        for alt in result.alternatives:
            dir = alt.transcript[0]
            print(dir)
            if COMMANDS.find(dir) != -1:
                return dir
    return "止"
