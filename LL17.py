
"""
In The Name Of GOD

Created on Wed Oct  2 17:54:26 2024

@author: Ali Pilehvar Meibody

LL17 (FINAL)

"""

'''
Python and AI for Engineering Course AUG2024 -----------
3 SECTION

SECTION 1 ----------------(BASIC PYTHON)
Python ---> interface between human (ENglish) vs computer ( Binary 01)
We need Chatbox (liek whatsapp ,m telegram) --> IDE (integrated development enviuronemnt) --> Jupyter , SPYDER
Python like other languages has two component --> 1-words (vocab)  2-grammar
bUILT IN function , keywords

Variables (ZARF) --> int, float, complex , str , bool , .. function str.function str.lower() str.upper() ,...
Multiple variables ---> List, touple , set (similar) , dictionary 
built in function--> print() input() len() type() open() ...
Keywords---> if , if else , for , while , .......
Functions --> def (arg1,arg2,....)
Advanced---> Class- object , additional keywords,.....
20% Project A1 ----> AIM --> Idea --> function 

SECTION2------------(MAdules, libraries)
import lib as brief
Math --> mathematic
Numpy -->calculation    np.array() 0D, 1D , 2D (row,column) --> approximately 50x  faster than list
Pandas---> working with data --> pd.DataFrame --> np 2d with column namesw sand row names , data cleaning (step 0 )--> dropna, isna, fillna, duplicated, to_numeric, read_csv, read_excel()
Matplotlib.pyplot--> Drawing graph --> plot(),scatter(),pie(),bar(), hist() [random normal(gaus) , unifrom]
30% Project A2 --> AIM--> Idea --> Data analys and calculation



SECTION3---------(AI MACHINE LEARNING)
regression basic simple ( a b , cost functiuon optimization)




AI ---> 2 GENERATION (NASL) 
First generation --> if else -->support chatbox if message==salam print('salam janam') , recommender, fuzzy logic , optimization (30% of Artificial intelligence)
Second generation --> ML (Machienb leanring 70% )--> difference --> learning ability like human ( 1-data 2-learning(trianing) 3-decision making ( tasmim , action amal))


ML ---> 3 SECDTION
-----Traditional ML---------
1----> Supervised learning (tahte nezarat)
2----> Unsupervised Learning (gheyre tahte nezarat, bedone nezaarat)
3-reinforcement (taghviati)

----DEEP LEARNING---- YADGIRIE AMIGH , suprervised --. advanced --> it needs million, billion data ( it is rare in engineering field) social media (insta, ) , picture, self driving car(Tesla), google , chat gpt , ....



1----> Supervised ----> classification (daste bandi) , regression (*regrasion)



************
KOLE MASAELE JAHANO --> INPUT() OUTPUT()
ML --> Ye boxe on vasat donable rabete ye beyen voroodi va khoroji


khoroji mitone adsade peyvaste bashe --> 1234.4 23 2323.. ashari --> rabeteye beyne yek vorodi (chnata vorodi) va yek khoroji peyvaste --> ML REGRESSION
khoroji mitone gosaste bashe--> mese tedade afrad edkahel class, mnmitoni bgi 2.5 2 3 4 ,..--> ta , chnat chnata --> daste bandi --> ML CLASSIFICATION



INPUT-----> RELATIONSHIP----->OUTPUT
1-ML supervised --->  regression, classifcation(gorbe , sag | badkhim , khosh khim | engineerin bad quality , good qulity | awli , bad khoob , 4 ghesmat , daste daste bandi ) -->dade e
dataee k darii  --> yeseri sotone x dari (arz, toole gol ,..) , khoroji dare-->obe roye har nemone neevshti in badkhime ,m oon khosh khim , 0 1 , nargese , rozo oon sag oon grobas (label) -->output has label
ag khoroji label nadashte bashe chi?--> yani shoma fght 100 ta gol dari k fght arzo tolesho dari
yek datae k 2 ta soton , 100 ta rafdif -->100 ta gole har gol yedone arz , yedone tool , ama sotone label nadare , yan nanevshte kodom roze kodom nargese, kodom sage kodom grobas kodom ,..... label XXXX
ML-->behesh bdim va bma bge k sage ya gorbas (daste bandi)
2-ML Unsupervised (tahte nearat nist) ---> K-means --> shoro mikone dataharo bar asase shabahato tafavor khoshe bandi , deghata aksaran paeen, validation , dar ebtedaye rah hastim --> Unsupervsied --> classification without lable

3-Reinforcement (advanced )-->taghviati --> Unsupervsied, supervsied datampoon amadas , import mikonim midim b moel mire jolo  train mibine amadas, amadeye prediction pishbini , ye model bzari too kar , ba mohti dar ertebat bashe m dar
heyne grftne dade hey khdoesho taghviat kone , hey bishtar yad bgire --> taghviati 
control CNC 


#------------------
kole framework  (supervised (sotone khoroji darim), y mitone peyvaste bashem gosaste)
step0----> data clenaing
step1----> data--> x , y 
step2---> x,y --> training, test data set taghsim mikonim (vase validation)
step3--> model selection ( 6 model 1-LR 2-K nearest neighbor 3-Decision tree , 4-random forest , 5-support vector machine , , 6-Multi layer perceptron ( Aretificxal neural network)) hamashon do noan ye no baraye y e gosaste (daste bandi) y e peyvaste (regression)
step4--> fit.(trianing) --> traiN , MIRE BA RAVESHI K BALADE (LR--> a , b mesal mziad cost fucnction optimzie minimum cost funciton A B) 2-KNN , (noghte noghte mizasht nazdik tarin hamsaye haro varmidasht va kole safe ro rangi mikrd) 3-decision tree--> hey dade haro yek gere mizad (node) soal ,, taghsim mikrd, shakhe shakhe, random forest --> chanta azin derakht haye random ro mziasht knare, svm , mlp
step5--> Validation , hala k fit dade shode --> training score ( fitting ability),test score (prediction ability) --> both trian score, test score high -->sweet (delkhah) point -->model awlie

kole mL model 2 ta generla steps---> 1-training (zaman mibare, yad migire) 2-usage (prediction, pishbini, daste bandi) --> kh sari chon yad grfte model.rpedict()
vali gahble inke bri tousage
from 1 to 2 . az amozesh ta estefade --> valdiation(etebarsanji konid) -->report k chghd modelet gtahvie



'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.DataFrame([[2.4,1.5,0],[2.6,1.7,0],[5.2,3.2,1],[5,3,1],[2.1,1.2,0],[2,1,0],[5.9,3.9,1],[2.12,1.43,0],[6,3.2,1],[6,3.1,1],[2.11,1.87,0]],
                  columns=['tool','arz','noe_gol'])



'''

tool  arz     noe gol
3 .4    2.2     Roz
5 .3    1.4    narges
4 .4    1.4     narges



tool  arz     noe gol
3 .4    2.2     0
5 .3    1.4    1
4 .4    1.4     1

dadeye ma -->gosaste ---> chanta chanta daste daste
0 1 
0 1 2 3
.......
1.5
ashar ndre



bar khalafe inke y ro bar asase x rasm konan
mian x haro bar asase ham rasm mikonan

'''
import matplotlib.pyplot as plt

#plt.scatter(data['tool'],data['noe_gol'])
plt.scatter(data['tool'],data['arz'],c=data['noe_gol'] , cmap='viridis')
plt.title('gol ha')
plt.xlabel('tool')
plt.ylabel('arz')
plt.show()


#1-Lostic regression --> hey khat haye motefavet in vasat mizasht
#2-KNN --> done done arzo tool haye motefavet ro bar asase nazdik tarin hamsye ha rang amizi mikrf
#3-decision tree , aval y soal miporsid , toole shoam bishtar az 4 hast ya na taghism mikrd, dobare baid -->derakhte tasmim --> random soalash ro miporsid , range ,.. adad ha va pishbini
#4-random forest -->> hezaran ya sadha derakhte tasmime random bsazam va miangineshon ya maximumeshon
#5-SVM
#6-MLP

#bastegi darad be dataye shoma va rabete ee k donbalesh hastid


'''
SVM--> YERK FEATURE (SOTONE VORODI) ezafe konim
shayad btoonim dar bode (dimention) balla tar daste bandi ro anjam bdim

kernel---> poly , rbf, sigmoid


'''


#STEP0
#STEP1
x=np.array(data[['tool','arz']]) #reshape nmikhad 2 ta sotoon
y=np.array(data['noe_gol'])

#step2
#x,y --> xtest x train , y test y train 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25, shuffle=True, random_state=42)


#step3
#classifcation

from sklearn.svm import SVC #support vector Clasiifier
#from sklearn.svm import SVR #support vector regressor

model=SVC()   #rbf --> rbf , poly (polynomial , chand jomle ee , daraje do ,....)
#kernel-->rbf
model=SVC(kernel='poly',degree=2) #kernelamo bokn poly , 2 

#step4
model.fit(x_train,y_train)


#step5-->

y_train_pred=model.predict(x_train)

#classification , gosaste mae, mape
#accuracy , confusion matrix

from sklearn.metrics import accuracy_score
train_score=accuracy_score(y_train, y_train_pred)
print('Train score accuracy : ',train_score)
#Train score accuracy :  1.0  --> kernel-->rbf 
#Train score accuracy :  1.0  --> kernel-->poly, degree=2

y_test_pred=model.predict(x_test)
test_score=accuracy_score(y_test,y_test_pred)
print('test score accuracy: ',test_score)
#test score accuracy:  1.0 ----> kernel-->rbf
#test score accuracy:  1.0 ----> kernel-->poly , degree=2



#===============================================================
#MLP -->DEEP LEARNING , 6-MLP Multi layer perceptron  --> ANN Artificial neural network(shabakeye asbaie masnooe)


'''

1-Linear (LR)
2-K nearest neihhjbor (KNN)
3-Decision tree (DT)
4-random forest (RF)
5-Support vectgor machine (SVM)
6-....... multi layer perceptorn (MLP)


--> ham baraye classifcation [tadrisa shod --> daste bandi anjam midad] joda miakrd
--->ham baraye regression --> fit mikone



'''


#==================================================================
#Hyperparametr haro chikar konim???????--> mohem tarin ML
#General Workflow --> naghshe 
#classification , regression anjam midahid


#Yek mesal ---> dade haye tajrobi 
#5 T AMODEL RO FIT MIKONIM


#deep learning (MLP)
#project 3 khedmate shoma .....

#-
'''
CROSS VALIDATION 
---> FGHT YEDONE TEST VR NDAR

FK KON 5 TA LAP TOB DARI
TOO YE LAPTOB --> akahrie (noghteye 5 o test bzar m roo 4 ta trian kon )
darsad khatasho dar bair MAPE --> test score 

too ye laptobe dg --> bvia dovomi ro test vrdar ,test score2
......

ta avalin noghtaro test , 

5 ta test score

cross validation --> miangine in 5 taro bgir va tamam -->
test score ---> cross validation test score

5 fold cross validation trest score


yebar train test split konm
k bar train test split krdm ---> bias ro miare paeen
daghigfh tare oon adadet
kazeb nis fgth b avakhere rnage , aavayele range
tamame data ha hadeaghal yekbar test dataset shodn

cross validation




#-------------------------------------------
15 ta data
train test split

3 ta random vrmdiahst  4 , 7 9 test baghie ro train --> train fit --> 4,7,9 mape --> %


k=5 fold --> 
5laptob --> 
1 laptob--> 4 7 9 test baghie train --> MAPE 4%
2---> 11, 14 , 1 --> test baghie train 

5 ta 3 taee test 
3
4
5

score1
scfor2
score3
score4
scoree5

SUM / 5-->mianginesho mide


20 ta data --> 

25% ---> 5 

--> 4 fold 

20 ---> 5   15
   5 15
    5 15
    5 15
    
1 2 3 4 5 ...20 data
5 ta 5 ta ( 1/4 test score)
 4 ta fold
 4 bar boro trian 
 

test_train
cross validation (HAM BARAYE CLASIFICATION accuracy, regression mae mape)

#------------------------ steo 0 - step5 bejaye trian test split --> 5 bar -->miangine 

hyperparameter (classification , regression)

step3-->model selection
model=-.....
too paranetz yekseri paramet k behsh miugan faraparameetr taeen mikaridm
ina ro mdoel ya dnmigire
balke ma midim bvhsh va baes mishe va tasire ziadi oroye yadsgiri daree
va ma hey bayad test konim



1-LR-----------------
Hyperpartemetr ndre
bishtar baraye khati ha hast 
va kh sarii hast vali accuracy paeene


2-KNN-------
kh computational costly --> done done noghat b noghat bayad bre hamsaye haro...
lazy -->tanbalie
hyperparameter----> y seri parmaetr dare dar step 3 model=KNN bayad tooye giome
paramet hasho(faraparameter ,)--> bayad taen koni gahbl az trizaning --> tasire ziadi rooye yadgirish va scoreh drer

n_neighbors   --> integer (1 ta tedade data -1 [30]) hrchi kamtar --> overfit , adad bishtar bashe --> underfit
knn(n_neighbors=)

metric =
knn(metric= '')
'minkowski'  , 'euclidean' , 'manhattan'
fasleey beyne setare he ta hamsaye haro 
5 ta nazdikk




3-DT-------
#taghsim bandi mikrd
#random_state=42 , ... --> hardafe run koni beham nakhore test score
max_depth ta ch omgh bre derakht --> chegahd daste bandi 
1 ta number of vorodi ha 
harhche bishtar --> underfitting ---> overfittiing

min_samples_split --> hadeaghal tedade nemone haee k naiz has ta taghsim kone

(2,5,10) fraction a total sample ( 20  --> 10 , 
                            45 --> 15 , 3 , 5)

min_samples_leaf --> taggsim mikone har soal -_.chanta soal ? (1,2,5)

#ebsanje beyen daste bandia k bbie aya vagehna khob bod eya na shakhesi -->criteration

criterion =
'gini'
'entropy'  ---> sangin tare run




4-RF-------
random_state=42 
n_estimator---> derakht bsaze 10 , 10000 
harchi bishtar behatre ama computatonal mzamane mohjasebat afzayesh mdie va khob 
kam b bala shoro koni


max_features= az vorodi hat y tedadi ro fght vr midare , yekseri az vorodi hat 
gomrah konande bashe , tasir ndshte bashe

tedade vorodi tedad ejadvale 4,5
1 ta teade -1
5 ta jadval vorodi
1
2
3
4

decision
max_depth
min_samples_split
min_samples_leaf






5-SVM-------
kernel --> mibare bdo ebalatar 
'linear'  khatiu
'poly'   chan jomle daraje 2 , daraje 3 va va va...
'rbf'  non-linear



C--> (0.001 o 1000)  small --> underfit  large-->overfitt
gamma--> 0.0001 to 1 --> small--> underfit , large-->ovberfit

vase poly
degree---> 2 , 3, 4,




#-----------------
cross validation --> bejaye inke test train split --> kfold
hyeprparemetr -->  range hay emokjtalefesho --> hey emtehan konim

in dota kar ro baham anjam bdim



gridsearchCV


gridsearch --> done done hyperparameter haye motefavet (model ba parmetr motefavet) -->trian dadam va bhtrin ro vardashtam
cross validation --> na fght rooye 20% data 4 train 1 test . baray edone done fold ha anjam dadam



'''


#-----------------------------------------------
#knn n=1 n=2 n=3 n=4 n=5 ...test score hesab konim??
#behtrin kodome
#bad bgim ahan ien??

#Sade tarin ravesh ---> Gridsearch
#step0------------------------------------------
from sklearn.datasets import load_iris
iris=load_iris()
#4 ta sotooon, yedone khorojhi dasht
# TOOL ARZ SEPAL , tool arzx petal 
#Khoroji -_> esme gol 0 1 2 3 no gol
#daste bandi classsification

#atep0 ---> data cleaning

#step1-->x , y
x=iris.data
y=iris.target

#step2----> train test , cross validation 
#az train_test_split -->yekabr split taghsim mikone
#kfold tabeye dgas esteafde koni
#
#advanced
#baste b magahle ee 
#-->train test
#if > 2 

from sklearn.model_selection import KFold

kf= KFold(n_splits=5,shuffle=True,random_state=42)

#step 3
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier() #hyperparameter bdm man y range ro mikham bsanjam
my_params= { 'n_neighbors':[1,2,3,4,5,6,10],
            'metric':['minkowski'  , 'euclidean' , 'manhattan'] }


#step4---> #khdoe mdoel ro fit konm
from sklearn.model_selection import GridSearchCV

gs=GridSearchCV(model,my_params,cv=kf,scoring='accuracy')
#aval mige modeleto bde

#natije-->lope kalam-->behtarin hyperparemetr ro peyda mikone
#va bahash mire rooye kole range motabar tarin score ro mide


gs.fit(x,y)


#tamam


#step5---------
#tgoo dele gs kh hcizie
#in hamon modelemone

gs.best_score_ # 0.9733333333333334  % accuracy
gs.best_params_
#{'metric': 'minkowski', 'n_neighbors': 4}

#azash estefade koni va predict

gs.predict(np.array([5,3,1,0.2]).reshape(1,-1))
#0 --->gole




#========================
#framworke man


#step0-------data cleaning
#dropna , ......

#step1---> x , y
x=iris.data
y=iris.target


#step2** ----> kfold
from sklearn.model_selection import KFold
kf= KFold(n_splits=5,shuffle=True , random_state=42) #yekabr rtain test split motamen ta rmisahe score


#step3 **--<>model selection with hyperparemetr
from sklearn.svm import SVC
model=SVC()

my_params={ 'kernel':['poly','rbf']}

#step4--->fit
from sklearn.model_selection import GridSearchCV

gs=GridSearchCV(model,my_params,cv=kf,scoring='accuracy',return_train_score=True)

gs.fit(x,y)
 
gs.best_params_ #Out[37]: {'kernel': 'poly'}
gs.best_score_ #Out[38]: 0.9733333333333334
cv=gs.cv_results_


gs.predict(x_new)



#-------------------------------------
#Mesal regression ro 



f_path='/Users/apm/Desktop/MAIN/Shadab Bagheri/3d printing-First phase/Data/final data.xlsx'

import pandas as pd
data=pd.read_excel(f_path)

data.info()

'''

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 23 entries, 0 to 22
Data columns (total 13 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Unnamed: 0   0 non-null      float64
 1   Unnamed: 1   21 non-null     object 
 2   Unnamed: 2   21 non-null     object 
 3   Unnamed: 3   19 non-null     object 
 4   Unnamed: 4   19 non-null     object 
 5   Unnamed: 5   19 non-null     object 
 6   Unnamed: 6   16 non-null     object 
 7   Unnamed: 7   16 non-null     object 
 8   Unnamed: 8   16 non-null     object 
 9   Unnamed: 9   18 non-null     object 
 10  Unnamed: 10  18 non-null     object 
 11  Unnamed: 11  18 non-null     object 
 12  Unnamed: 12  18 non-null     object 
dtypes: float64(1), object(12)
memory usage: 2.5+ KB
'''

data.columns
'''
Index(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4',
       'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9',
       'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12'],
      dtype='object')
'''


#removing columns and rows
data.drop(columns=data.columns[0],inplace=True)
data.drop(columns=data.columns[0],inplace=True)
data.drop(columns=data.columns[0],inplace=True)

a=data.loc[4]
data=data.set_axis(a, axis="columns")


data.drop(index=0,inplace=True)
data.drop(index=1,inplace=True)
data.drop(index=2,inplace=True)
data.drop(index=3,inplace=True)
data.drop(index=4,inplace=True)


#4 ta tekrari
data.drop(index=15,inplace=True)
data.drop(index=16,inplace=True)
data.drop(index=17,inplace=True)


data.reset_index(inplace=True,drop=True)


data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 15 entries, 0 to 14
#15 ta nemone dari 10 ta sotoon
15 nbon-null --> na empty
Dtype-->float (adad)
object 

wrong format

Data columns (total 10 columns):
 #   Column                    Non-Null Count  Dtype 
---  ------                    --------------  ----- 
 0   Nozzle size               15 non-null     object
 1   Infill Percentage         15 non-null     object
 2   Raster Angle              15 non-null     object
 3   Pore size (mm2)           15 non-null     object
 4   NEW PORESIZE              15 non-null     object
 5   SHAPE FACTOR              15 non-null     object
 6   porosity(%)               15 non-null     object
 7   Modulus(MPa)              15 non-null     object
 8   Strength(MPa)             15 non-null     object
 9   Specific Strength(MPa/g)  15 non-null     object
dtypes: object(10)
memory usage: 1.3+ KB


to_numeric

'''

data['Nozzle size']=pd.to_numeric(data['Nozzle size'])

data.info()
# 0   Nozzle size               15 non-null     int64 
data['Infill Percentage']=pd.to_numeric(data['Infill Percentage'])
data['Raster Angle']=pd.to_numeric(data['Raster Angle'])


data['Strength(MPa)']=pd.to_numeric(data['Strength(MPa)'])

#3 ta vporodi
#1 done khoroji

#4 ta soton
#empty , wrong format, logic 
#
data.describe()
'''
4      Nozzle size  Infill Percentage  Raster Angle  Strength(MPa)
count    15.000000          15.000000     15.000000      15.000000
mean    400.000000          50.000000     90.000000      31.377948
std      84.515425          16.903085     25.354628      14.434741
min     300.000000          30.000000     60.000000      10.280775
25%     300.000000          30.000000     60.000000      19.220423
50%     400.000000          50.000000     90.000000      33.654109
75%     500.000000          70.000000    120.000000      41.445994
max     500.000000          70.000000    120.000000      54.553934

'''
'''
for i in 'nozzle size' <100 :
    drop
'''



#step 1----> x o y
#x --> 3 ta vorodi 3 ta soton nozle size, infil percentrae , angle
#y --> 1 khoreoji strength

x=pd.concat([data['Nozzle size'],data['Infill Percentage'],data['Raster Angle']],axis=1)
y=data['Strength(MPa)']

#15 ta nemone dram
#x ham 3 ta soton dare tooye 3 ta nzole size, angle , infil percnetrage
#y -->estehkam

#haadasf---> rabetey beyne process parameter --> estehkam

#peyvaszte---> ML REGRESSION



#step2-----------------train test split 15 --> 3 taro etst
#train test split (x,y, shuffle=true) --> x_trian,x_test,y_train,y_test impact factor --> score chon fght 3 taro az ye nahie random vrmiadre test score , traIn score gahbeel trustable
#creoss valdiation #15 taro 5 ta fold
#5 bar train anjam bde
# 5 ta test score
#mean --> cross validation
#advance train test split

from sklearn.model_selection import KFold

kf= KFold(n_splits=5,shuffle=True,random_state=42)


#step3---->model selection
#regression
#LR , KNN, DT, RF, SVR 
#KNN KNNclasifier
#KNNREGRESSOR

from sklearn.neighbors import KNeighborsRegressor #na KNeighborsClassi
model= KNeighborsRegressor()
#hyperpaarmeetr , neighbor , metric

my_params= { 'n_neighbors':[1,2,3,4,5,6,10],
            'metric':['minkowski'  , 'euclidean' , 'manhattan'] }

#step 4---> fit

from sklearn.model_selection import GridSearchCV

gs=GridSearchCV(model,my_params,cv=kf,scoring='neg_mean_absolute_percentage_error')
#return_train_score =True
#n_jobs--> chanta cpu tedade bebari bala 1 done , movazi anjam mdie va sari tar anjam
#n_jobs=-1 ba harchi tedade cpu mojode


#tooye qutation ' '
#mae ---> neg_mean_absolute_error
#mape --> neg_mean_absolute_percentage_error
#mse --> mean_squared_error


gs.fit(x,y)
#anjam shod


#regression --:> manfi 

gs.best_score_ #-0.5516855803934992
gs.best_params_ #{'metric': 'minkowski', 'n_neighbors': 6}

#yani KNN n 6 bzari metric minkowski , behtrin resulto mide va bhtrin resultet ham hast 0.55 % khataaaaa

#in details
cv=gs.cv_results_

#gs.predict() use




#step3------
from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor(random_state=42)
my_params={ 'max_depth':[1,2,3,4,5,6,7,10]}


gs=GridSearchCV(model, my_params,cv=kf,scoring='neg_mean_absolute_percentage_error')

gs.fit(x,y)


gs.best_score_
#Out[73]: -0.16951149579190386
#85 % deghat




from sklearn.svm import SVR
model=SVR()
my_params={'kernel':['poly','rbf','linear'],
           'C':[0.001,0.01,1]}
#bishtar

gs=GridSearchCV(model, my_params,cv=kf,scoring='neg_mean_absolute_percentage_error')

gs.fit(x,y)
gs.best_score_
#Out[75]: -0.058819087874948175
#94%
gs.best_params_

#Out[76]: {'C': 1, 'kernel': 'linear'}


#----------------------------------
#rasmmmm

#modelema peyda krdm

#LR, KNN, DT , RF , SVM done doen anjam bdi


#nozzle size  [300 - 500]
#infil percnetage [ 0 , 100]
#angle [60,90,120]


#sakht mishe rasm

#yedone ee
new_x=np.arange(0,100)
y=gs.predict(new_x)
plt.scatter(new_x,y)
#y=gs.predict

#gs.predict( . . .)
def generate_bumpy():
    a1_values = np.arange(200,600, 10)
    a2_values = np.arange(10,100, 1)
    a3_values = np.array([60,90,120])

    a3, a2, a1 = np.meshgrid(a3_values, a2_values, a1_values, indexing='ij')

    result = np.column_stack((a1.flatten(), a2.flatten(), a3.flatten()))

    return result


input_space = generate_bumpy()
input_space.shape #(10800, 3)

#10800 radif  3 ta sotoon


y_pred=gs.predict(input_space)
#10800 nemone k baryad test too snaie pishbini krd

#60 zavia 60
#harchi k zavaish 690  ero jod askrdm
#sotone aval inozzle size xx1
# infill percnetage xx2
#yy --> khorojime


xx1=input_space[0:3599,0]
xx2=input_space[0:3599,1]
yy=y_pred[0:3599]


#tooye fght zavie haye 60 
#biam estehkam ro bar asase nozzle size, infil percnetage rams konm

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

#inja
#x y z
# x y z ba hci rang kone
scatter = ax.scatter(xx1,xx2,yy, c=yy, cmap='viridis', marker='o')

# Set labels
ax.set_xlabel('Nozzle Size')
ax.set_ylabel('Infill Percentage')
ax.set_zlabel(f'estehkam')
ax.set_title(f'modele class')
# Add a colorbar
cbar = fig.colorbar(scatter, ax=ax, pad=0.1, shrink=0.8)

# Show the plot
plt.show()


#scatter(x,y)---> 2 D

#pishrafte --> sample dashte bashid

#===============================================
#===============================================
'''
PROJECT A3-----------------

entekhab konid classification , regression 
#harki harkdoom ro khasts











ML SUPERVISED -->ENGINEERING
millions , billions data

deep learning + mlp --> advanci introduction 
videoye  nimsaat khedmat ersal 



'''

#------CLASSIFICATION------ A3

from sklearn.datasets import load_breast_cancer

data=load_breast_cancer()

#havie 
x=data.data
y=data.target




'''

569 ta biamr boodan
har bimar ye ax az sine ash grfte 
azin ax 30 ta vizhegi , ghotre ghode , noore ghode , .. shoae ghode , .... 
tooye 30 ta jadval gozahstanb

va jolosh kh sade
khosh khime ya badkhim

step0 niazi nist
info ()
describe()


'''

data.feature_names

'''
array(['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error',
       'fractal dimension error', 'worst radius', 'worst texture',
       'worst perimeter', 'worst area', 'worst smoothness',
       'worst compactness', 'worst concavity', 'worst concave points',
       'worst symmetry', 'worst fractal dimension'], dtype='<U23')
'''


data.target_names
#array(['malignant', 'benign'], dtype='<U9')

#0 -->malignant --> badkhim
#1--->bengin-->khosh khim

#step1 --> x , y bala atbdil krdm
#step2---> kfold 
#step3--> model , my params [ Logisticregression , Kneasresthclassifier, Decisiontreeclassifier, Randomforestclassdifier, SVC] parametr , hypaerparmaetr 
#step 4--> Gridsearch gs.fit() ---> baraye har model best score ro dar miari 
#va natije migiri k kodooom bhtrin pishbini ro dare
#scoring='accuracy' ----> nahayta
#gs.predict() rasm mikoni 
#yek vordi bar asase vorodie dg  





#=========regression======

from sklearn.datasets import fetch_california_housing

data=fetch_california_housing()



x=data.data
y=data.target


data.feature_names

data.target_names

'''
20000 khone hast 
8 ta maoleagsho rftn vase harkhone darovordn
['MedInc',
 'HouseAge',
 'AveRooms',
 'AveBedrms',
 'Population',
 'AveOccup',
 'Latitude',
 'Longitude']


y--->gheymate oon khone
'MedHouseVal']
    
    200000 khone
    
    
betoni rabete beyne in khone moalefe haro ba gehymate khone dar bairi
'''

#step0--> cleane hame clean --> 
#step1---> x , y bala anjam dzadasm
#step2--> kfold
#step3--> model = [linearregression, knnregressor, decisiontreeregressor, random forest regressor, SVR]
#step4--> gridseachcv --> scoring=mean_absolute_percentage_error --> MAPE
#baraye hare model va aprametr 
#behtrin mdoel best_score_ --> mape ro hesasb mikoni

#dar nahayt migi ko0dom  model bhtrin pishbini ro darer
#va ghyeymat ro bnar asase yek kodom az moalefe ha rasm mikoni (pishbinish ro)



#**** bejaye inek dakheel spyderfile .py bznid


'''

ADVANCED ---> LL_ADVANCED ersal mishe --> bad az inke roo in hite ha kar krdi --> file marjaee
LL_DEEP_LEARNING ---> 30 Minutes --> tadris kardam + deep learning ,....... alaghe mandan *****
A3_PROJECT --> LINKESHO  reposotory --> github ersal krdin --> change , ... vali ta dead linead 
file akahro downloadesh  --> telegram 

Deadline--> Final1 , final2 --> hale yek masale ye regresssion bostoun_house -->
sklearn.datahouse
workflow........




'''





