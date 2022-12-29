import pyaudio
import wave
from aip import AipSpeech
import os
import sys
import io

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav"

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
AppID = "25496064"
APIKey = "A6fXM6nA1B8GY2txDIUCXYyu"
SecretKey = "4qb3jX1C8ue1rhwMkp27kzmrxLTli9G8" 
client=AipSpeech(AppID,APIKey,SecretKey)

voice=client.synthesis("你好，你要吃什么",'zh',6,{'vol':15,'per':3,'spd':5})
with open("ask.mp3",'wb') as fp:
    fp.write(voice)
voice=client.synthesis("我没听懂你在说什么",'zh',6,{'vol':15,'per':3,'spd':5})
with open("error.mp3",'wb') as fp:
    fp.write(voice)

os.system("ask.mp3")

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
stream.start_stream()
print("* 请说，我在听......")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
stream.stop_stream()
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

with open('audio.wav', 'rb') as fp:
        wave=fp.read()

print("识别中......",len(wave))
result = client.asr(wave, 'wav', 16000, {'dev_pid':1536})
print(result)
if result["err_no"] == 0:
    for t in result["result"]:
        print(t)
else:
    print("对不起，识别失败\n",result["err_no"])
    os.system("error.mp3")

if result["err_no"] == 0:
    dish = result[4:]
voice=client.synthesis(dish+"很简单，跟我一起学吧",'zh',6,{'vol':15,'per':3,'spd':5})
with open("tmp.mp3",'wb') as fp:
    fp.write(voice)
os.system("tmp.mp3")
