def confusion_matrix(true_labels, predictions):
    if (len(true_labels) != len(predictions)):
        raise TypeError("Lists must match")
    
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for i in range(len(predictions)):
        if predictions[i] == 1 and predictions[i] == true_labels[i]:
            TP += 1
        elif predictions[i] == 0 and predictions[i] == true_labels[i]:
            TN += 1
        elif predictions[i] == 1 and predictions[i] != true_labels[i]:
            FP += 1
        elif predictions[i] == 0 and predictions[i] != true_labels[i]:
            FN += 1
    return (TP, TN, FP, FN)

if __name__ == "__main__":
    pass