#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 20:46:52 2018

@author: leonel
"""
# organize imports
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy as np

#Para reproducir los mismo resultados
seed = 9
np.random.seed(seed)

#Se carga la data
dataset = np.loadtxt('dataFinal.csv', delimiter=',', skiprows=1)

#Split de variables de ingreso y de salida
X = dataset[:,1:24]

Y = dataset[:,0]

#Entrenamiento 66 y validacion 33
(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, test_size=0.33, random_state=seed)


model = Sequential()
model.add(Dense(100, input_dim=19, init='uniform', activation='relu')) #Solo en la primera capa se debe de especificar el input dim

#model.add(Dense(50, init='uniform', activation='linear'))

model.add(Dense(625, init='uniform', activation='relu'))

#model.add(Dense(10, init='uniform', activation='selu'))

model.add(Dense(625, init='uniform', activation='relu'))
model.add(Dense(110, init='uniform', activation='linear'))


#model.add(Dense(600, init='uniform', activation='softplus'))
#model.add(Dense(600, init='uniform', activation='tanh'))
model.add(Dense(1, init='uniform', activation='sigmoid'))



model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, Y_train, validation_data=(X_test, Y_test), nb_epoch=750, batch_size=300) #300

scores = model.evaluate(X_test, Y_test)
print ("Accuracy: %.2f%%" %(scores[1]*100))


#Relu x2, elu y sigmoid = 54 sin tiempo y respuesta => 57.39% 


#Relu x2, elu, sigmoid, sin tiempo, respuesta y cie 55.47 (1200 epochs) y 56 con (2000 epochs) 56

#tiempo, respuesta, cie y cies 55.67 (1200 epochs) y  58 con (2000 epochs)
#tiempo, respuesta, cie y cies y dsmt 55.33 (1200 epochs) y  58 con (2000 epochs)
#Tiempo, respuesta, cie, cies y pebl 59.11 (1200 epochs) y 57.39 con (2000)
#Tiempo, respuesta, cie, cies, pebl y rmsLevel  58.42 (1200 epochs) y  55.67 con (2000)
#Tiempo, respuesta, cie, cies, pebl y maxLevel  58.08 (1200 epochs) y  58.42 con (2000)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~~~



#Tiempo, respuesta, cie, cies, pebl y escolaridad  56.7 (1200 epochs) y 53.61 con (2000)





#tiempo, respuesta, cie y cies 56.7 (1200 epochs) y  53.95 con (2000 epochs)

#tiempo, respuesta, cie y cies y ciem  55.67 (1200 epochs) y 57.04  con (2000 epochs)

#tiempo, respuesta, cie y cies y ciem y cief 52.23 (1200 epochs) y  53.95 con (2000 epochs)


#22 avenida 00-39 vista hermosa 2 zona 15
# 2 menus y una hamburguesa
