import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import preprocessing

# Extra trees classifier

def loadData(filename,
             num_classes,
             num_features,
             num_samples):

    sample_data_x = np.zeros((num_samples, num_features))
    sample_data_y = np.zeros((num_samples, 1))
    count = 0
    for line in open(filename, 'r'):
        info = line.split(',')
        for entry in range(len(info) - 1):
            sample_data_x[count, entry] = float(info[entry])
        sample_data_y[count] = float(info[-1])
        count += 1
    train_y = np.array(sample_data_y.astype(np.int32))
    #converted_sample_data_y = convert_to_one_hot(train_y, num_classes)
    return sample_data_x, train_y


def convert_to_one_hot(y_labels, num_classes):
    lb = preprocessing.LabelBinarizer()
    classes_array = np.arange(0, num_classes)
    lb.fit(classes_array)
    one_hot = lb.transform(y_labels)
    return one_hot


def extraTreesClassifier(X, Y, X_test, Y_test):
    clf = ExtraTreesClassifier(n_estimators=10,
                               random_state=0)
    fitXY = clf.fit(X, Y)
    score = fitXY.score(X, Y)
    print('Training set score: ' + str(score))
    score = clf.score(X_test, Y_test)
    print('Test set score: ' + str(score))


filename = 'Fusobacterium_train.txt'
num_classes = 2
num_features = 60
num_samples = 48
training_x, training_y = loadData(filename,
                                  num_classes,
                                  num_features,
                                  num_samples)

filename = 'Fusobacterium_test.txt'
num_classes = 2
num_features = 60
num_samples = 10
test_x, test_y = loadData(filename,
                                  num_classes,
                                  num_features,
                                  num_samples)


extraTreesClassifier(training_x, training_y, test_x, test_y)
