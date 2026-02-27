class Scorer:
    def calculate_score(self, counts, brightness, glare):
        # Start initial score at 70 
        score = 70
        
        # --- PENALTIES ---
        # Deduct 30 points per distractor
        distractor_penalty = counts.get("distractor", 0) * 30
        score -= distractor_penalty
        
        # Deduct 15 points per non-study clutter item
        clutter_penalty = counts.get("non_study_clutter", 0) * 15
        score -= clutter_penalty
        
        # --- REWARDS ---
        # Add 15 points per study essential item
        essential_bonus = counts.get("study_essential", 0) * 15
        score += essential_bonus
        
        # Add 5 points per study support item
        support_bonus = counts.get("study_support", 0) * 5
        score += support_bonus
        
        # --- ENVIRONMENTAL PENALTIES ---
        # Apply penalty for low brightness [cite: 29]
        if brightness < 80:
            score -= 10
        elif brightness < 40: # Too dark
            score -= 20
            
        # Apply penalty for high glare [cite: 30]
        if glare > 5.0:
            score -= 10
        
        # Clamp score between 0 and 100 
        score = max(0, min(100, score))
        
        # Determine status label
        if score >= 80:
            status = "Good"
        elif score >= 50:
            status = "Moderate"
        else:
            status = "Poor"
            
        return score, status