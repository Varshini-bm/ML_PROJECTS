import cv2
import numpy as np
from colorama import Fore, Style, init
from models.speech_model import SpeechModel
from models.tone_model import ToneModel
from models.body_model import BodyModel
from utils import start_audio, stop_audio, init_camera, calculate_scores

init(autoreset=True)

# Initialize models
speech_model = SpeechModel()
tone_model = ToneModel()
body_model = BodyModel()

# Initialize camera
cap = init_camera()

# Global state
running = False
full_transcription = ""
audio_chunk = np.array([])

def process_audio(audio):
    """Process finalized audio chunk and return all metrics"""
    if audio.size == 0:
        return "", 0.0, 0.0, "Neutral"
    
    # Transcription
    text = speech_model.transcribe(audio)
    
    # Tone/Emotion
    confidence_score, tone_label = tone_model.analyze(audio)
    
    # Simple clarity metric: words per second
    clarity_score = min(len(text.split()) / 2.0, 10.0)
    
    return text, clarity_score, confidence_score, tone_label

print(Fore.LIGHTGREEN_EX + "Press 's' to START analysis, 'e' to STOP, 'q' to QUIT." + Style.RESET_ALL)

while True:
    ret, frame = cap.read()
    if not ret:
        print(Fore.RED + "❌ Camera feed lost!" + Style.RESET_ALL)
        break

    # Overlay instructions on camera
    cv2.putText(frame, "Press 's'=START, 'e'=STOP, 'q'=QUIT", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 2)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s') and not running:
        start_audio()
        running = True
        print(Fore.GREEN + "▶️ Analysis STARTED" + Style.RESET_ALL)

    elif key == ord('e') and running:
        audio_chunk = stop_audio()
        running = False
        print(Fore.YELLOW + "⏹ Analysis STOPPED" + Style.RESET_ALL)

        # Analyze audio and video once after stop
        text, clarity, confidence, tone = process_audio(audio_chunk)
        full_transcription += text + " "

        impact, body_label = body_model.analyze(frame)

        scores = calculate_scores(clarity, confidence, impact)

        # Terminal output
        print(Fore.MAGENTA + "\n[HOLO-ANALYSIS REPORT]" + Style.RESET_ALL)
        print(Fore.CYAN + f"🗣️ Clarity: {scores['Clarity']:.2f}/10")
        print(Fore.YELLOW + f"🎵 Confidence: {scores['Confidence']:.2f}/10 [{tone}]")
        print(Fore.GREEN + f"👤 Impact: {scores['Impact']:.2f}/10 [{body_label}]")
        print(Fore.LIGHTWHITE_EX + f"🌐 Overall: {scores['Overall']:.2f}/10")
        print(Fore.BLUE + f"💬 Transcript: " + Style.RESET_ALL + f"{full_transcription[-200:]}...")

    elif key == ord('q'):
        if running:
            stop_audio()
        print(Fore.RED + "🛑 Exiting HOLO-SESSION..." + Style.RESET_ALL)
        break

    # Live camera feed
    cv2.imshow("HOLO INTERFACE", frame)

cap.release()
cv2.destroyAllWindows()
