import numpy as np

def calculate_scores(clarity, confidence, impact):
    overall = np.mean([clarity, confidence, impact])
    return {
        "Clarity": clarity,
        "Confidence": confidence,
        "Impact": impact,
        "Overall": overall
    }
