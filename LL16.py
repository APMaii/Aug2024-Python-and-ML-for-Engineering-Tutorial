
"""
In The Name of GOD

Created on Sun Sep 29 18:05:05 2024

@author: Ali Pilehvar Meibody

LL16 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data=pd.DataFrame([[10,3000],[20,4322],[30,4334],[40,5722],
                [50,6200],[60,6999],[70,8300],[80,9000]],columns=['speed','estehkam'])



plt.scatter(np.array(data['speed']) ,np.array(data['estehkam']))
plt.title('data ha')
plt.xlabel('speed')
plt.ylabel('estehlkam')
plt.grid()
plt.show()



#------------MACHINE LEARNING---------
#1-SUPERVISED  TAHTE NEZARAT
#2-UNSUPERVISED  GHEYRE TAHTE NEZARAT
#3-REINFORCEMENT   TAGHVIATI



#----DAKHELE SUPERVISED
#BAR ASASE KHROOHJI (Y) PISHBINI 2 DASTE HATS

#1-KHOROJI PEYVASTE BASHE 43.4 45.6 33300 -->REGRESSION ML
#2---> GOSASTE BASHWE CLASIFICATION ml (DASTE BANDIE


#hamechiz yeksane fght model ha esmeshon frgh dre




#----------STEPS
#step0====================================
#cleaning 
data.info()
#drop 
#dropna
#fillna 
data.describe()
data.duplicated() #ag row radifi rtekrari bashe mige true
#data.drop_duplicates()

new_data=data.drop_duplicates()
nn=len(data) - len(new_data)
print('in data ',nn, 'ta duplicated (tekrari) dare')


#===============================
#Step1======================================================
#data--> x o y tabdil koni
#nokat--->
#hatman x o y et numpy array bashe -->choon sorate array az tamame mavarede digar bishtare

#agar x et 1 soton bod fght --> az reshape(-1,1) estefade kon  . ag yek soton abshe --> np.array 1d , ba reshape 2d 1 sotoon chanta radif
x=np.array(data['speed']).reshape(-1,1) 
y=np.array(data['estehkam']) #bbinim gosaste hast ya peyvaste--->toye stepe 3



#step2==========================================
#in x o y ro b train test -->badesh y dataset bename test dahste bashim
#k btoonim b onvane yek dadeye jadid va unseen and new estefade konim azash baraye
#validation-->etebarsanjie modelemon

from sklearn.model_selection import train_test_split
#x_train, x_test , y_train , y_test = train_test_split(x,y,test_size=0.25,shuffle=False) 
#az tahe vr mdiare


x_train, x_test , y_train , y_test = train_test_split(x,y,test_size=0.25,shuffle=True) #random_state=None
#harbar k run mikoni mire ychi vr midare 
#yebar 2 taye akha r, run mikoni dotaye vasati
#4.34%
#4.28% 

#shuffle-->True-->agha az tahesh var ndre --> boro random entekhab kon, random_state ye adad mziri har dfe run mikone 4 o 9 ro vrdare
#ta abad 4 o 9 ro vrdare harki mikhad run bzen

x_train, x_test , y_train , y_test = train_test_split(x,y,test_size=0.25,shuffle=True,random_state=42) 




# x , y train
# x , y test -->kenar (badan azash estefade koni)


#ch baray classification , regression


#dataye aslie man ine
plt.scatter(x_train,y_train)
plt.title('DATA')
plt.xlabel('speed')
plt.ylabel('estehlkam')
plt.grid()
plt.show()






#rasmesh baham
plt.scatter(x_test,y_test,label='test dataset')
plt.scatter(x_train,y_train,label='train dataset')
plt.title('DATA ')
plt.xlabel('speed')
plt.ylabel('estehlkam')
plt.legend()
plt.grid()
plt.show()



#step3======tarife model
from sklearn.linear_model import LinearRegression
model=LinearRegression() #aval mdoeleto tarif mikoni

#model=DecisionTree()
#model=RandomRegressor()
#model=SVR()



#6 ta model
#1-LINEAR MODELS (kahti)
#2-K nearest neihghboru (KNN)
#3-Decision Tree (DT)
#4-Random Forest (RF)
#5-support vector machine (SVM)
#6- MLP (multi layer perceptron)

#ham barayre regression
#ham baraye classifcation

#1-LINEAR MODELS (kahti)---> hey a o b ro randm
#hoshamnd (gradiant descent )--> a ob haye mokhtaelf ro test mikrd
#hey kaht y=a*x+b
#vas eharkodom cost value hesba mikrd
#paeen tarin cost value---> a o b sh ro vr dmidahst
#Migof in hamon khatie k rabetey asli azash peyravi mikone

#raveshe Linear khati
#KNN, DT , RF , SVM , MLP ravesh haye khdoehson
#bejaye inke a o b bzne ,..........



#steo4----fitting
model.fit(x_train,y_train)

#inja LR khatie, 5 ta model
#tooye fitting oon rabete ro dar miare

a=model.coef_ #a
b=model.intercept_ #B
print('shibe khate man hast : ', a , 'va arz az mabda hast' ,b)
#steo 5--

#adado migire mzire too in rawbete behet pas mide
model.predict(np.array(13).reshape(-1,1)) #3123.738]
model.predict(np.array([13,17,39]).reshape(-1,1)) #array([3123.738, 3476.482, 5416.574])
#rams anjam va va va ....
#ghable hameye in chizzaa
#ghable estefadee az model --->
#sehate modelet ro besanji
#validation (etebar sanjie model)

x_new=np.arange(0,100).reshape(-1,1)
y_pred=a*x_new+b
plt.scatter(x_train,y_train,label='training data')
plt.plot(x_new,y_pred,label='predicted line')
plt.title('Data')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.legend()
plt.show()


#in rabteeye asli injast

#yeki mgie agah man ghabol ndrm boro test kon
#ch testi? mige do noghte boro azmayehsgah
#noghteye masalan 20 , 60 
#bde b model model mizre tooey oon rabete --> y ro mide y_pred
#hala ba y e vagehi -->too azmayeshgah bdast maid moghasyese kon


#man mgm sab kon nmikha dbri 
#man ghablesh b fkr boodm 2 ta data ro gozahstam kenar (test dataset)
#


#------5-----validation
#modlemon k amade hsode 2 ghesmat dre
#1--->aval baya dbbinm rooye hamon train dataset khoob fit shode?
#asan tooenste jkhob model beshe? khoob tonese rabete he ro bdast biare
#yani in noghat holo hosh rooye oonb khat hastan?

#train score ---> data hae k train , score 

#2---> unseen data new data behesh bdim ? -->
#Mitone pishbini kone?-->prediction bbinim (ghodrate pishbinie model)

#test score---> oon noghate test (unseen, new data) --> mitoen khob pish bini kone?


#validation 2 ta score report koni
#train score (neshooneye fitt, modeling)
#test score (nehsone ye prediction ,pishbini)


#3 halat dare------
#train score kh paen bashe--->test score paeen-->underfitiin yad ngrfte , 
#train score kh balaee--> noise , error too data yad grfte--> test score biad paeen--->overfittiing
#sweat point --> noghte ye optimum talae-->ham train score, ham test score bala bashan -->injaeem


#regression----->peyvaste hats ashsari hatsam ,tni kam koni
#ag regression -----> MAE , MAPE , .... MSE , RMSE
#mige 
#donabel ekhtelafe pishbini shodie ba vageh ei (y_true , y_pred)
#MAE--> MEAN ABSOLUTE ERROR
#MAPE -->MEAN ABSOLUTE PERCENTAGE ERROR
#MAE--> ekhtelafe in dota noghtaro motlagh dar nzr bgir y_TRUE-y_pred --> modele man ekhtelafe pishbinish inghdre 200 tas , adadi pishbini kard +- 200
#MAPE--> boro y_true-y_pred / y_true --> darsadi mdie--> chan darsad pishbini hay emdoelet motefavete +- 2% +-5%
from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import mean_absolute_percentage_error 

y_pred=model.predict(x_train)
train_score=mean_absolute_error(y_train,y_pred)
print(train_score) #169.2400000000001
#agha in 6 ta noghte ro model eman roshon fit hsode
#va pishbini mikone+-169
#0.00000032
#0.00000017

#darsadi
train_score=mean_absolute_percentage_error(y_train,y_pred)
print(train_score)
#0.033878970810629905
#mdoele man +-3 % khata dare -->train score



#train score--> in 6 ta nogthe k dadam bhsho , mdoele man az roo hamash ra dnashode ke
#khatesh fitting curve , +-3 % ekhtelaf dre
#hame rooye oon khat ......



#pishbinish chtore??
y_pred=model.predict(x_test) #Noghte ee hast k ndidi
test_score=mean_absolute_error(y_test,y_pred)
print(test_score)
#425.22
#mdoele man +-425 har adadio k nadide va pishbini kone +_425 fasele dre


test_score=mean_absolute_percentage_error(y_test,y_pred)
print(test_score)
#0.08646094679090467

#mdoel eman da mogahbeel dade haye jadid +-8 % khata darad


#classification mishi-----------------
#ekhtelaf mohem nis
#tooye stepe 3 modelo mizdi 
#modela
#KNN -->KOLIE
#KNNREGRESSON
#KNNCLASSIFICATION
#YEKSANE

#validation , etebar sanii
#peyvaste k nis biay y --> 4433.43 ekhtelaf hesab

#balke kolan daste bandi dari mikoni
#y hat 0 1 
# 1 2 3 
#narges maryam
#khosh khom bad khim

#dar enteha-->modelet -->
#behesh vorodi bdo , bge kodom dastas
#sag gorbe
#roze , narges
#khsohkhim badkhim
#0 1 

#kodom daste gol
#narges , roz , holandi, ....
#0 1 2 3 4 5 
#to adadi ro pishbini nmikoni
#daste ro pishbini mikoni

#moheme k chanta doro spishbini karde
#az har daste chand doone doros pishbini krde
#chan darsad az noghat ro doros pishbini krde

#ekhtelaf nisii XXX

#confusion matrix
#accuracy

#tool , arz golharo bgirim jolosh bnvisi gole narges , roz 
#b narges bgim 0 , roz 1

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

plt.scatter(data['tool'],data['arz'],c=data['noe_gol'] , cmap='viridis')
plt.title('gol ha')
plt.xlabel('tool')
plt.ylabel('arz')
plt.show()

#step0 cleaning
#step 1 x , y
#step 2 trian test
#step3 model selection (hamon 6 ta model , classficier)
#step4 fit
#step 5 valdiation ( frgh , bjaye MAE, MAPE , confusion matrix accuracy hesba mikoni)

#classifictaion, regression
#Modele ma donable in noist k fit bshe rooey data ha ta rabetey beyne x o y ro bde
#donabel rahi hast btone beyne daste ha tafavot iajd kone va tashkhis bde
#x haro bdi , haeli  yek marzi dahste bashe bar asase on tasmim bgire
#k y eshoma , gole shoma , ... jozve kodom dastas



#-------step0
#clean

import numpy as np
#step1--->x o y
x=np.array(data[['tool','arz']]) #reshape nmikhad 2 ta sotoon
y=np.array(data['noe_gol'])



#step2------- test train
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25, shuffle=True, random_state=42)


plt.scatter(x_train[:,0],x_train[:,1],c=y_train , cmap='viridis')
plt.title('TRAININGGGGGG gol ha')
plt.xlabel('tool')
plt.ylabel('arz')
plt.show()



plt.scatter(x_test[:,0],x_test[:,1],c=y_test , cmap='viridis')
plt.title('TESTTTT gol ha')
plt.xlabel('tool')
plt.ylabel('arz')
plt.show()

#dar akhar model ma ghrar ebeiste jolot bege agha jan
#bmna vorodi bde (tool , arz) khrooji midm (migm az kodom dastas)

#3------model selection
from sklearn.linear_model import LogisticRegression
#bejaye Linearregrssion -->in baraye dade haye peyvaste hast
model=LogisticRegression()
#linear baraye regrasioon
#c;lassification daste bandie


#khat haye motefavet miekshe k in beyn biad 
#yek fasele bndaze , dast ebandi kone

#4---training . fit
#training


model.fit(x_train,y_train)




#-----5 validation
#ma donbale ekhtelaf nisim mese regression

#y_pred y_true
#peyavste -->4580  4440


#daste ha 0 1 
#miokhay bbini az 8 ta trainet , 3 ta testet , chantasho doros pishbini krde
#chantasho doros 


#----------
y_pred=model.predict(x_train)

from sklearn.metrics import accuracy_score

train_score=accuracy_score(y_train,y_pred)
print(train_score)

#1.0 -->100%
#100 % in 8 taro doro spishbini krde oon khate


#test score
y_pred=model.predict(x_test)
test_score=accuracy_score(y_test, y_pred)
print(test_score) #1.0
#100 % in 3 taro doros zade



#ekhtelaf mAE, MAPE
#DARSADE SEHAT -->mese regression darsade ekhtelaf nis
#darsade sahih pishbini krde modele
#100 % tamame daste haro doros pishbini krd


#500 biamr saratani darim
#1--> 500 ta biamro doros pishbini krde k khosh khiman ya badkhim




#accuracy __. doorost pishbini shode ha / tamame halat ha 

#---> doros pishbini + ghalat pishbini





#accuracy --> 95 %
#--->5 ghalat pishbini krde



# 95 % doros 5% ghalat



#5% ghalat bri 
#khode ghalat ro ham vashekafi koni



#500 bimar  --> 0 1     0 badkhim 1 khoshkhim
#ax haye ct scan 


'''
ghotre ghode       arze ghode   masahate ghode    tashkhis
43.2               5.3           120               0(badkhim)
...
...
....
..




#x--->y
ct scan-->x
tashkhis -->y


train test 500 ta biamr
50 ta ro mizrm kenar


50 ta test dataset -->bimaraye jadid



model fght 450 ta biamr mibine pishbiisho kone
50 ta biamr ejadid midm y hasho drm, x hasho
model.predict(x_test) -->y_pred

y_true (y_tets)

classification
az 50 ta chantasho doro sgofte
45 tasho


90%
10% ghalat pishbini krde (tamoom nmishe)-->accuracy

TP ---> vaghean badkhim bodn va badkhim pishbini
TN --> vaghena khsohkhim bodn va khoshkhim pishbini krdim

accuracy = TP + TN / ALL
pishbini haye true

45 doros psihbini karidm / 50 


#ghalat pishbini krdn -->false


5 ta bimaro ghalat zade -->

FP khosh khim bodan , badkhim pishbini krdim
FN  badkhim bidan , ma khoshkhim pishbini kridm



all= TP+TN+FP+FN

TP
TN
FP
FN



accuracy--> TP + TN / TP + TN + FP+FN
True / ALL
0.95 --> 95 % kole pishbini ha doro sbode
% drs dkhata





dota mdoelan 5 ta khata tashkis dadan ok?

yekodom 5 taro FN --> ina khoshkhim bodn badkhim ---> hazine tarashid eshode , khoshkhim biodn , modele man ehsetbah badkhim , ....


yekodom dg model 5  FP --> badkhim bdon , model man khsohkhimgofte ---> 5 ta marg


migm dot amodel accuracy 90% yeksan nis
shoma naiz dari bdone False ha ya error ha
FP , FN (tooye pezeshgki, hasas)

fght b accuracy_score ektefa nmikone


confusion_matrix



'''


from sklearn.metrics import confusion_matrix

y_pred=model.predict(x_test)
score=confusion_matrix(y_test,y_pred)

print(score)
[[2 0]
 [0 1]]




'''


                     vaghean class 0   vaghean class 1
pishbinie class 0        TP                 FN             
pishbinie class 1         FP                     TN


[[2 0]
 [0 1]]


                true class0     true class 1
pred class 0     2               0
pred class 1     0               1



2 ta goel 0 bodn ( roz) --> 2 gole 0 awlie
1 gol ham 1 bode (narges)---> naregs ham pishbini shode


3/3 --> 1 accuracy
porecision
f_score


confusion_matrxi yek pele jolo tar az accuracy hast abraye classification





'''

a=model.coef_
b=model.intercept_


print(a) #[[1.12270329 0.59196494]]
print(b) #[-5.74065762]


x_min,x_max=x[:,0].min() - 0.5,x[:,0].max() + 0.5
y_min,y_max=x[:,1].min() - 0.5,x[:,1].max() + 0.5
xx,yy=np.meshgrid(np.linspace(x_min, x_max,200),np.linspace(y_min,y_max,200))
z=model.predict(np.c_[xx.ravel(),yy.ravel()])
z=z.reshape(xx.shape)
plt.scatter(x_train[:,0],x_train[:,1],c=y_train , cmap='viridis')
plt.contourf(xx,yy,z,alpha=0.2,cmap='bwr')
plt.show()




#+==================================
#KNN

#DT
#RF
#SVM


#---2-KNN --> Regression , classifiction

#step0----
#cleaning
#step1--->x , y
#step2--> train , test
#setp33-->model selection
#step4-->fitiiing
#step5-->validation

#step0--cleaning-----

#step1--->x o y------------
x=np.array(data[['tool','arz']]) #reshape nmikhad 2 ta sotoon
y=np.array(data['noe_gol']) #--->gosaste

#step2----------------
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25, shuffle=True, random_state=42)

#step3-------------
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neighbors import KNeighborsRegressor
#jfoteshon KNN -->classifictaion , regression nesbat b y 

model=KNeighborsClassifier()
#KNN, DT, RF, SVM, MLP ,.....
#ingdh sade nis k bzari fitt she

#yechizaee
#paraemter
#hyperparameter (faraparameter)

#Model ha az ravesh haye khdoeshon
#raveshe a o b
#setare hamsaye 
#......
#parametr haero yad migiran
#ama hyperparameter (faraparameter) -->parametrhaee hastan k dar toole trianing
#yad grfte nmishavad
#balke bayad ghabel training b model dade shavad (khdoemon bayad bdim)
#motasefane -->tasire besezaee bar amalkarde model dare

model=KNeighborsClassifier(n_neighbors=)
#k ya n_neighbout
#bayad bgi vaghty mikhd rang amizi kone
#chnata chanta hamsaye ro bbine va oon nogthe ro rng kone?
#1?-->valino bbine sarian 
#try test 

model=KNeighborsClassifier(n_neighbors=1)
#too khdoe jae k model selection -->tarife modle mikonim baya dhyperparameetresho bznim


#step4--fiting
model.fit(x_train,y_train)
#model-->predict mitoni pisjhbini koni abd az training


#step5---validation

#5.1.training

y_pred=model.predict(x_train)
train_score=accuracy_score(y_train,y_pred)
print(train_score) #1.0



y_pred=model.predict(x_test)
test_score=accuracy_score(y_test,y_pred)
print(test_score) #1.0



#-----COMPACT
x=np.array(data[['tool','arz']]) #reshape nmikhad 2 ta sotoon
y=np.array(data['noe_gol']) #--->gosaste
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25, shuffle=True, random_state=42)
model=KNeighborsClassifier(n_neighbors=6)
model.fit(x_train,y_train)
y_pred=model.predict(x_train)
train_score=accuracy_score(y_train,y_pred)
print(train_score) 

#n=1 -->1
#n=5 -->1.0
#n=7 --> 1
y_pred=model.predict(x_test)
test_score=accuracy_score(y_test,y_pred)
print(test_score) #1.0




#mesal yekam vaghe ei tar she

#step 0 too khode sklearn

from sklearn.datasets import load_iris
iris=load_iris()


#sklearn. madule datasets -_>too delsh koli data hast


#step 1 --->
#dasti, miam az sklearn
#object iris --> too delesh data target

x=iris.data
#4 ta soton 150 ta
#nmdionm
print(iris.feature_names)
#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

#baraye 150 ta gol done done arzo toole sepal o petal
#4 ta adad baraye ahr gol

y=iris.target
#0 1 2 gosaste
print(iris.target_names)

#3 ta goaln
#0           1             2
#['setosa' 'versicolor' 'virginica']

 

#x o y ro darim
#step1


#step2
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25, shuffle=True, random_state=42)

#38 ta golo test
#112 taro train -->model



model=LogisticRegression()

model.fit(x_train,y_train)


y_pred=model.predict(x_train)
train_score=accuracy_score(y_train,y_pred)
print(train_score) 
#logisticregression=0.9642857142857143 %
#96% az 112 ta goli k bhsh dadim ro doros pishbini krde k kodom yek az 3 t agole



y_pred=model.predict(x_test)
test_score=accuracy_score(y_test,y_pred)
print(test_score) 
#logisticregression=1.0
#az 38 ta gole test hamaro doros gofte


#-------modele badi
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=10)

model.fit(x_train,y_train)


y_pred=model.predict(x_train)
train_score=accuracy_score(y_train,y_pred)
print(train_score) 
#n=1 ---->1.0
#n=5 --> 0.9642857142857143
#n=10 --> 0.9642857142857143


y_pred=model.predict(x_test)
test_score=accuracy_score(y_test,y_pred)
print(test_score) 
#n=1--> 1.0
#n=5 -->1

#-----dar in dataset -->
#harchi n bishtar bshe --> train score yadgriie man badtar mishe
#tedade ziadi hamsaye varmdire
#oon marzaro nmitone doros tashkhis bde

#n -->bishtra msuhe aabdtar mishe
#in natije giri hamsihe sadegh nis


#bayd baraye har modle, baraye har data -->inkaro anjam bdi




#==============================
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=10)

model.fit(x_train,y_train)


y_pred=model.predict(x_train)
train_score=accuracy_score(y_train,y_pred)
print(train_score) 
#n=1 ---->1.0
#n=5 --> 0.9642857142857143
#n=10 --> 0.9642857142857143


y_pred=model.predict(x_test)
test_score=accuracy_score(y_test,y_pred)
print(test_score) 



#--------Decision Tree----------------
#5 ta step
#model=.....
#hypeeparameter




#---jalase ayande framwork behtrin hyperparameter ...
#rasm haye alsio
#ba yek mesale regression khedmateton zade mishe



#-------------------------------------
#decision tree derakhte tasmim

#criteria (shakhes ha) --> az bala b paeen daste bandi anjam taghsim

#-----4 ta goroh drim mikhaym bbini gorgan , gorbe, sag, oghab
#100 ta data
#----hey soal miporsim

#soale aval--> kodoemshon parvaz mikone va nmikone

#onae parvaz mikonan dasteye chap
#onae k nmikonan dasteye rast

#soale badi-->kodomeshon vahshie
#taghsim
#soal-->

#soal 
#soal
#mikonim

#...... 4 ta dast etaghsim

#hamchiz yeksan ast



#======================
#======3-Decision Tree-------
#----------------------
from sklearn.datasets import load_iris
iris=load_iris()
#step 0 -->Done by sklearn
#step 1 --->
#dasti, miam az sklearn
#object iris --> too delesh data target
x=iris.data
y=iris.target

#step2 test train
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25, shuffle=True, random_state=42)


#step3------
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(max_depth=1,random_state=42)
model=DecisionTreeClassifier(max_depth=3,random_state=42)
model=DecisionTreeClassifier(max_depth=5,random_state=42)

#random_state=42
#DT , RF , MLP


model.fit(x_train,y_train)

y_pred=model.predict(x_train)
train_score=accuracy_score(y_train,y_pred)
print(train_score) 
#depth 1---> 0.6607142857142857
#depth3--> 0.9553571428571429
#depth5 --> 0.9910714285714286

y_pred=model.predict(x_test)
test_score=accuracy_score(y_test,y_pred)
print(test_score) 
#depth1 --> 0.6842105263157895
#depth3--->1.0
#depth5--->1.0




#shoam harchi max depth taghir bdi
#sampel_split (soal azash miporese 2 , 3 ,)
#kh hasaseeee kh hasaseeeee
#baes mishe gahiii shoma hey bri depth done done
#besazi

#bade ...
#vaght gire zaman gire
#BIAS


#============================
#-------RANDOM FOREST-------
#Jangale tasadofi------>

#man miam 100 ta decision tree misazam
#100 ta derakht --->
#hala miam masalan yeki az golat -->mdiam bhsh
#har derakht max_depth, ,........
#random --> max 3  max 5 max 7 min split
#train


#y adadb har 100 ta derakh tmidm
#ydone datamo mdim b random forest
#b 100 ta derakht
#har derakht y pishbni mikone
# yeki hgoole 0 
#gole 1

#bishtarienshon chi migan

#95 ta gole 1 
#5 ta 0 

#--->gole 1


#GENERAL....
#CHEGAHD ROBUST GAHVIE TAre


#aya 100 ta?
#1000 __. computational cost bishtr zaman mibre
#kh memory lazem , ..1000000
#in k chghd bashe harchi bsihtr aksaran 
#computere shoma nmikseh

#tedade derakht daste shoma-->hyperparameetr ---> entkehab koni

#---------RANDOM FOREST
from sklearn.datasets import load_iris
iris=load_iris()
#step 0 -->Done by sklearn
#step 1 --->
#dasti, miam az sklearn
x=iris.data
y=iris.target
#step2 test train
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25, shuffle=True, random_state=42)
#step3------
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(random_state=42,n_estimators=40)
#chanta derakht bsazam?-->n_estiamtors

#step4
model.fit(x_train,y_train)


y_pred=model.predict(x_train)
train_score=accuracy_score(y_train,y_pred)
print(train_score) 
#1.0


y_pred=model.predict(x_test)
test_score=accuracy_score(y_test,y_pred)
print(test_score) 
#1.0


#-------------------------------------

#dar jalaseye badi
#REVIEW ---------
#----+
#SVM --> CLASIFICATION

#------MESALE KAMELAN SANATI --> REGRESSSION
#hyperparameter chiakr konim???? n_neighbout? max_depth? -->

#1-LR
#2-KNN
#3-DT
#4-RF
#5-SVM

#framework
#step , 1 step.......
#RASME NAHAEE 
#FRAMWORK-->KHAT 


#---------
#Introduction on deep learning
#MLP (ANN basic)
#......

#CNN
#GAN
#.... Millions to billions data 


#-----UNSUPERVISED, REINFORCEMENT ...........
#model haye ghavi nadaran 
#thoory .........


#l17 *final




#============quiz
#l16 Q
#formate hamsihegi

'''
iris
x
y


1-Logistic
2-KNN ( ba 3 ta k motevafet)
3-Decision tree ( ba 3 ta depth motefavet)
4-random forest ( ba 3 ta n_estiamtor motevfavet )

10 ta

10 ta train score
10 ta test score
tahesh bdid va yek natije giri kondi k kodom mdoel ghavi atre
rooye dataey iris



4 ta toolo arz sepal va petale yek gol ro dare




'''
from sklearn.datasets import load_iris

iris=load_iris()

x=iris.data
print(iris.feature_names)


y=iris.target
#0 1 2

print(iris.target_names)




#step 0 --->(optional --> np --> dataframe) info , dropna,...
#step ,....
#
#report 20 ta adad va yek paragrpah tozih



#bnzrm shoro konid va ino dakhele 
#github bznid


#jalas ebadi tadrsi\
    #project bayad dar github bargozari shavad

'''

train score

for logistic regression  1
// // // //
for knn with n=1     0.96



test score
...




Conclusion:
    I think the best model is Random forest because
    it can geenralize .....
    
    
Ai.2024.pilehvar@gmail.com

Q_L16_fname_lname

#--------------


'''



 
