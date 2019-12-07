#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   knn_font.py
@Time    :   2019/12/8 2:50:00
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''
import numpy as np
import pandas as pd
from maoyan.font import get_font_data
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier


class Classify:
    def __init__(self):
        self.len = None
        self.knn = self.get_knn()

    def process_data(self, data):
        imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
        return pd.DataFrame(imputer.fit_transform(pd.DataFrame(data)))

    def get_knn(self):
        data = self.process_data(get_font_data())
        x_train = data.drop([0], axis=1)
        y_train = data[0]
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_train, y_train)
        self.len = x_train.shape[1]
        return knn

    def knn_predict(self, data):
        df = pd.DataFrame(data)
        data = pd.concat([df, pd.DataFrame(np.zeros(
            (df.shape[0], self.len - df.shape[1])), columns=range(df.shape[1], self.len))])
        data = self.process_data(data)
        y_predict = self.knn.predict(data)
        return y_predict

