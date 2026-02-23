from transformers import pipeline
from PIL import Image
import cv2

class BodyModel:
    def __init__(self, model_name="google/vit-base-patch16-224"):
        self.pipe = pipeline("image-classification", model=model_name)

    def analyze(self, frame):
        # Convert OpenCV BGR frame → RGB → PIL
        if isinstance(frame, (list, tuple)) or hasattr(frame, "shape"):  
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)

        # Run the pipeline
        results = self.pipe(frame)

        # Take top prediction
        top = results[0]
        impact = top["score"] * 10
        gesture = top["label"]

        return impact, gesture
