import cv2
from camera import Camera
from detector import Detector
from env_metrics import EnvMetrics
from scoring import Scorer
from logger import Logger
from overlay import Overlay

def main():
    # Initialize all modules
    cam = Camera()
    # Ensure 'best.pt' exists in your folder or update path
    detector = Detector(model_path='best.pt') 
    env = EnvMetrics()
    scorer = Scorer()
    logger = Logger()
    overlay = Overlay()

    print("Starting Study Environment Assessment System...")
    
    # 62. Run in continuous loop [cite: 62]
    while True:
        # 1. Capture frame [cite: 55]
        frame = cam.get_frame()
        if frame is None:
            break

        # 2. Run detection [cite: 56]
        detections, counts = detector.detect(frame)

        # 3. Compute environmental metrics [cite: 57]
        brightness, glare = env.analyze(frame)

        # 4. Compute score [cite: 58]
        score, status = scorer.calculate_score(counts, brightness, glare)

        # 5. Draw overlay [cite: 59]
        frame = overlay.draw(frame, detections, brightness, glare, score, status)

        # 6. Show live video window [cite: 60]
        cv2.imshow("Study Env Assessment", frame)

        # 7. Log data to CSV [cite: 61]
        # (Optional: Add a delay or log every N frames to avoid massive CSVs)
        logger.log(counts, brightness, glare, score, status)

        # 9. Exit safely with key press 'q' [cite: 63]
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()