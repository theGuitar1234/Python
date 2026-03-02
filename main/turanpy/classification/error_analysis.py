def error_analysis(confusion_matrix):

    TP = confusion_matrix[0]
    TN = confusion_matrix[1]
    FP = confusion_matrix[2]
    FN = confusion_matrix[3]

    total = sum(confusion_matrix)

    percision = TP / (TP + FP)
    recall = TP / (TP + FN)
    
    return {
        "True Positives": TP,
        "True Negatives": TN,
        "False Positives": FP,
        "False Negatives": FN,
        "Accuracy": (TP + TN) / total,
        "Percision": percision,
        "Recall": recall,
        "F1_score": 2 * (percision * recall) / (percision + recall),
    }