import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from gura.buffer import ByteBuffer

#DURATION = 0.01
SAMPLE_FREQ = 44100
NSAMPLE = 1024#int(DURATION * SAMPLE_FREQ)

pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paFloat32,
                 channels=1,
                 rate=44100,
                 input=True,
                 frames_per_buffer = NSAMPLE)
stream.start_stream()

# We keep multiple windows in a buffer for smoothness
IN_BUFFER = 8*NSAMPLE
buf = ByteBuffer(4*IN_BUFFER) # because float32

# Only show the lower parts of the fourier
NFREQ = 200
freqs = np.fft.rfftfreq(IN_BUFFER, 1/SAMPLE_FREQ)[:NFREQ]

# Setup graphics
fig, ax = plt.subplots()
line, = ax.plot(freqs, 0*freqs)
ax.axis([0, np.max(freqs), 0, 100])

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(freqs))
    return line,

def animate(i):
    # stream.read blocks until we have enough points
    buf.push(stream.read(NSAMPLE))
    data = np.frombuffer(buf.get(), dtype=np.float32)
    f = np.abs(np.fft.rfft(data))
    line.set_ydata(f[:NFREQ])
    return line,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=1, blit=True, save_count=50)

plt.show()
stream.stop_stream()
print("Finished")
