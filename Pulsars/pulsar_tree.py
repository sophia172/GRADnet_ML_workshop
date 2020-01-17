import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
# Import train_test_split function
from sklearn.model_selection import train_test_split
# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Vizualization
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
#from IPython.display import Image
import pydotplus
#import cv2 as cv
import matplotlib.pyplot as plt
from scikitplot.estimators import plot_learning_curve

data = pd.read_csv('pulsar_stars.csv')

# We first decide on how to split the data into features and labels
# features:
features = data.columns[:-1]
X = data[features]
# output:
y = data.target_class

# Now we need to split te data using train_test_split.This requires us to choose said split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123)
# This will give a training:test ratio of 8:2. Random state is set so that we get the same results in a different run

# We now make the classifier
classifier = DecisionTreeClassifier()

# Training
classifier = classifier.fit(X_train, y_train)
# Preducting the response for the test dataset
y_pred = classifier.predict(X_test)


# Let's see how accurate our model is likely to be
print('Accuracy = {}'.format(metrics.accuracy_score(y_test, y_pred)))

plot_learning_curve(classifier, X_test, y_test)
plt.show()
