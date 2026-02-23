from transformers import pipeline

class ToneModel:
    def __init__(self, model_name="superb/wav2vec2-base-superb-er"):
        self.pipe = pipeline("audio-classification", model=model_name)

    def analyze(self, audio):
        results = self.pipe(audio)
        top = results[0]
        confidence = top["score"] * 10
        return confidence, top["label"]
