import cv2

class Overlay:
    def draw(self, frame, detections, brightness, glare, score, status):
        # Draw bounding boxes on frame
        for det in detections:
            x1, y1, x2, y2 = det['bbox']
            full_label = det['label']
            main_cat = det['main_category']
            
            # Format the text from "distractor_smartphone" to "distractor(smartphone)"
            if main_cat and full_label.startswith(main_cat + "_"):
                # Remove the main category and the underscore to get just the item
                item_name = full_label[len(main_cat)+1:] 
                display_text = f"{main_cat}({item_name})"
            else:
                display_text = full_label
            
            # Color-code boxes by main category
            color = (0, 255, 0) # Green for study items (essential & support)
            if main_cat == "non_study_clutter":
                color = (0, 0, 255) # Red for clutter
            elif main_cat == "distractor":
                color = (0, 165, 255) # Orange for distractor
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            
            # Display the formatted item name on the screen
            cv2.putText(frame, f"{display_text} {det['conf']:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Dashboard Overlay (Top Left corner)
        info_text = [
            f"Score: {int(score)} ({status})",
            f"Brightness: {brightness:.1f}",
            f"Glare: {glare:.1f}%"
        ]
        
        y_offset = 30
        for info in info_text:
            cv2.putText(frame, info, (20, y_offset), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
            y_offset += 30
            
        return frame