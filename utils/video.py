import cv2

def init_camera(index=0):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError("❌ Could not open webcam")
    return cap

