from ultralytics import YOLO

class Detector:
    def __init__(self, model_path='best.pt'):
        # Load trained YOLOv11 model
        self.model = YOLO(model_path)

    def detect(self, frame):
        # Run detection on each frame
        results = self.model(frame, verbose=False)[0]
        
        detections = []
        counts = {
            "study_essential": 0,
            "study_support": 0,
            "non_study_clutter": 0,
            "distractor": 0
        }

        for box in results.boxes:
            # Output bounding boxes
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            
            # This will now be "distractor_smartphone", "study_essential_book", etc.
            full_label = self.model.names[int(box.cls[0])]
            
            # Dynamically figure out the main category by checking how the label starts
            main_category = None
            if full_label.startswith("study_essential"):
                main_category = "study_essential"
            elif full_label.startswith("study_support"):
                main_category = "study_support"
            elif full_label.startswith("non_study_clutter"):
                main_category = "non_study_clutter"
            elif full_label.startswith("distractor"):
                main_category = "distractor"

            detections.append({
                "bbox": (x1, y1, x2, y2),
                "label": full_label,       
                "main_category": main_category,
                "conf": conf
            })

            # Count objects per main category
            if main_category in counts:
                counts[main_category] += 1
                
        return detections, counts