import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def marvellousClassifier(DataPath):
    border="-"*50

    #step1:load the dataset from csv file
    print(border)
    print("step1:load the data set from csv file")
    print(border)

    df=pd.read_csv(DataPath)

    print(border)
    print("some entries in dataframe")
    print(df.head())
    print(border)

    #step2:clean the datset
    print(border)
    print("step2:clean the datset")
    print(border)   

    df.dropna(inplace=True)
    print("shape of dataset:",df.shape)
    print("total records:",df.shape[0])
    print("total columns:",df.shape[1])

    print(border)
def main():
    marvellousClassifier("WinePredictor.csv")
if __name__=="__main__":
    main()