import pyaudio
import numpy as np
from time import time, sleep

DURATION = 0.05
SAMPLE_FREQ = 44100
NSAMPLE = int(DURATION * SAMPLE_FREQ)

pa = pyaudio.PyAudio()

pa.get_default_input_device_info()

t = time()
def callback(data, frames, time_info, flags):
    global t
    print(time() - t, "there came", frames)
    t = time()
    return (None, pyaudio.paContinue)

stream = pa.open(format=pyaudio.paFloat32,
                 channels=1,
                 rate=44100,
                 input=True,
                 stream_callback=callback,
                 start=True)


while stream.is_active():
    sleep(1)
stream.close()
pa.terminate()
