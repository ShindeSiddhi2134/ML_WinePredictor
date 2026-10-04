import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def marvellousClassifier(DataPath):
    border="-"*40

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

    #step3:seperate dependent and independent veriables

    print(border)
    print("step3:seperate dependent and independent veriables")
    print(border)   

    X=df.drop(columns=['Class'])
    Y=df['Class']

    print("shape of X:",X.shape)
    print("shape of Y:",Y.shape)

    print(border)
    print("input column:",X.columns.tolist())
    print("output column:class")
    print(border)

    
    
    #step4: split the dataset 
    
    print(border)
    print("step4: split the dataset ")
    print(border) 

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("details of training and testing data")
    print("Shape of X_train:",X_train.shape)
    print("Shape of X_test:",X_train.shape)

    print("Shape of y_train:",Y_train.shape)
    print("Shape of y_test:",Y_train.shape)

    print(border)
def main():
    marvellousClassifier("WinePredictor.csv")
if __name__=="__main__":
    main()