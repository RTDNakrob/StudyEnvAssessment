import cv2

class Camera:
    def __init__(self, source=0, width=1280, height=720):
        # 1. Open USB webcam [cite: 5]
        self.cap = cv2.VideoCapture(source)
        
        # 2. Set resolution [cite: 6]
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        
        if not self.cap.isOpened():
            raise ValueError("Could not open video source")

    def get_frame(self):
        # 3. Continuously capture frames [cite: 7]
        ret, frame = self.cap.read()
        
        # 5. Handle camera read failure [cite: 9]
        if not ret:
            print("Failed to grab frame")
            return None
            
        # 4. Return frame (timestamp handling can be done in main) [cite: 8]
        return frame

    def release(self):
        self.cap.release()