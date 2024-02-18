import statistics

class ScoreTracker:
    def __init__(self):
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)
    
    def get_median_score(self):
        if len(self.scores) == 0:
            return 0
        else:
            return statistics.median(self.scores)

if __name__ == "__main__":
    score_tracker = ScoreTracker()
    score_tracker.add_score(85.5)  # Stream: [85.5]
    score_tracker.add_score(92.3)  # Stream: [85.5, 92.3]
    score_tracker.add_score(77.8)  # Stream: [85.5, 92.3, 77.8]
    score_tracker.add_score(90.1)  # Stream: [85.5, 92.3, 77.8, 90.1]
    median1 = score_tracker.get_median_score()  # Output: 87.8
    print("Median 1:", median1)
    score_tracker.add_score(81.2)  # Stream: [85.5, 92.3, 77.8, 90.1, 81.2]
    score_tracker.add_score(88.7)  # Stream: [85.5, 92.3, 77.8, 90.1, 81.2, 88.7]
    median2 = score_tracker.get_median_score()  # Output: 87.1
    print("Median 2:", median2)


