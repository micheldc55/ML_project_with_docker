import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split


def load_and_process(path):
    df = pd.read_csv(path)
    df = df.drop(columns=["Unnamed: 0"])
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df


def split(df):
    X = df.drop(columns=["price"])
    y = df["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return X_train, X_test, y_train, y_test
