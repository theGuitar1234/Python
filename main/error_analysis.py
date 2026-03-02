from turanpy.classification import error_analysis
from turanpy.classification import confusion_matrix

import random

def main(true_labels, predictions):
    cnfsn_mtrx = confusion_matrix(true_labels, predictions)
    print(error_analysis(cnfsn_mtrx))

if __name__ == "__main__":

    true_labels = [random.randint(0, 1) for _ in range(10)]
    predictions = [random.randint(0, 1) for _ in range(10)]

    main(true_labels, predictions)
    # {'True Positives': 2, 'True Negatives': 4, 'False Positives': 2, 'False Negatives': 2, 'Accuracy': 0.6, 'Percision': 0.5, 'Recall': 0.5, 'F1_score': 0.5}