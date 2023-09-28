import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = ___(
        evidence, labels, test_size=___
    )

    # Train model and make predictions
    model = ...
    #Make predictions. Hint: check the sci-kit learn predict method!
    predictions = ...
    sensitivity, specificity = evaluate(___, ___)

    # Print results
    print(f"Correct: {(y_test == ___).sum()}")
    print(f"Incorrect: {(y_test != ___).sum()}")
    print(f"True Positive Rate: {100 * ___:.2f}%")
    print(f"True Negative Rate: {100 * ___:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence, labels = [], []
    import calendar
    month_to_number = {name: num - 1 for num, name in enumerate(calendar.month_abbr) if num}

    with open(filename) as data:
        reader = csv.reader(data)
        next(reader)  # skip the fist line with attributes
        for row in reader:
            ___.append([
                ___(row[0]),    # Administrative
                ___(row[1]),  # Administrative_Duration
                ___(row[2]),    # Informational
                float(row[3]),  # Informational_Duration
                int(row[4]),    # ProductRelated
                ___(row[5]),  # ProductRelated_Duration
                ___(row[6]),  # BounceRates
                ___(row[7]),  # ExitRates
                float(row[8]),  # PageValues
                float(row[9]),  # SpecialDay
                month_to_number[row[10][:3]],  # Month
                ___(row[11]),   # OperatingSystems
                ___(row[12]),   # Browser
                int(row[13]),   # Region
                int(row[14]),   # TrafficType
                1 if row[15] == 'Returning_Visitor' else 0,  # VisitorType
                ___((row[16]) == 'TRUE'),   # Weekend
            ])

            ___.append(
                int(row[17] == ___)  # Revenue
            )

    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = ___(n_neighbors=1) # train model with 1 neighbor
    # Fit the model (train). What inputs does the model need to train? Check the sciki-learn fit method!
    ...
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    ___, specificity = 0.0, 0.0
    ___, negative = 0.0, 0.0

    for ___, ___ in zip(labels, predictions):
        if label == 1:  # if label is positive, then we calculate sensitivity (positive rate)
            positive += 1
            if label == prediction:
                ___ += 1

        else:  # if label is negative, then we calculate specificity (negative rate)
            negative += 1
            if label == prediction:
                specificity += 1

    sensitivity /= ___
    specificity /= ___

    return ...


if __name__ == "__main__":
    main()
