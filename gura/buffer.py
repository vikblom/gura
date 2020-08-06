

class ByteBuffer:
    def __init__(self, size):
        self._n = size
        self._buf = bytearray(self._n)

    def push(self, bs):
        if len(bs) > self._n:
            self._buf = bytearray(bs[-self._n:])
        else:
            self._buf[:len(bs)] = b''
            self._buf.extend(bs)

    def get(self):
        return self._buf

    def __len__(self):
        return self._n
