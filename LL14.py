
"""
Created on Sun Sep 22 18:01:35 2024

@author: Ali Pilehvar Meibody


L14-------------




kole masaele jahano input-output tabdil konim


assumption:
voroodi va khoroji yek rabet ee dare
input----> box -----> khorooji


box--> AI 
AI az ravesh haee (statistcial) va rabete ro bdast biare
ag rabet ro bdast baire
dg shoam mitoni input bshh bdi khrooji bgiri 



shhod shabieh ensan
yek ensan ba yek maghz
ya bhtre begim
Hooshe masnooe

artificial inteligent
1-data bhsh midiim ( input output )
2-azash rabete he ro yad migire (beyne input o output)
3- bhsh input midi --> output pas mide
adad (azmayeshgah) riazi fizik
tasivr --> daste bandi , hads bzn, pishbini
seda
matn bfrsi matn 
input output



#ghabl az inke varede AI bshim
Regression -->regrassionnnnnn  (ML , AI nist)


#yek sistem darim , 3d printing , ..... mesal
setting daste mae (input) ---> .... ---> quality parameter (adad 3000 4000 , 1.342 0.0001 , khoob bad , 0 1 , A B C D)
rabetey ebyne input va output az raveshi hastim k esmesh regression
Regression miad rabeteye beyne  input va outptu ro dr miare (MESE AI ama AI nist (ma ghabl az AI hastim at alan))


sharhe masale:
    3d printing
    soratesho mitonesim tgfhir bdim (0,100)
    estehkam measure ---> (0,8000)
    7000 mikhaym
    
    data---> 4 ta test anjam dadim 
    
    
asssumption:
    1-rabete ee vpojkdo darad beyne input o output (estehkam = f (sorat))
    2-rabete khati hast 

estehkam=A*sorat + B

A o B ro peyda konim
    va fgth 4 ta noghte darim
    
sorat   Estehkam
10    1200
20    2044
30     4043
40    55000

dg nmitonim hey brim error try error nmishe zmaan gire , hazine bare
aya raveshi hast k in rabetey ebyen estehkam va sorat ro bfhme ( A o B ro dar baire?)

A o B ro ag dahshte basham --> A * soratam + B --> estehkamam

bjaye inke too azmayehsgah soratamo masalan bzaram 80 bad brm estehakmo dr bairm estehkam bdast miad

A va B bdast biad
regression mige man mitooonam Basic Regression


"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#---1 sakhtam
a=np.array([ [10,1200],[20,2044],[30,4043],[40,5500] ])
data=pd.DataFrame(a,columns=['speed','estehkam'])

#----2 real world
#data=pd.read_csv(/ ... /.....csv)




plt.scatter(data['speed'],data['estehkam'])
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
plt.grid()
plt.show()


#----regression
#yek khat5 bekesham 

# y= a*x + b
#ba in fromol mishe hargoone khate safi k bkhay bkshi

#1*x + 0   y=x
#2x

#ba bazi ba a o b 
#khat y=a*x + b mitone tabdil bn har khati bkhay bshe

#algorithm darim miad random hey a o b ro entkehab mikone
#yek bar ye a ye b  a=3 b =6 mikeshatesh
#miad faseleye khat ro ba in noghate vaghe ei (azmayehsgah bdast ooomde) bdast miare --> majmooe morabaat --> jam mikone be tavane 2 e faseleye har noghte ta khataro 
#in yani chi??-->faseleye kole noghat ta khate??
#---> yani 



#--flasshback
#estehkam va speed rabete dashte
#estehkam = A* speed + B
#ma nmidonim in khate kojas
#vali ahrmoghe miri azmayeshgah va azmayehs mikjoni
#har amyaeshet yek nogthte az in khatas + yekma error k dalilesham toee ya azmayeshgah

'''
afg bri 1000 t aazmayesh koni
1000 ta noghte beham chabside dari (khate)
khat ero bdast mairi

hazine , zaman nmizare
dastet bastas




bayad yek raveshi peyda konio fght ba hamin chanta nogthe oon kahtaro peyda kone
regrsssionm

a o b reANdom   cost value (majmooe morabaate fasele ye noghat ta khat -- cheghadr naxdiek khate hast)


100000 a 10000 b  ---> hakrodom cost value  100000c ost

1000 cost --> paeen tarin adad -->paren tarin fasele-->nazdik tarin khat b hame --> kahte aslimon --> raveshe
regression --> hadeaghal majmooe moraabate 
Minimume sum square

pedyash mikoni --> a o b --> A va B


estehkam = A * speed + B


hala khatety amadas hamona slie hamoni
jkahane hasti dastete 


speede --> dkahelesh --> estehakm



'''
a=np.array([ [10,1200],[20,2044],[30,4043],[40,5500] ])
data=pd.DataFrame(a,columns=['speed','estehkam'])

plt.scatter(data['speed'],data['estehkam'])
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
plt.grid()
plt.show()


#a o b ro taghir dadim

#tqasviri geometry
import pandas as pd
x=np.arange(0,100)
y=100*x+600
a=np.array([ [10,1200],[20,2044],[30,4043],[40,5500] ])
data=pd.DataFrame(a,columns=['speed','estehkam'])
x=np.linspace(0,100,100)
plt.plot(x,y)
plt.scatter(data['speed'],data['estehkam'])
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
plt.ylim(0,7000)
plt.grid()
plt.show()

#y=100*x+600
'''
y=100*x + b

hamoon
y= A* x + B

A va B

BASIC REGRESSION

2 farz
htamn rabet ee bashe
hartman khati bashe
yedoone x yedone y

mashin hesab 
'''

#----basic regression 
#yek tabe baramon regression 
#ketabkhone



#sklearn
#scikit learn
#company --> traditional ML
#deep lerning --> tensorflow , keras, pytorch
#NVIDIA geforce 3060 3070 3080 3090 testa v100

#cpu mohasebati ---> aksaran cpu
#Gpu --> tasavir , tasvire graphici


#--------
#pip install scikit-learn

#installesh kon

import sklearn 
#

'''
import libname
import libname as mokhafaf

raveshe 3 -->ketbakhane bozorg mzirn

from libname import func

'''

#modele basic regression estefade koni

from sklearn.linear_model import LinearRegression 
#az dele sklearn 
#yek tabe hast bename LinearRegression
'''
-->sklearn
-------->linear_model

def LinearRegression( , , , ):
    ...
    .
    .
    ...
    ....
    .
    ....
    ....
    .....
    
'''



from sklearn.linear_model import LinearRegression 

#modelet mire tooye yek zarf bname model
model=LinearRegression()
#salam
#khobi
#mymodel
#yourmodel

data=pd.DataFrame(a,columns=['speed','estehkam'])
x=data['speed']
y=data['estehkam']

#mohasedbat ag dari numpy array
#agar xeton yedone ee basher .reshape(-1,1)
#2 ra soton 2 ta vorodi, 3 ta ,.... niazi nsit

x=np.array(data['speed']).reshape(-1,1)
y=np.array(data['estehkam'])


model.fit()


#------------------------------
#review
from sklearn.linear_model import LinearRegression
model=LinearRegression()
x=np.array(data['speed']).reshape(-1,1)
y=np.array(data['estehkam'])
'''
a=np.array([10,20,30,40,50])
a.ndim #Out[22]: 1
b=a.reshape(-1,1)
b.ndim
'''

model.fit(x,y)  #train mide
#yani maid alan 4 ta noghatro dare hey a o b hey a o b ,...... #costr function hesab mikone
#minimu va paeen tarin cost functrion ro peyda mikone
#zaman bar

#hala shoma ychi dariu bename model too delesh koli informationeee
#@bekeshi brion
#tamam

#pishbini
# x--> y bde
#------
#modelemon yek tabe dare benam epredict
#mige agah bman adad bde man pishbini
#x---> y bgir
#speed bde --> estehkam bgir


#spped 50 bbinm estehakm chan mishe

new_x=50 #Mitooni
#hamechio numpyu bdi sorate mohasebat bala bashe

new_x=np.array(50).reshape(-1,1)

y_pred=model.predict(new_x)
#pishbini
#6921.5\
    
#====================
#====================
#====================
#====================


#kole kod kenar eham
#BASIC REGRESSION
from sklearn.linear_model import LinearRegression
model=LinearRegression()
x=np.array(data['speed']).reshape(-1,1) 
y=np.array(data['estehkam'])
model.fit(x,y)  #a b ab cost functin ,... behtarino peyda mikone

#---pishbini
new_x=np.array(50).reshape(-1,1)
y_pred=model.predict(new_x)
print(y_pred) #[6921.5]
#y adad pishbini kone?

#bia rasmehs konim
#-----rahe vaal-------
#dataye vaghei
x=np.array(data['speed']).reshape(-1,1)
y=np.array(data['estehkam'])
new_x=np.arange(0,101).reshape(-1,1)
# 0 , 1 , 2, 3, 4,...,100

y_pred=model.predict(new_x)


plt.scatter(x,y) #y ro bar asase x 4 ta nogth evaghe ha hast
plt.scatter(new_x,y_pred,s=3) #noghate farzi 0 ta 100 , psihbini ha -->pishbini ha
plt.title('avalin regression')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.show()



#model.predict(adad)
#y= A*x + B ---> A*adad + b --> bht pass
#shekli --> 
#khati ma nakehsidim
#100 ta nogthe ro keshidim




#---raveshe dovom------
#Y = A*x + B
# A va B ro bdast ovorde



#too dele mdoel koli informatione

model.coef_ #A #shib #coefficient

model.intercept_ #B #adad ezafe #arz az mabda

#Y = A*x + B
# Y = coef*x + Intercept

A=model.coef_
B=model.intercept_ 

print('my A is : ', A)
print('my B is : ', B)

'''
my A is :  [148.99]
my B is :  -527.9999999999995

'''

#mosadfel asli bdast ovorde

# Y = 148.99 * X -527.999

#Estehkam = 148.99 * speed - 527.999


'''
review
data --> x y dasht
model.fit(x,y)   # regresion grf a o b hey zad cost , minimum ,.. A , B
#Y=A*X + B ---. model.coef_  model.intercept_
#model.predict( new_valu)
#rasm do ravesh


'''
x=np.array(data['speed']).reshape(-1,1)
y=np.array(data['estehkam'])
A=model.coef_
B=model.intercept_
new_x=np.linspace(0,100,1000).reshape(-1,1)
y_pred=A*new_x + B



plt.scatter(x,y) #y ro bar asase x 4 ta nogth evaghe ha hast
plt.scatter(new_x,y_pred,s=3) #noghate farzi 0 ta 100 , psihbini ha -->pishbini ha
plt.title('avalin regression')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.show()



#-----------------------------------------
#basic tnestim
#BASIC REGRESSION RO BEFAHMIM
#LinearRegression()
#class ---> def , adade sabet  #details Advanced

class bank():
    
    def hesab():
        #kjhdjklslsdjsl
        return #idsjslj
    
    def hesab1000():
        #odissoij
        return #dssuhs
    
    sabet=20
    
    
a=bank()

a.hesab()


#100 ta tabe ro brizi dkahele yek class


#LinearRgeression #class koli tabe dare

#fit 

#class to yek chzi  bname model
model=LinearRegression()


#koel nokte-----> model koli tabe tooshe

#yek tabe too dele model hast k vorodi hash x va y hast 
#mire kare regression ro anjam mide

model.fit(x,y)

#vaghty tamoom shod
#Y=A*X + B ro bdast miare


#A ro mizare
coef_=A
intercept_=B

#shoma bkahy seda koni
model.coef_
model.intercept_


#tabey dg  predict

model.predict(new)

#new ro migire
#mizare toye A*new + B --> y predic

#estehkam = A* x + B



def fit(x,y):
    
    a=np.random.uniform(0,100)
    b=np.random.uniform(0,100)
    
    cost_list=[]
    #yek khat misaze
    for i in rnage(0,1000):
        y=a*x + b 
        #cost hesab mikone
        #cost 1 
        cost_list.append(cost)
    min(cost_list)
    #A o B
    
    coef_ = A
    intercept_ = B
    
def predict(x):
    y= coef_ * x + intercept_
    return y 



class LinearRegression():  
    def fit(x,y):
        
        a=np.random.uniform(0,100)
        b=np.random.uniform(0,100)
        
        cost_list=[]
        #yek khat misaze
        for i in rnage(0,1000):
            y=a*x + b 
            #cost hesab mikone
            #cost 1 
            cost_list.append(cost)
        min(cost_list)
        #A o B
        
        coef_ = A
        intercept_ = B
        
    def predict(x):
        y= coef_ * x + intercept_
        return y 
    
#model=LinearRegression()
#model.fit(x,y)

#model.coef_
#model.intercept_


#model.predict(new_x)


#---bjaye inke hey biad a o b ro randoim bzne
#100000 ta bayad bsaaze tool mikeshe

#az raveshi banme gradiant descent 
#gradiane kaheshi estefade mikone


#bsoroate random a o b ro misaze
#ekhtelaf (cost ro hesab mikone)
a=[1,2,3,4]
cost=[5,3,2,1] # 55noghte 3 noghte 2 noghte
plt.plot(a,cost)
plt.xlabel('A')
plt.ylabel('cost value')
plt.show()


#a=1 --> cost function ro hesba mikoen 5 % khata
#a+1 = 2 --> cost function edame mide
#agar bishtar bshje edame nmide


#bare aval random A ro gozaasht 2
#1 -->

#too dele tabeye lienarregression

#bare aval a va b besoorate random zade mishe
#badesh cost function
#a haye badi b haye badi
#gradiant descent estefade mishe

#yani dar jahati tagghir mikonan k tabeye cost functione ma gradiante , kaheshi bashe
#algorithem pichide
#rfiazi



#gridy done done avalie
#dovomie sklearn --> behine sazi 
#

#nmiad doen doen random search kone
#'hadafmand' a o b ro taghir mide
#ta kamtarin cost value ro peyda kone






#---. Linear Regression ( regrasion khati)
#---> ba estefade az hadeaghale majmooe morabaat
#----.Least squared 
# a coef
#b intercept
#cost 

#gradiant descent --> optimize a o b 

#minimum cost value
#A B chie


'''
1- ag yedoone x nabod , speed , temp ,....
2- ag khati naboood?
3- cheghad gahbele ghaboole in khat k shabihe khate avakl ( khate avale hasti) --.accuracy , trust

'''
#1----> yedone x nabod
from sklearn.linear_model import LinearRegression
model=LinearRegression()
x=np.array([[10,25],[20,27],[30,29],[40,31]]) 
y=np.array(data['estehkam'])

#vaghty 1 x dashtmim khat haye random a o b 
#y=a*x + b   ba bazi krdn ba a o b miseh hezarta khat kshid



#y=a*x1+b*x2+c ---> hezaran safe sakhrt ba bazi ba a , b ,c 
#hezarta safe bsazsi
#hey cots value hesab koni bara har

#y=a*x1+b*x2+c*x3+D*XC4+.........
#bale b sadegi
#nbedone hich taghir
#fght yadet bashe choon xet bishtar az 1 done soton dre dg niaz b reshape ndri


model.fit(x,y)  #a b ab cost functin ,... behtarino peyda mikone
#khodesh tashkhis mdie
#bejaye inke bgrde donbale a o b fght
#chon mibine 2 ta x darim -->fazaye data 3 bodie
#donabel safe migrde a , b ,c



#kafier hala predict koni

#ag soratamo bbrm bala rooye 70 va dama ro kh sard konm chi?

y_pred=model.predict(np.array([[70,5]]))
print(y_pred) #[8984.43846154]



#rasm 
#hala ghashang mishe.....[project]

#x=arange(0,100)

#---------------------------
#Agar non-linear bood chetor??????
#khati nsit
#a o b hads zadan bri peydash koni ?
#algorithem haye pichide tar 
#amari tar

#yekserei algroithem amari hast k kh pichide taran 
#algorithem oon zir dare karesho dare mikone
#to kafie az fit bdi rooye datahat
#vba estefade koni az oon algorithem haye pish sakhte


#az ravesh haye gheyre khati estefade konid
#---------------------------------------------
'''
1- ag yedoone x nabod , speed , temp ---> yek safe , ... y=a*x1 + b*x2 + c*x3 + .....
2- ag khati naboood? ---> bjaye Basic LR (linear regression) ravesh haye pichdie tari hastan 
3- cheghad gahbele ghaboole in khat k shabihe khate avakl ( khate avale hasti) --.accuracy , trust

'''

#-------Temnplate------
from sklearn.linear_model import LinearRegression
model=LinearRegression() 
x=np.array(data['speed']).reshape(-1,1)
y=np.array(data['estehkam'])
model.fit(x,y)

#y=A*x + B
#A
print('my A is : ', model.coef_)
print('my B is : ', model.intercept_)

#my A is :  [148.99]
#my B is :  -527.9999999999995

#predict
new_x=np.array([80]).reshape(-1,1)
yy=model.predict(new_x)
print('my predicted output is ', yy , 'for speed 80')
#my predicted output is  [11391.2] for speed 80

#rasm
#tarjih midm
#che baze ee az speed ro mikhay pishbini kolesh----------
new_x=np.linspace(0, 100).reshape(-1,1)
A=model.coef_
B=model.intercept_
y_pred=A*new_x + B

plt.scatter(x,y)
plt.plot(new_x,y_pred)
plt.grid()
plt.show()





#raveshe dovome-----------------------
new_x=np.arange(0,100).reshape(-1,1)
y_pred=model.predict(new_x)
plt.scatter(x,y)
plt.scatter(new_x,y_pred,s=2)
plt.grid()
plt.show()



new_x=np.arange(0,100).reshape(-1,1)
y_pred=model.predict(new_x)
plt.scatter(x,y)
plt.plot(new_x,y_pred)
plt.grid()
plt.show()


#-----------------------------
#=============================

#soale -->too clas matrah shod

'''
sarmaye gozar
Developer

sarmate gozar 4 ta data vase shoma
developer man yek khat pishbini krdm  y=A*x + B , in this case y=140*speed-600

avalish -->khode noghat rooye khat hast ya na  --> saramyer gzoar --. OK dvlpr --> :) 
dovomish---> spped darooonesh , biroone rfsange ---> test mikoni




2 ta azmayehs koni 
yeki spede 80---> esthekam = 12000 y true
speede 100 ----> estehkam ==== 130000 y true


midi b mdoel
model.predict(80)----> y adad y pred
model.predict(100) ---. y pred


y-true - y pred = 10 ta too estehkam frh


y tru - y-pred/ y-tru --> 1 % 

darsade



pas kareii motmaen tr z inke beri too azmayesh gah vojdo ndre

in kar --> naiz b hazine , sarf vaght (emkanesh nabod chi???)





hala soal --->







azooone noghate azmayehsgahi
4 tas





5,6 harchanta bood

'''


#ghabl az modeling

# datamo ---> train   , test
#varede laptob nakonm


#model.fit (train)


#rooye test 
#pishbinimo anjam bdm


a=np.array([ [10,1200],[20,2044],[30,4043],[40,5500],[50,6600],[60,7000] ])
data=pd.DataFrame(a,columns=['speed','estehkam'])
x=np.array(data['speed']).reshape(-1,1)
y=np.array(data['estehkam'])

plt.scatter(x,y)
plt.title('noghate azmayeshi')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.show()

#sarmaye gozr beman dade

#man ghabl az inke modeling konm

train=np.array([ [10,1200],[20,2044],[30,4043],[40,5500],[50,6600] ])
test=np.array([[60,7000]])

x_train=train[:,0]
y_train=train[:,1]

x_test=test[:,0]
y_test=test[:,1]



#datamo k 6 ta noghte dash --taghsim krdm b dota data --> train ,, test 
#datam x o y         train y x o y   test x o y

#data--> train + test

plt.scatter(x_train,y_train)
plt.scatter(x_test,y_test)
plt.title('noghate azmayeshi')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.show()


#modleingamo agha anjam bdm rooye 


from sklearn.linear_model import LinearRegression
model=LinearRegression()
#nbjaye kole 6 noghte , fght rooye 5 noghte ( train)

x_train=np.array(x_train).reshape(-1,1)
y_train=np.array(y_train)


model.fit(x_train,y_train)  #mese ghdim x , y 

new_x=np.arange(0,100).reshape(-1,1)
y_pred=model.predict(new_x)

plt.scatter(x_train,y_train) #noghteye abi
plt.scatter(x_test,y_test) #Noghteye test
plt.plot(new_x,y_pred)
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.show()


#---zibasazi
plt.scatter(x_train,y_train,label='training') #noghteye abi
plt.scatter(x_test,y_test,label='testing') #Noghteye test
plt.plot(new_x,y_pred)
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.legend()
plt.grid()
plt.show()


#y prediction
#y true



#y_true - y_prediction
from sklearn.metrics import mean_absolute_error


#y vaghe eeee 
#pishbini shode
#y_test=test[:,1]
#Y_TEST ---> 

y_test=test[:,1]
y_pred=model.predict(x_test.reshape(-1,1))


mean_absolute_error(y_test,y_pred)

#in tabe ye adad pas mdie too y zarf




MAE=mean_absolute_error(y_test,y_pred)

print('MAE of this model is : ', MAE)
#MAE of this model is :  1154.2000000000007

#1154 aadad ekhelad dre, khatra dare

#MAE ---> gozareshe khata
#mean absolute erooor , miangine motlaghe kjhata

#MSE
from sklearn.metrics import mean_squared_error

MSE=mean_squared_error(y_test,y_pred)
import math
RMSE=math.sqrt(mean_squared_error(y_test,y_pred))
#RMSE ---> radikal MSE


#MAPE-------------
#

#-----
#mae -->ekhtelaf
#modelet agha tooye estehkam 1000 ta pishbini frgh
#mse , rmse --.adsadsa kh rizan 0.00001 

#MAPE
#mean absolute percnetage error --.darsade khata
#Y_true -= y_pred / y_true

from sklearn.metrics import mean_absolute_percentage_error

MAPE=mean_absolute_percentage_error(y_test,y_pred)

print('darsade khataye mdoele ma hast:', MAPE)

#darsade khataye mdoele ma hast: 0.16488571428571439

'''
modelam ok shod
16%

1154.2000000000007


'''







#=========================================
#----QUIZ L14-------
#YEK DATA BSAZIM B NP.array
#YE X dahste bashe
#y y 

#tozih ham bdid dar description
'''
x--->
y-->

np 
ham pd

---> x o y

#---2  kar
'''
#-----kare aval hamoon basic LR
#model
#fit koni roo kole x o y 
#moadelle khato bedast biari too hashtag bnvgisish
#plotesho rasm koni



#----kare dovom --> ba hamoon data
#ghabelsh train , test taghsimesh kon
#modelo fit bde fght rooye train
#scoresho khatasho rooye test bhm bgooo
#MAE , MAPE


'''
kh kh kh kh mohem
fght o fght az ravesh haee k dar class gofte shode

tabe hast
tabe ee k esmesh to in jalase naumade ersla bshe 
ghanoni quiz -->estefade nakon
screening 


Q_L14_fNAME_LNAME
#in quizmohem hastttttt
****

github

'''













