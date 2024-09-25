"""

In The Name of GOD

Created on Wed Sep 25 16:06:05 2024

@author: Ali Pilehvar Meibody


LL15




"""
'''

Tamam masaele jahan ro ma tbdil mikonim input - output



entezaremon az yek ML chie



ensan --->
1-vorod mgirie (cheshmash, goosh midi , booyio , tamio , lams)
2-bar asase oon yadesh migire , manteghi kasb 
3-action , (tasmim bgiri, kari anjam) bar asas yadgiri (manteghe)



Artificial intelligent --->
1-vorodi-->data (vorodi - khoroji dahste bashe sorat , estehkam , neveshte javab , yek gol rasm kon , axe gol , ....)
2-yad bgire az data, rabetye beyne vorodi khoroji (Machine leanring ML)
3-bhsh y vorodi bdim , bar asase oon rabete h bdast ovorde--->khoroji ro mide




ghabl az inke vare shim----> BASIC linear regression
y=A*x + B (A , B)

farz-->rabete ee darim beyne vorodi va khoroji (data = sorat , estehkam)
farz -> in rabetehe khati hast


hezaran khat miskaht ( y=a*x+b  ba taghire a o b)
vase har khat miomd faseleye oon khat ro ba noghate tajrobi (azmaeshi) bedst miovord--> faseleye har nogthe ba khate be tavane 2 badesh jameshon mikrd---> cost value


a=4 b=6  costvalue1=12392
a=3 b=5   costvalue2=2222
a=2 b12  costvalue3=232
a=100 b=229  costvalue4=2123
......

az beyne hame khata k rasm mikrd , ooni k kamtarin  costvalue ro dare
a o b ro dar miavord--> migof in hamoon rabete ee hast k donabelsh bodm
oon a o b --> A va B i hats k donbaleshma

mantegh kasb krde --> khoroji = a* vorodi + b

pas bhsh ag vorodi bdi mizre in too va bht khoroji mide


BASIC
.....

CHijori test konim va bfhmim k doroz mige?
accuracy chijori mishe gof baalst???


'''





# Import ha
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

x=np.array(data['speed']).reshape(-1,1)
y=np.array(data['estehkam'])
#Linear regression --> hezarta a , b baraye ma mizne , costvalue harohesab mikone
#paeen tarineshon , minimum tarin cost value a o b ro bdast miare
#basic tarin halate regression hast
from sklearn.linear_model import LinearRegression as LR
model=LR()
#fit beshe
model.fit(x,y)

#training --> a o b haye mokhatlef ------> optimization , optimum tarin a va b ro peyda kone kamtarin cost value




#too dele model , A o B hast
a=model.coef_
b=model.intercept_
print('shibe khat hast: ',a,' va arz az mabdaye khat hast: ',b)


#y=83.7*x + 2215
#esteehkam = 83 * speed + 2215 
#yad grfte---> ML --> Machine learning

#predict------------------
#dar speed 100 estehkamemon chande
x_new=np.array(100).reshape(-1,1)
model.predict(x_new)

#yani dar speede 100 vaghty sorate datsgah ro 100 bzari , estehla mishe 10591
#fghth ydon epredict mitone anjam bde ?? naa harchgdh bkhaye
x_new=np.array([10,15,20,25,30,35,40]).reshape(-1,1)
model.predict(x_new)


#7 ta sorat too yek arrayu ddm 7 ta estehkam ham too yek array dad, mitoni ino rasm koni ya ya....
#arange, ....

x_new=np.arange(0,100).reshape(-1,1)
y_pred=model.predict(x_new)


plt.scatter(x_new,y_pred,s=2)
plt.title('pishbini')
plt.xlabel('speed')
plt.ylabel('estehlkam')
plt.grid()
plt.show()


#hamchnin yek rahe dg ham hast 
x_new=np.arange(0,100).reshape(-1,1)
#bejaye inke y_pred hey az predict estefade koni
#predict az chi dare estefade mikone? A , B x--> a*x+b --> tahvcil mide
A=model.coef_
B=model.intercept_
y_pred= A*x_new + B
plt.scatter(x_new,y_pred,s=2)
plt.title('pishbini')
plt.xlabel('speed')
plt.ylabel('estehlkam')
plt.grid()
plt.show()


#goftam hala dar nahyat biaym bbinim kenare ham dg ham dade haye azmayeshgahi ro ham dade ye regression ro 
A=model.coef_
B=model.intercept_
y_pred= A*x_new + B
plt.scatter(np.array(data['speed']) ,np.array(data['estehkam']),label='real data')
plt.scatter(x_new,y_pred,s=2,label='predicted values')
plt.title('DATA')
plt.xlabel('speed')
plt.ylabel('estehlkam')
plt.legend()
plt.grid()
plt.show()

#accuracy ro az koja bfhmim? #chghd trustable ghabekle etemad hast ?
#bayad brim azmayesh bokonim ---> zamnan bar , momken nis va va va
#ghabl azainke model konim ysri data ro bzarim kenar aslan varede bazi nakonimesh 
#datamoon--> avale kar---> train dataset hastan test dataset hastan
#biaym model. fit( fght rooye train ha.
#badan k ok shod, brim x e test haro bgirim bdim b modle model.predict() bzne --> y_pred
#y_test o ba y_pred moghayese konim ---> (MAE ekhtelafeshon , ya MAPE % ekhtelaf)
#report va gozaresh chi bgim ----> modele ma felan darsad khata darad)

#nokte ye test train split ---> chnataro bzar kenar, fk kon ina oonae bode k ghrar bode
#bad az model sazi bri too azmayeshgah bgirishon ta bbini modelet valid hast ya na 
#hamoon avale kar bzareshon kenar ....................

#soal
#chantaro bzairm kenar?
#kojaro
#beham chjasbide bashan?

#--------------javab----------
#trade off 
#train dataset , point hardcxhi bishtar , noghat bsihtar e, mdoele ma behtar mitone bfhme rabete aslie chie bode
#harchi test dataset bishtar bashe , accuracy k elam mikonim daghigh tare


#train kh ziad bashe , etst kam bashe -->modelemon khob yad migire sama motmane nisim
#ag test ziad bashe kh ziad -->model deghate dgahigh migim ama deghat 18% , train dataset kame vba model nmitone kyaeesh bgire
#noghte behine oon vasate sweat point --->nesbat b data hast --> 25% dataset --> test dataset 20,30

#soale 12
#soale 2-->

#BIAS ----> 




#inke aval joda koni
#25% data bbinim chanta mishe
#random vardari va va a... chghd skahte
#2,3 khat
#sklearn ???? --> tabe dare

#-------framwork ---> ML dareid yad migirid
#---> Linear Rgeression ML model ----------
data=pd.DataFrame([[10,3000],[20,4322],[30,4334],[40,5722],
                [50,6200],[60,6999],[70,8300],[80,9000]],columns=['speed','estehkam'])
#data=pd.read_excel()  #mirizi too data
#data=pd.read_json() az roo site
#data=pd.read_csv()


#dar harsoorat dade hat toye yek variable hast bname data k sotoon dare har soton yeseriash vroodi khoroji


#step0------->
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

#Step1======================================================
#data--> x o y tabdil koni
#nokat--->
#hatman x o y et numpy array bashe -->choon sorate array az tamame mavarede digar bishtare

#agar x et 1 soton bod fght --> az reshape(-1,1) estefade kon  . ag yek soton abshe --> np.array 1d , ba reshape 2d 1 sotoon chanta radif
x=np.array(data['speed']).reshape(-1,1) 
y=np.array(data['estehkam'])

#step2==========================================
#ma baya dmodelemon ro sehat sanji konim , brim too azmayesh dobarew azmayeh
#ye rahe hale talaee-->ghabl az train 
#boro va yek tedad az datato aslan joda kon bzar knar bgo ina fk koni nadarish
#*******8

#ALL DATA ---->  TRAIN DATASET | TEST DATASTES

#data-->x , y

#x , y --------> xtrain y train | xtest y test
#*******8

from sklearn.model_selection import train_test_split
x_train, x_test , y_train , y_test = train_test_split(x,y,test_size=0.25,shuffle=True,random_state=42) 
#x va y ro tabdil mikone x train y train | x test y test 
#4 ta zrf dri

#@arg --> test size az 0 ta 1 ----> 20 nanevsi 20  0.20   #random anjam nmide mire az tah var midre
#tekoon dadane livane havie tas

"""
tozihe train_test_split dar sklearn

def train_test_split(x,y):
    len_x=len(x)
    len_y=len(y)
    x_test=random.choice(x,2)
    x_train=x- x_test
    #y......
    return x_test, x_train, y_test, y_train


train_split_split(x,y)
a=tabe()
a,b,c,d=tabe()
"""
#rasmesh
plt.scatter(x_test,y_test,label='test dataset')
plt.scatter(x_train,y_train,label='train dataset')
plt.title('DATA')
plt.xlabel('speed')
plt.ylabel('estehlkam')
plt.legend()
plt.grid()
plt.show()

#dataye aslie man ine
plt.scatter(x_train,y_train)
plt.title('DATA')
plt.xlabel('speed')
plt.ylabel('estehlkam')
plt.grid()
plt.show()


#step3======tarife model
from sklearn.linear_model import LinearRegression
model=LinearRegression() #aval mdoeleto tarif mikoni
#model=KNN
#model=DT
#modle=ANN




#step4----------fit , training------ rabete ro ya dbgire

model.fit(x_train,y_train)
#bejaye inke rooye kole data yad bgire , fght trianingh

#alan yek mdoel daram k yad grftee....
#chia too deleshe ? predict() mitone pishbini mikone 
#A
#B
#Moadele hast 
a=model.coef_
b=model.intercept_
print('shibe khate man hast : ', a , 'va arz az mabda hast' ,b)
#shibe khate man hast :  [88.186] va arz az mabda hast 1977.3200000000006

#rabetey aslie man hast 
#Y= 88 * x + 1977

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

#step5=======model validation====================
#---------------------
#modele shoma rooye training dataset train dide 
#aya rooye khode hamin noghat fit hast????

#training score ---> fitting ability -->tavanaee modelsazimon, tavanaee fiit shodanehso nshon mide
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_absolute_percentage_error as mape

#x_train , y_train in noghate abi -->vagheiate true data, azmayeshgah omdn
#x_train haro ag bdm b model chi barash pishbini mikone rooye khat 
y_train_pred=model.predict(x_train.reshape(-1,1))

#ekhtelafe beyen pishbini shod ebba vagheaiato mdie bar asase formu
#mae-->ekhtealfe motlagh
#mape 
training_score1=mae(y_train,y_train_pred)
print('MAE train score model hast: ', training_score1)
#MAE model hast:  169.2400000000001
#model man khode dade haee k bhsh dadim ro ba ekjhtelafe 169 holohosh dar epishbini mikone
#ham enoghata k rooye in khate nisan


training_score2=mape(y_train,y_train_pred)
print('MAPE train score model hast: ',training_score2)
#MAPE model hast:  0.033878970810629905


#in 3% ya 169 ekhtelaf , score khataye
#yekodom darsadi yekodom 

#In nshon mide fitting ma 3% khata dare (train_score)
#yadgiri ch shekli bode



#2------->
#bayad bbini modeletrt, dataye jadid ro chijoori pishbini mikone
#bayad bri too azmayeshgah
#x_test
#y_test
#baayd mriftm azmayeshgah ama gozshtmsh kenare


#x_test, y_test -->datahaee hastan unseeen and new 
#nadide mod0el jadide bartaye model 
#Pishnbinie modelo mahak bznim

#ekhtealfe beyne vaghe ei va pishbini

y_test_pred=model.predict(x_test.reshape(-1,1))

test_score1=mae(y_test,y_test_pred)
print('MAE test score ma hast :' , test_score1 )
#MAE test score ma hast : 425.22

test_score2=mape(y_test,y_test_pred)
print('MAPE test score ma hast :' , test_score2 )
#MAPE test score ma hast : 0.08646094679090467

x_new=np.arange(0,100).reshape(-1,1)
y_pred=a*x_new+b
plt.scatter(x_train,y_train,label='training data')
plt.scatter(x_test,y_test,label='test data')
plt.plot(x_new,y_pred,label='predicted line')
plt.title('Data')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.legend()
plt.show()

#train score---> mape(y_train, y_train_pred) --> 3 % --> faslee noghate abi ba khat --> fit ability , modleing , yadgirimon chghd khob
#test score---> mape(y_test, y_test_pred)-->8% #noghate narenji -->y test , y_test_pred in kahte faselasho -->pishbinie dade haye jadid ro

#report
'''
modeli k sakhtam migoyad rabeteye beyne estehkam va sorat hast
Estehkam = 88 * speed + 1977


va deghate modeling

train_score = 3 %
test_score = 8 %

yani fasdeleye khate pishbini shod eba noghati k dar training estefade shode ast 3% ekhtelaf dsran ke neshan midahan 
process yadgirie rabete az rooye dataha kh khoob bode


deghate model dar pishbinie dade haye jadid (test) 8 % kharta dahste k nesbataan khooob ast



train_score -->model fitting (learning)
test_score  --> prediction
ba mdoelet bazi mkrdn



***
ag train score paeen bashe test score paeene -->undefitting yani ya dngrfte

train score bala bashe kefayat mikone? hata oon noise va khatey dat aham yad grfte --> general bashe , dade haye jadid ro khoob pihs bini
overfitting  (generalization ro az sdast mide)
'''

'''
-----AI---------
30% nasle yek + optimziation + namadgara = fuzzy 
70% ------> ML machien learning



#***kole masaele jahan----> voroodi -- khoroji   input() output()

----MACHINE LEANRING-------- (bar asase soale mnaale he b 3 ghesmat tbdil msihe)
supervised ML
unsupervised ML
reinforcement


supervised------> barasase output ---> do ghesmate
khorojiiiii

peyvaste ---> continious --> vazn , jerm ashari 1.3237 1.322 1123627 2173298
gosaste --> chanta chanta -->afrade tooye class 2.5 XXX 2.5 
#kole khoroji ha mitone peyvaste bashe ya gosaste

vorooodi ---->rabete --->khrooji
too in bedast abvardan khrooji
ag khorojie peyvaste bashe (217.23 1232.32322 dama, estehkam , quality parameter)---> Supervised Regression
ag khorojimon gosaste bashe (cdhanta chanta , khoobe ya badeee 0 1 ,gorbe sag , print , khoob bad , awli khoob bad ---> daste bandi 
Supervised Classification





'''

#---------------
#kole masale ejahan input()  output()
#ml mikhad biad rabete ro befahme
'''
banabar outptu va khrojimon
agg peyvaste bashe regression ag gosaste bashe classification


-------Supervised regression | supervised Clasdsfification ------------ (bar asase khoroji
1-data darim (havei sotrone input, sye sootn output) ---> clean , x  o y tabdil , test train tabdil mikoni
2-model (train , fit---> rabete he ro ya dbgire) , basic regression raveshe hadeghal morabat a , b ,... rabete he ro dr
model hjaye dg ham darim -->az ravehs haye khase khdoeshon hamashon baham donable rabteeye x va y hastan
1-lienar regression | logistic regression
2-K nearest neighbour (KNN)
3-decision tree (DT)
4-Random Forest (RF)
5-Support vector machine (SVM)
6- Artificial neural network ( ANN) Multi layer perceptron (MLP)


#-----model . predict, a b , .......
#3----> validation
#train score, test score 

#.......predict anjam bdi va reporteto hazer koni





#****yani ch regreession , clasificton 6 ta model


'''

'''
Mesale classification

'''

#0-cleaning
#1-data --> x , y 
#2-> test train split
#3-modeleto tarif mikone
#4-trianing (fit)
#5-validation  predict() mae mape

#----modelemon toyue ghesmate 3 fgrh mikone


#gol shenas 
#yek gol 2 ta feature (moshakahse) 
#toole gole
#ARZE GOL

# do no gol
#narges
#roz

#yk frd mifhme ye gol nargese
#yek gol roze

#tool o arzesh kh ziad bashe ->narges
#ag kh koochik bashe roze gole

#vorodiiii- (andze bargo ina) ----> maghz -----> nargese ya roze

#ML ---> in rabete ro mifhmid chgdh awliiiiii



#-------------
#-----20 ta gol negah mikonm va baraye harkodomesh mirm 
#arzo tolesho hesab mikonm va mibinm jozve kodom golas

'''
 
nemoone     tool        arz      type
1             2.4    1.5          roz
2             3.5     5.3         narges
3
.....
20



roz 0 narges 1
#----------------shabieh machine
nemoone     tool        arz      type
1             2.4    1.5          0
2             3.5     5.3         1
3
.....
20

'''
import pandas as pd
data=pd.DataFrame([[2.4,1.5,0],[2.6,1.7,0],[5.2,3.2,1],[5,3,1],[2.1,1.2,0],[2,1,0],[5.9,3.9,1],[2.12,1.43,0],[6,3.2,1],[6,3.1,1],[2.11,1.87,0]],
                  columns=['tool','arz','noe_gol'])
#rabete toolo arz ha ba noe gol hastam
import matplotlib.pyplot as plt

plt.scatter(data['tool'],data['arz'],c=data['noe_gol'] , cmap='viridis')
plt.title('gol ha')
plt.xlabel('tool')
plt.ylabel('arz')
plt.show()
# ha rnoghte yek goil hast
#11 ta gol  drm
#har gol ye otool dar eyek arz

#man ag brm yek gole jadid bgirm
#arz=3 , tool 4

#model---> rabetey beyne msohakahset gol va noe gol
#b besmela--> masale--> input() output()
#Machine learning Supervised Classification anjam midam
#model ---> 6 no model LR,KNN, DT ,RF , SVR, ANN

#LR -->regression
#LR (logistic regression) ---> classification


#Linearregssion , #logiosticregession

#---.frghesh ine
#bejay einke rooye khat biad fit kone
#Miad mige in khate balash y dastan paeenesh y dasteye dg hastan



#step0-----------
#cleaning

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


#3------model selection
from sklearn.linear_model import LogisticRegression
#bejaye Linearregrssion -->in baraye dade haye peyvaste hast
model=LogisticRegression()

#4---training . fit
#training


model.fit(x_train,y_train)




#5---validation
#1----train score
#2----test score

y_train_pred=model.predict(x_train)
#faseleye beyne vageh ee haro ba pishbini ro dar biaram
#mAPE MAE
#MAPE , MAE baraye regression hastan na classification
#clasification bayad bge k masalan azin 8 ta noghte k trian shdon ro
#chanta sahih mige chanta ghalat pishbn
#8 ta 7 ta golo doros gof --> 1 done ghalat

from sklearn.metrics import confusion_matrix
score=confusion_matrix(y_train,y_train_pred)
score

#faseleye beyen vahghhe e ha y-train ba y_train_pred ro bma bde

'''
narges  1 postie +
roz  0 mnegetive _


#_-----
#doros pish bini krde
momkene gole narges1 bashe model ma ham bge narges1    TP
momkene gole ma roz 0 bashe model mahma bge roze   TN


#ghalat pishbini kona?
momkene gole narges bashe1 bge gole roze  FN
momkene gole roz bashe 1 bge gole nargese FP



8 DATA nargesan ya rozan


'''

from sklearn.metrics import accuracy_score
score=accuracy_score(y_train,y_train_pred)
score  #8 ta az 8 ta ro dorosd pish bini krder  100/100

#0.5 ---> 4 tasho doros pish bini karde 4 ta sho ghlt

'''
ACCURACY:"
TP + TN / TP + TN + FN+ FP 
tedade doros ta bar hame ye halate momkene----> 4 az 8 ta data ---> 0.5 accuracy

gahan barasmon moheme ke hata chanta 
ghalat 
4 ta ghalate
kodoma roz bodan narges pishbini krde  zz1
kodoam narges bodan roz pishbini krde  zz2

zz1 + zz2 ---> 0.5 doros bode 0.5 4 ta zz1 , zz2



#---->pishbiie saratan 
TRuueeee---------
khosh khim bashe mdoelgofte khosh khim  TN
Bad khim ag doreo sbge badkhim TP

Eshtebah modelmon
ag khosh khim bashe ama modele ehstebah bge bakdhime   FP
ag bad khim bashe amdoele ehsetbh ge khosh khime  FN



accuracy --> tedade tru ha / kol 
#rajebe ghalat
chizi nmige




modele man biad bge 100 ta bimar drim

accuracy 96--> fght 4 taroghalat gfote



4 ta ro ch ghalakti 

-----------
                  predicted negetive     predicted positive
Negetive class
positive class



           precdcited 0     predicted 1
class 0
class 1

vonfusion matrix





TP  TN  -->doros pishbini shodan 

FP FN  =---> ghalat



accuracy---> TP + TN / all 
bishtar sare dar bairi -->confusion matrix bgiri
'''

from sklearn.metrics import confusion_matrix

score=confusion_matrix(y_train,y_train_pred)
score

'''
array([[4, 0],
       [0, 4]])

'''
#train score bod  az 8 ta noghtamo 8 tash doros bodeeee confusion bbini

from sklearn.metrics import accuracy_score
y_test_pred=model.predict(x_test)

sc=accuracy_score(y_test,y_test_pred)
sc

#oonam doros pishbini krde baram
cm=confusion_matrix(y_test,y_test_pred)
cm
#az oon 3 ta gol k tgest vrdashtim
#dota roz bode
#1 kish narges

#oon 2 ta roz ro model 2 ta roz doros pishbini rde
#oon ydone roz ham, roz pishbini krde

#kh awlii
#trian score 100%\
#test score 100%
#awli shod




#deploy------ az predicdt estefad ekone


#bri toolo arze jadid bgiri bdi bhsh

#gole jadid daram
gol_jadid=np.array([[6.2,4]])
model.predict(gol_jadid)
#array([1])

#classfiication ham train bdim


#$================
'''
QUIZZZ
'''

#jalaseye yekshanbe
#quizzziii


#yek data tolid konid dota soton vorodi yek soton khorojhi 
#yekabr sotone khorojiton peyvaste bashe---> Linearregresion va in workflow 6 step done done najam bshe


#yekabr ham sotone khorojiton gosaste bashe 0 1 , 0 1 2 ashe --> clasification --> wqorkflow logistic regression 



#shoma say konid
#title
#Q_L15
#baraye bande ersal namaeeee





























