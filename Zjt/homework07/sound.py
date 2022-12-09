from aip import AipSpeech
from subprocess import Popen
import pyaudio
import wave

APP_ID = '28605023'
API_KEY = "DLOby1QMvU4vV4bxEC1G26FG"
SECRET_KEY = "tZaaFOaAtvU4FEkSNORtS7XHDv73BW4e" 

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5

def Sound_Get(filename):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    stream.start_stream()
    print("* 开始录音......")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    print("* 录音结束......")

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def Sound_S2T(filename):
    client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
    with open(filename, 'rb') as fp:
        wave=fp.read()

    result = client.asr(wave, 'wav', 16000, {'dev_pid':1537})
    if result["err_no"] == 0:
        for t in result["result"]:
            return t
    else:
        print("没有识别到语音\n",result["err_no"])
        return ""

def Sound_T2S(order,filename):
    client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
    content = order
    voice = client.synthesis(content,'zh',6,{'vol':15,'per':3,'spd':5})
    if not isinstance(voice, dict):
        with open(filename+".mp3",'wb') as fp:
            fp.write(voice)
        fp.close()
        return True
    else:
        print(voice)
        return False

def Sound_Play(filename):
    Popen(filename+".mp3",shell=True)  

