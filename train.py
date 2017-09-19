import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation

def main():
    print("Reading in the training data")
    x = pd.read_csv("train.csv", header=None)
    y = pd.read_csv("trainLabels.csv", header=None)
    
    print("Random Forest cross validation score")
    clf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=1, random_state=0)
    print cross_validation.cross_val_score(clf, x, y[y.columns[0]], cv = 5)

    print "Run train and test split"
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y[y.columns[0]], test_size = 0.2, random_state=0)
    clf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=1, random_state=0)
    clf.fit(x_train, y_train)
    print clf.score(x_test, y_test)
    
if __name__=="__main__":
    main()







