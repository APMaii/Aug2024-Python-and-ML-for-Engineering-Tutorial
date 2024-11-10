#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In The Name Of GOD

Created on Sat Oct  5 10:41:06 2024

@author: Ali pilehvar mEIBODY


LL_DEEP_LEARNING


AI ----> 80% ml ----> (Traditional ML + Deep L (DL))

Deep learning --> Base --> Perceptron --> inspiration from neuron

neuron---> input ---> Oouput (claculation)


perceptron --> input ---> weight multiple + bias --> output


Multi layer ---> MLP (muylti layer perceptron)
first layer--> input layer--> we dont have any calculations --> getting input
hidden layers (1 , 2, 3 >3 --> deep )
final layer---> output layer--> ooutput--> classifdication ( 0 , 1), regression

each layer has multiple neurons


laye ye aval (vorodi) be tedade vorodi ha neuron dare
laye ye akahr yedone (be onvane khoroji)
lauye haye beyn

chanta laye darim , 2,3,4,....
va dar harkodom chanta neurons
activation function -->control mikrd khorojie har neuron az ch noee bashe
backpropagation --> pas enteshar --> random w, b --> error MAE --> barmigasht
chijoori optimization ro najam bde --> algorithm optimization

--->hypeparameters --> ghabl az training moshakhas konim--> tasire ziadi dar amozoehs em adarand



v1 v2 v3


w1*v1 + w2*v2 + w3**v3 + Bias = Khooroji


Multi Layer perceptron 

#----------------------
1-kh awlie --> fdeature extraction + learning
2- deghate besiar balaee dare

Disadvantages:
    1- niaz b dataye kh ziaddd dare ta deghatesh khob bashe ( 10000 , 1 million)
    2-kh tedade hypeparameter hash ziade (tedxade laye, to ha rlaye chnata neuron , vase har laye ch activation function , ....)
    3- computationally cost 
    



"""
#1-
#2-

from sklearn.datasets import load_iris

#step0------------------------ cleaning
iris=load_iris()

#step 1---> x,y
x=iris.data
y=iris.target
#x--> 4ta vorodi daran --> #picture, data , kalamat
#opencv --> ax --> numpy array contain (too delesh --> havie doen doen pxiel hja ye krange beyne 0 ta 251 hast1 )

#y--> 0 1 2 


#step 2---> kfold , maa man inja train test easy

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)


#STEP3 ---> MODEL SELECTION model. fit mikonm -p--> model , myparams gridsearch

from sklearn.neural_network import MLPClassifier #BARAYE CLASSIFICATION
from sklearn.neural_network import MLPRegressor #baraye regressipon
#too delesh man parmaetr haye mohemro mizrm
model=MLPClassifier(random_state=42,hidden_layer_sizes=(100,) ,activation='tanh',solver='sgd')

                    
#begoo chnd laye dari chan ta neuron
#Vorodi khroojiam vel kon man khdoam baladam

# 1 laye 20 ta neurpon 
#(20,)

#(100,) 1 laye vasat 100 ta neuron

# 2 laye 10 , 20
#(10,20)

#harchi bsihtar abshe , bsihatr tool mikshe , amja momkene javab bde ,
#my params = {'hidden_layer_sizes' : [ (10,), (20,),(100,),(10,10),(20,20),(100,100)]}
#khoroji haye har neuron ro contorl mikone relu
#tanh
#activation{‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, default=’relu’
#solver{‘lbfgs’, ‘sgd’, ‘adam’}, default=’adam’
#dar myparams

#step 4---> shoma gridsearchcv (model, myparams, score ,.....,n_jobs=-1)  gs.fit(x,y)

model.fit(x_train,y_train)
#gs.best_score

#step5-->valdiation

from sklearn.metrics import accuracy_score

y_test_pred=model.predict(x_test)
sc=accuracy_score(y_test,y_test_pred)

print(sc)
#0.9666666666666667


model=MLPClassifier(random_state=42,hidden_layer_sizes=(100,) ,activation='relu',solver='sgd')
model.fit(x_train,y_train)
y_test_pred=model.predict(x_test)
sc=accuracy_score(y_test,y_test_pred)
print(sc)
#0.9333333333333333

#==================================
#takm,li va nahaeee

#step0----> clean 
#step1 --> x , y
x=iris.data
y=iris.target

#step2-->kfold

from sklearn.model_selection import KFold

kf=KFold(n_splits=5,shuffle=True,random_state=42)

#step3---> model selection + myaprams

from sklearn.neural_network import MLPClassifier

model=MLPClassifier(random_state=42) #default
myparams={ 'hidden_layer_sizes' : [(100,), (200,),(10,10),(20,20),(10,10,10)],
          'activation':['relu','tanh','logistic','identity'],
          'solver':['adam','sgd','lbfgs']}


#'alpha'
#learning_rate_init

#4--->
from sklearn.model_selection import GridSearchCV

gs=GridSearchCV(model,myparams,cv=kf,scoring='accuracy',n_jobs=-1)

gs.fit(x,y)

gs.best_score_ #Out[23]: 0.9800000000000001

gs.best_params_

'''
 {'activation': 'relu', 'hidden_layer_sizes': (200,), 'solver': 'adam'}
 '''






'''
 Maximum iterations (200) reached and the optimization hasn't converged yet.
 model=MLPClassifier(random_state=42,max_iter=200000) #default

'''
 

#======================

'''

CNN ---> binaee machine
RNN ---> bazgashti --> hafeze
GAN -_> generative adversial network --> 2 ta network , network, network baerkhalafe onyekio misaze
autoencoder
LSTM



base--> ANN (MLP)

'''


'''
ketabkhoenye pishrafte tar--_>

Keras
Tensorflow [XXXXXX]


pytorch

'''

