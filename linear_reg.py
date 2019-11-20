import numpy as np
import random

import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split


class linear_regression:
    def __init__(self, learning_rate, iterations,
                 fit_intercept=True, normalize=False, coef=None):
        self.fit_intercept = fit_intercept
        self.normalize = normalize
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.coef = coef
        self.c = 0
        self.m = 0


    def fit(self, X, y):
        """
        Fit linear model.
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Training data
        y : array_like, shape (n_samples, n_targets)
            Target values.
        """
        if(self.normalize):
            no_f = X.shape[1]
            X = (X-np.mean(X, axis=0))/np.std(X, axis=0)

        m = np.zeros(X.shape[1],1)
        #number of rows
        r = X.shape[0]


        if(self.fit_intercept):
            N = len(X)
            N = np.concatenate([1],X)
        else:
            N = X

        for i in range(self.iterations):
            y_0 = np.dot(N,m)
            k = y_0-y
            M = m - self.learning_rate*(1/r)*np.dot(k,X)
        return M


    def predict(self, X):
        """Predict using the linear model
        Parameters
        ----------
        X : array_like, shape (n_samples, n_features)
            Samples.
        Returns
        -------
        C : array, shape (n_samples,)
            Returns predicted values.
        """
        predict = np.dot(self.m, X)
        return predict



# Your code goes here
dataset = pd.read_csv('C:\Users\rutvi\Downloads\\50_Startups.csv')
print(dataset.shape)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
linear_reg = linear_regression(0.0001, 30,fit_intercept=True, normalize=False, coef=None)
linear_reg.fit(X_train, y_train)
print(linear_reg.intercept_)
print(linear_reg.coef_)
#zip(feature_cols, linear_reg.coef_)
y_predict = linear_reg.predict(X_test)


