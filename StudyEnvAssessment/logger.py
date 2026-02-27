import csv
import os
from datetime import datetime

class Logger:
    def __init__(self, filename="study_log.csv"):
        self.filename = filename
        
        # 47. Create CSV file if not exists and write headers [cite: 47]
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Timestamp", 
                    "Study Essential", 
                    "Study Support", 
                    "Non-Study Clutter", 
                    "Distractor",
                    "Brightness", 
                    "Glare (%)", 
                    "Score", 
                    "Status"
                ])

    def log(self, counts, brightness, glare, score, status):
        # 48. Append data continuously [cite: 48]
        with open(self.filename, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # [cite: 49]
                counts.get("study_essential", 0),
                counts.get("study_support", 0),
                counts.get("non_study_clutter", 0),
                counts.get("distractor", 0),
                f"{brightness:.2f}",
                f"{glare:.2f}",
                score,
                status
            ])