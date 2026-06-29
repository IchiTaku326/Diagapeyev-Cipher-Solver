"""
Diagapeyev Cipher Heuristic Optimizer
This script implements a stochastic heuristic search to recover the 6x6 
Straddling Checkerboard matrix by maximizing linguistic coherence using 
Russian bigram frequency statistics.
"""

import random
import math
import sys

# Ciphertext coordinates
COORDS = [
    (4,5), (2,2), (5,2), (4,5), (6,1), (2,2), (6,1), (2,4), (5,1), (2,4),
    (6,1), (3,4), (5,5), (4,4), (3,4), (3,4), (4,4), (4,2), (5,4), (4,3),
    (5,1), (2,3), (5,1), (4,1), (4,4), (3,4), (5,2), (2,2), (3,4), (3,5),
    (5,3), (4,2), (5,4), (5,1), (4,5), (3,4), (3,5), (4,3), (4,5), (3,5),
    (4,5), (5,3), (3,3), (2,5), (3,5), (4,1), (3,3), (4,1), (4,5), (4,5),
    (4,5), (3,5), (3,4), (2,2), (5,2), (5,2), (5,5), (3,4), (3,3), (4,2),
    (4,5), (3,4), (5,3), (4,1), (3,5), (4,1), (5,4), (4,5), (3,4), (4,5),
    (3,4), (4,5), (5,5), (2,3), (5,2), (3,2), (3,2), (4,3), (3,2), (4,1),
    (5,1), (3,2), (5,1), (2,4), (3,3), (3,5), (5,2), (4,1), (3,4), (4,3),
    (3,3), (4,2), (5,5), (4,1), (3,3), (2,3), (3,3), None,  (4,4), (4,1),
    (6,1), (5,1), (5,4), (2,3), (5,5), (4,4), (3,5), (2,4), (5,5), (2,5),
    (3,2), (5,4), (3,2), (2,2), (5,5), (5,1), (5,5), (5,1), (4,4), (5,1),
    (4,2), (3,5), (3,4), (2,5), (4,5), (3,1), (3,5), (4,3), (3,2), (2,4),
    (4,4), (4,1), (5,2), (4,4), (3,2), (4,2), (3,4), (5,1), (5,1), (5,3),
    (3,5), (2,2), (3,4), (4,4), (5,4), (5,1), (5,3), (4,5), (4,4), (5,1),
    (5,1), (2,5), (4,2), (3,4), (5,3), (4,3), (5,5), (4,2), (5,3), (2,4),
    (3,2), (3,2), (3,2), (2,5), (3,2), (4,3), (4,5), (5,2), (4,2), (2,3),
    (5,2), (4,2), (4,2), (3,2), (5,3), (4,2), (5,5), (4,4), (4,5), (4,2),
    (5,1), (4,3), (4,2), (4,4), (3,2), (4,2), (5,3), (3,5), (5,1), (2,4),
    (4,5), (3,4), (5,5), (4,1), (3,2), (5,2)
]

# Standard Russian bigram frequencies
RUSSIAN_BIGRAMS = {
    'СТ': 0.0312, 'НО': 0.0243, 'ЕН': 0.0231, 'ТО': 0.0212, 'НА': 0.0205,
    'ОВ': 0.0198, 'НИ': 0.0189, 'РА': 0.0175, 'ВО': 0.0166, 'КО': 0.0162,
    'ПО': 0.0158, 'ЛО': 0.0143, 'ЛИ': 0.0135, 'ОН': 0.0132, 'ТА': 0.0128,
    'ОТ': 0.0125, 'ЕМ': 0.0119, 'ОД': 0.0115, 'МЕ': 0.0112, 'ВА': 0.0108,
    'ТИ': 0.0105, 'ЕТ': 0.0098, 'ПЛ': 0.0095, 'АК': 0.0092, 'ЛА': 0.0089,
    'ЗН': 0.0085, 'НЕ': 0.0082, 'АЛ': 0.0079, 'БЫ': 0.0075, 'ЧТ': 0.0072,
    'ЕС': 0.0070, 'ОМ': 0.0060, 'БЛ': 0.0055, 'ДА': 0.0052, 'КА': 0.0048, 'ЕР': 0.0045
}

BASE_MATRIX = {
    (1,1): 'Х', (1,2): 'Ф', (1,3): 'Ш', (1,4): 'Ц', (1,5): 'Я',
    (2,1): 'Г', (2,2): 'З', (2,3): 'В', (2,4): 'И', (2,5): 'Д',
    (3,1): 'Ж', (3,2): 'П', (3,3): 'Э', (3,4): 'Н', (3,5): 'Б',
    (4,1): 'Ы', (4,2): 'К', (4,3): 'Л', (4,4): 'С', (4,5): 'Е',
    (5,1): 'Т', (5,2): 'Р', (5,3): 'А', (5,4): 'М', (5,5): 'О',
    (6,1): 'Ч', (6,2): 'Ю', (6,3): ' ', (6,4): 'Ь', (6,5): 'У'
}

def get_text(current_map):
    """Map coordinates to characters to produce plaintext."""
    return "".join([" " if c is None else current_map.get(c, "?") for c in COORDS])

def calculate_score(text):
    """Calculate the log-likelihood score based on Russian bigram frequency."""
    score = 0.0
    for i in range(len(text) - 1):
        bigram = text[i:i+2]
        weight = 2.0 if (i % 5 >= 3) else 1.0 
        if bigram in RUSSIAN_BIGRAMS:
            score += math.log10(RUSSIAN_BIGRAMS[bigram] * 1000) * weight
        elif "?" in bigram or " " in bigram:
            score -= 4.0
        else:
            score -= 0.4
    return score

def main():
    print("=== Diagapeyev Cipher Heuristic Optimizer Started ===")
    best_map = BASE_MATRIX.copy()
    all_coords = [(r, c) for r in range(1, 7) for c in range(1, 6)]
    
    best_score = calculate_score(get_text(best_map))
    iterations = 0
    
    while True:
        iterations += 1
        test_map = best_map.copy()
        
        # Periodic stochastic jump to escape local optima
        if iterations % 500 == 0:
            targets = random.sample(all_coords, 15)
            shuffled_vals = [test_map[t] for t in targets]
            random.shuffle(shuffled_vals)
            for t, v in zip(targets, shuffled_vals):
                test_map[t] = v
        else:
            c1, c2 = random.sample(all_coords, 2)
            test_map[c1], test_map[c2] = test_map[c2], test_map[c1]
            
        test_text = get_text(test_map)
        test_score = calculate_score(test_text)
        
        if test_score > best_score:
            best_score = test_score
            best_map = test_map
            print(f"🔥 [New Best] Iterations: {iterations:,} | Score: {best_score:.2f}")
            with open("new_result.txt", "w", encoding="utf-8") as f:
                f.write(f"Score: {best_score}\n{test_text}")

if __name__ == "__main__":
    main()
