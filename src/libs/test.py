import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(path):
    df = pd.read_csv(path)
    df = df.drop(columns = ['Unnamed: 0'])
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df
