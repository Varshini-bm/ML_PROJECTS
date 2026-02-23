import sounddevice as sd
import numpy as np

# Global state
_stream = None
_buffer = []
fs = 16000

def callback(indata, frames, time, status):
    if status:
        print(status)
    _buffer.append(indata.copy())

def start_audio():
    """Start recording audio in the background"""
    global _stream, _buffer
    _buffer = []
    _stream = sd.InputStream(samplerate=fs, channels=1, callback=callback)
    _stream.start()
    print("🎙️ Recording started...")

def stop_audio():
    """Stop recording and return numpy array"""
    global _stream, _buffer
    if _stream is not None:
        _stream.stop()
        _stream.close()
        _stream = None
    audio = np.concatenate(_buffer, axis=0) if _buffer else np.array([])
    print("🛑 Recording stopped.")
    return np.squeeze(audio)
