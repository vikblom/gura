import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sys import getsizeof

from gura.buffer import ByteBuffer

N = int(44100*0.05)

pa = pyaudio.PyAudio()
pa.get_default_input_device_info()
stream = pa.open(format=pyaudio.paFloat32,
                 channels=1,
                 rate=44100,
                 input=True,
                 frames_per_buffer = N)
stream.start_stream()

IN_BUFFER = 5*N
buf = ByteBuffer(4*IN_BUFFER) # because float32

fig, ax = plt.subplots()
x = np.linspace(0, 1, IN_BUFFER)
line, = ax.plot(x, np.sin(x))
ax.axis([0, 1, -.1, .1])

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,


def animate(i):
    buf.push(stream.read(N))
    #print(len(buf), len(buf._buf), len(x))
    line.set_ydata(np.frombuffer(buf.get(), dtype=np.float32))
    return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=0.1, blit=True, save_count=50)


plt.show()
stream.stop_stream()
print("Finished")
