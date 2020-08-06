import pyaudio
import numpy as np
import matplotlib.pyplot as plt

pa = pyaudio.PyAudio()

pa.get_default_input_device_info()

stream = pa.open(format=pyaudio.paFloat32,
                 channels=1,
                 rate=44100,
                 input=True,
                 frames_per_buffer = int(44100*0.1))

stream.start_stream()
block = stream.read(int(1000))
stream.stop_stream()

array = np.frombuffer(block, dtype=float)
plt.plot(array[0:]); plt.show()
