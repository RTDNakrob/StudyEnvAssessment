import cv2
import numpy as np

class EnvMetrics:
    def __init__(self, glare_threshold=230):
        # 25. Use configurable thresholds [cite: 25]
        self.glare_threshold = glare_threshold

    def analyze(self, frame):
        # 22. Convert frame to grayscale [cite: 22]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 23. Compute brightness = mean grayscale intensity [cite: 23]
        brightness = np.mean(gray)
        
        # 24. Compute glare percentage [cite: 24]
        # Count pixels that are very bright (above threshold)
        glare_pixels = np.sum(gray > self.glare_threshold)
        total_pixels = gray.shape[0] * gray.shape[1]
        glare_percentage = (glare_pixels / total_pixels) * 100
        
        return brightness, glare_percentage