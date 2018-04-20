import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import csv
X1 = []
X2 = []
Y = []

XTrain = []
YTrain = []
XTest = []
YTest = []

XTrainNorm = []
YTrainNorm = []
XTestNorm = []
YTestNorm = []
def crearConjuntos():
    #Variables auxiliares


    with open('ex1data2.csv') as csvarchivo:
        entrada = csv.DictReader(csvarchivo, delimiter=";")
        for row in entrada:
            X1.append(float(row['X1']))
            X2.append(float(row['X2']))
            Y.append(float(row['Y']))


    for i in range(len(X1)):
        if (i < 28):
            #print(i,"Llenando train")
            XTrain.append([1, X1[i],X2[i]])
            YTrain.append(Y[i])
            XTrainNorm.append([1, nomalizar(i, X1), nomalizar(i, X2)])
            YTrainNorm.append(nomalizar(i, Y))
        else:
            #print(i,"llenando test")
            XTest.append([1, X1[i], X2[i]])
            YTest.append(Y[i])
            XTestNorm.append([1, nomalizar(i, X1), nomalizar(i, X2)])
            YTestNorm.append(nomalizar(i, Y))

    return np.asarray(XTrain),np.asarray(XTest),np.asarray(XTrainNorm),np.asarray(XTestNorm),np.asarray(YTrain),np.asarray(YTest),np.asarray(YTrainNorm),np.asarray(YTestNorm)


def nomalizar(i, valArray):
    valArray=np.asarray(valArray)
    norm = (valArray[i] - np.mean(valArray)) / (np.amax(valArray) - np.amin(valArray))
    return norm


#Crear todos los conjuntos

X_Train,X_Test,X_TrainNorm,X_TestNorm,Y_Train,Y_Test,Y_TrainNorm,Y_TestNorm = crearConjuntos()
np.add
B=np.linalg.inv(X_Train.T @ X_Train) @ X_Train.T @ Y_Train
Bnorm=np.linalg.inv(X_TrainNorm.T @ X_TrainNorm) @ X_TrainNorm.T @ Y_TrainNorm

def pruebaMAPE():
    dif=[]
    dif2=[]
    ind=0
    for i in X_Test:
        aux=B[0]+i[1]*B[1]+i[2]*B[2]
        dif.append(np.abs((Y_Test[ind]-aux)/Y_Test[ind]))
        ind = ind + 1

    print("MAPE: ",np.mean(dif))

    ind = 0
    for i in X_TestNorm:
        aux = Bnorm[0] + i[1] * Bnorm[1] + i[2] * Bnorm[2]
        dif2.append(np.abs((Y_TestNorm[ind] - aux) / Y_TestNorm[ind]))
        ind = ind + 1
    print("MAPE Normalizado: ", np.mean(dif))



print("betha: ",B)
print("betha norm: ", Bnorm)
pruebaMAPE()


