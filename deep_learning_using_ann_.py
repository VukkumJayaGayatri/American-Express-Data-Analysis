# -*- coding: utf-8 -*-
"""Deep Learning Using ANN .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i7tsJQkwoNUghWrUcEAn2e_pdq97_nDu

Deep Learning using ANN
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_set = pd.read_csv('/content/American Express User Prediction.csv')

data_set = data_set.dropna()

X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, -1].values

print(X)

"""Encoding Categorical data

Gender Column: Label Encoding
"""

from sklearn.preprocessing import LabelEncoder

label_encoder=LabelEncoder()

X[:,2]=label_encoder.fit_transform(X[:,2])

print(X)

"""Geography Column: One hot encoding"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(), [1])], remainder= 'passthrough')
X = np.array(ct.fit_transform(X))

print(X)

"""Splitting data into train and test dataset"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

"""ANN Initialization"""

import tensorflow as tf
import keras
from keras import layers

ann1=tf.keras.models.Sequential()

print(X_train.shape, y_train.shape)

"""Adding Input and first Hidden Layer"""

ann1.add(tf.keras.layers.Dense(units=5, activation='relu', input_shape=(11,)))

"""Adding Second Hidden Layer"""

ann1.add(tf.keras.layers.Dense(units=5, activation='relu'))

"""Adding output layer"""

ann1.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

"""ANN Training

Compiling ANN
"""

ann1.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

"""Training on Train dataset"""

ann1.fit(X_train, y_train, batch_size=32, epochs =120)

"""Predicting

Single Predictions
"""

print(ann1.predict(sc.transform([[0.0, 1.0, 0.0, 501, 0, 32, 2, 0.0, 4, 1, 545501]])) > 0.5)

"""Prediction on Test dataset"""

y_pred=ann1.predict(X_test)
y_pred=(y_pred>0.5)

print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1 ))

"""Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)

accuracy_score(y_test, y_pred)
