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

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

    print(border)
    print("details of training and testing data")
    print("Shape of X_train:",X_train.shape)
    print("Shape of X_test:",X_train.shape)

    print("Shape of y_train:",Y_train.shape)
    print("Shape of y_test:",Y_train.shape)

    print(border)

    #step5:features scaling

    print(border)
    print("step5:features scaling ")
    print(border) 

    scaler =StandardScaler()
    X_train_scaled=scaler.fit_transform(X_train)
    X_test_scaled=scaler.fit_transform(X_test)

    Y_train_scaled=scaler.fit_transform(Y_train)
    Y_test_scaled=scaler.fit_transform(Y_test)
    print("feature scalling done")

    print(border)

    #step 6:hyper parameter tunning

    accuracy_score=[]

    k_values=range(1,21)

    for k in k_values:
        model=KNeighborsClassifier(n_neighbors=k)
        model=model.fit(X_train_scaled,Y_train)
        Y_pred=model.predict(X_test_scaled)
        accuracy=accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print("accuracy report:")
    for no in accuracy_scores:
        print(no)

    print(border)

    print(border)
    print("graphical representaion")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(k_values,accuracy_scores,marker="o")

    plt.title("k values vs accuracy")
    plt.xlabel("values of k")
    plt.ylabel("accuracy")
    plt.grid(True)
    plt.xtickss

    


def main():
    marvellousClassifier("WinePredictor.csv")
if __name__=="__main__":
    main()