import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


N = int(44100*0.1)

pa = pyaudio.PyAudio()

pa.get_default_input_device_info()

stream = pa.open(format=pyaudio.paFloat32,
                 channels=1,
                 rate=44100,
                 input=True,
                 frames_per_buffer = N)

stream.start_stream()
raw = stream.read(N)
data = np.frombuffer(raw, dtype=np.float32)
stream.stop_stream()

np.save('sound.data', data)

print("Finished")
