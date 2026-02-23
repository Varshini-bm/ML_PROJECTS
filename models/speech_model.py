from faster_whisper import WhisperModel

class SpeechModel:
    def __init__(self, model_size="small", device="cpu"):
        self.model = WhisperModel("tiny", device=device)

    def transcribe(self, audio):
        segments, _ = self.model.transcribe(audio, beam_size=5)
        text = " ".join([seg.text for seg in segments])
        return text
