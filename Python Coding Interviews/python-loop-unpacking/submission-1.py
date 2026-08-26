from typing import List, Tuple
import math

def best_student(scores: List[Tuple[str, int]]) -> str:
    maxscore = -math.inf
    maxname = ""
    for name, score in scores:
        if score >= maxscore:
            maxscore = score
            maxname = name
    return maxname




# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
