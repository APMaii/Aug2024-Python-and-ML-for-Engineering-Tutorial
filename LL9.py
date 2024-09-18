#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN THE NAME OF  GOD
Created on Sun Sep  1 17:57:58 2024

@author: Ali Pilehvar Meibody

L9
"""

#--------
#built in function
#keywords
#variables (number, str, list,......)
#function (def)--> return, vorodoi, khoroji, seda, arg (default =, * /)

#ma miaym va funciton hamono mitonim estefade konim
test_in_class(10,20)


#NameError: name 'test_in_class' is not defined


#tabe ro biaram ---> import konam
#import function -->tabe bairam

#import madule -->az dele madule.fucntion 




#tabe ee k mikham estfedad ekonm kojas? too kodom

#madule--> test_12  apm_23  apm217682 aliali

#desktop, user, application, folder C , folder D
#scipt hat koja save msihe default--> mire onja migrde

import test_12
#boro too file ha --> samte rast
#/Users/apm/Desktop
#hich errori

#test_12 is not defined
#No madule nameds test_12 
#agar samte rast havaset nabashe --> nadoone koja bgrde

#in madule ro hala mishanse , script


#function azash ro az dele in biron bekesh

#test_12 dot --> boro too dele test_12 ...
result=test_12.test_dar_class(10,20)

#inkaro shoma baray madule haee k dari ya sakhti miri anjam mdii



#hala ma kolan mikhaym ---------
#NOMR, STANDARD , PRINCIPLE--------
#KETABKHOONE HAYE MAROOOF, tabe haro miekshi


#numpy-->koli tabe-->mohasebate
#pandas-->koli tabe-->kar ba dade o data, cleaning,....
#matplotlib -->rasme


#aval ianro bayad import konim
import numpy
import pandas
import xfelan


#pas tebghe chizi k goftm 
#------yekabar -->sakh ttrin-->standard



#cpu, gpu -->ka rmikone , 0,1
#---windows------->panjere rooshe k beyen to o in mashin khosheglesh krde
#command line --->> terminal 


#================
#halate dastori va codie windows--> terminal
'''
windows: keyworde win+R  
wt ro minevisan
ye safe siah



mac: command+space
terminal minevusiam
ye safe siah



safe siah-->terminal


'''
#================


'''
roye base baz mishe

boro felan ja

cd desktop
cd user



ls
list behet mide


cd .. barmiagrde aghab

cd ~ home directory


.....


tamame ina too base -->too kole cpuye man dare anjam mishe



(base) apm@APMs-MacBook-Pro ~ % python --version
Python 3.11.5

yani na tanha pythond ari -->version 3.11.5

yek code ejra konam

python --version ---> mige k pythond ari ya nadare versionesh
python esme_file.py   -->oon fiel ro ejra mikone


base--> az kole cpu ham estefad ekrdm pythono--> run krdm yek barname




#============
python 3.11


farda rooz python 3.14 --> 
download pythone jadid


ANACONDA--->YEK BARNAME SAKHT
GOF BEJAYE INKE AZ BASE ESTEFADE KONI
MAN ABARAT 100000 TA ENVIRONEMNT MISAZAM
1000 ENV , COMPUTER DAI
AHRKODOOM PYTHON DARE


env --> class2023 -->python 3.11

class2025 -->python 3.16


chnata environemnt


env ---> python (har version) --> harchi ketabkhone ham khstti barash briz


#niaz b yek dastoor --> pip install package_name
masalan pip install numpy



aga rnumpy ro bekhay roo kole system brizi -->terminal --> pip install numpy


ama gar mikhay fght rooey yek environmentet berizi (kare doroste)

bayad avalbri anaconda bri too environmentet -->onja pip install --->powershell (rahe aval)
rahe dovom--->vali abz nakoni



env_name --> esme oon mohitet -->too in mesal class2024


#===========
conda info --envs 
chanta mohti dario chian kojan



conda activate class2024
pip install numpy 


motmaen bsihi :
    conda list
    
conda deactive




hala mikhay ba envrionementet yek code ro ejra koni





'''

import numpy
#yani biay in ketabkhoen ro ba koli fucntion bairy intooooo
#va az delesh ba (.) tabe bekeshi birooon


import numpy

#-----------
'''
**start --> spyder -->*** spyder(esme class)
spyder()-->kol vasl msihe 


#*****
anaconda-->bejaye base --> environemnt 
powershell --> pip install ...
numpy,pandas, matplotlib, scikitlearn


badan class tmaom shod
github, pip, .... google , chatgpt , -->search bzni
pip install felanesho epyda


beri anaconda-->environment -->poweshell -->pip install ...

'''
#-----------
#-----------
#numbers (int, float, complex)
#str
#boolean True False


#--.ag bkhaym chanta ro negah dairm chi??--> list
#1-assign---------------------
a=[1,2,3,4]
a=list((1,2,3,4)) #dota arantex
#2-access-----------------
#index az 0 
a[1] #2
a[3]
a=[10,20,30,40]
a[2] #Out[18]: 30
#sclicin
#indexe 1, 2 ...
a[1:3]  #Out[19]: [20, 30]
a[:2] #az 0
a[1:] #ta tah

#ba acces chiakr konm?--> change, varreisi(iteration)
#3------------------
a[2] #30
a[2]=56

print(a) #[10, 20, 56, 40]

#4-------
for i in range(0,len(a)):
    if a[i]==20:
        print('no')


#5-----function
#append

#str function upper, lower -->khoroji midad , 
#list function apply--> a -->a taghir mikr
a.append(60)
print(a) #[10, 20, 56, 40, 60]



#==============================
#-------------#--
#2 ta msohkel
#1-->sarii nist, kheyli konde -->too mophasebate bozorg azash estefade konim
#yek bodie 
a=[32,23,143,231,123,341,32]
#2-->radifo sotoon andare
#hRFE RADIF SOTOON --> dobodi bashe
#do bod -->ye bod --> radif , ye bod-->soton
#matrix, jadval

#2 dalil , nmishe az list estefade krd
#chize jadid--> araye --> array

#yek ketabkhone e bename numpy
#mige man too delam ye class daram
#array
#to mitoni azash estefadee koni
#frghesh
#1--->sari tare , 50 barabar . mobtani bar Cpack
#2---->mitoni chan bdoi besazi, 1 bdoi , radifo sotoon , 3D , 4D , 5D ,....



#mananad list assign, access, change, iteration, function


import numpy

#mige man mitonm b numpy vasl
#mitoni ba seda zadan numpy ba dot beri va function bekeshi


#yek arwy e besazam
a1=list((1,2,3,4))
a1=[1,2,3,4]
#joftesh


#hala areraye

a2=numpy.array((1,2,3,4))
#yek array sakhti

a2=numpy.array((10,20,30,40))


type(a2) #Out[33]: numpy.ndarray


a2=numpy.array((10,'hamid',30,True))
type(a2) #Out[35]: numpy.ndarray

#-----BOD--------- DIMENTION D-------
#----0D----- fght ye adad noghte
a=numpy.array(12)
a.ndim #Out[49]: 0
a.size #Out[55]: 1 yani ydone toosh
a.shape #Out[61]: ()


#----1D----> liste ye bodi ye  khate

b=list((10,20,30))
b=[10,20,30]
a=numpy.array(b)

a=numpy.array((10,20,30,40,50,60,70))

a=numpy.array([10,20,30,40,50,60,70]) #standard

a.ndim #1
a.size #7  yek liste (1d) -->7 ta adad toooshe

a.shape #a.shapeOut[63]: (7,)  #1 bdoe, 7 ta adad tooshe
#----2D------> YEK SAFE , do ta bod
#COLUMN --> SOTOOON
#ROW ---> RADIF

# yek bdoe radif ha , yek bode sotoon ha
a=numpy.array([ [10,20,30] ,[50,60,70] ,[87,92,100]   ])
#aval radifeto benevis
#bad radife badit
#bad radife badit

#vaghty misazi
#rooye esme arrayet dot yeseri property
#array a --> number of dimention -->chan bdoi
a.ndim #Out[53]: 2



b=numpy.array([ [10,20,30] ,[50,60,70] ])
b.ndim #Out[58]: 2
b.size # 6

b.shape #Out[65]: (2, 3)  2 bode, tedade radif, tedade soootn
#*********
#RADIF, SOTOOOON
#2 ta radif, 3 ta soooton
#2 bodie


#a.shape ---> (radif,sotooon)



#------------------------------
#----1D ,  2D ----------

#2-access
#dar lsit ha
a=list((10,20,30))

a[1] #Out[66]: 20
#ye berakte ,indexesh (index az 0 shoro mishe)

#slicing 0 ,1
a[0:2] #Out[77]: [10, 20]



#_---arrray
a=numpy.array([10,20,30])
a.ndim #1 bod
a.shape #Out[73]: (3,) 

a[1] #Out[73]: (3,)
a[0:2] #Out[79]: array([10, 20])
a[:2]
a[1:]

a[1:3:2] #az 1, 2  2 ta 2 ta 
#a[start:end:chantachanta]
#a[start:end]  yedone yedone
#**end shamel nmsihe

#1D daghigahn accesesh mese yel liste 

#2D-----. RADIF , SOOTOOON

a=numpy.array([  [10,20,30,40],[50,60,70,80]        ])
a.ndim
a.shape #Out[84]: (2, 4)

#aya mikahy b radif access 
#aya mikhay b column (sotoon)
#ya mikhay b ye adade khasi dastresiii
#--------------------------
#esme_zarf[kodom radif, kodom sotoon]
#--------------------------

#b 60 dastresi peyda konam

a[1,1]  #dar a , radife indexe 1 , sotone indexe 1 #Out[87]: 60

#40 
#radife 0 , sotone 3
a[0,3] #Out[88]: 40

#sotone sevom hamasho bede
#zarf[hamaeye radifa, sotone3]

a[:,3]


#radife 1 , hameye column sotona

a[1,:] #Out[90]: array([50, 60, 70, 80])

#comma radifo sotono avaz mikone
#: hamee

#hala agha man mikham bgam 
#
#slicing
#begam radife 0 , fght sotone1,2
a[0,1] #20
a[0,2] #30

a[0,1:3] #Out[92]: array([20, 30])


#NUMPY GAME ----> BAYAD KHDOETON ANJAM BEDAHID HATMAN
#VA BA LIST HEY MOGAHYESE KONID



#4----Iteration
#1----1 bodi
a=list((10,20,30,40))

for i in a:
    print(i)


a=numpy.array([10,20,30,40])

for i in a:
    print(i)



#2 bodi
a=numpy.array([ [12,32,65],[23,45,67]      ])


for i in a:
    print(i)

#[12 32 65]
#[23 45 67]


#mese list ye laye a[2]  a[4]
#dolay ejolot -->aval mire too radif, bad soton

for i in a:
    for j in i:
        print(j)

'''
12
32
65
23
45
67

'''

#aval baayd bri too radifa, bad sotooona
#access [radif,sotoon]
#iteration for for fore avali roo radifa, for e dovomi too sotona

#0d  10
#1d  [10,20,304]
#2d  radifo sotoon -->table
#3d --->
import numpy as np
a=np.array(10)
b=np.array([ 10,20,30,40])
c=np.array([ [10,20,30],[40,50,60]    ])
#kodom radif, kodom soton
c[1,0] #Out[108]: 40


d=np.array([[ [10,20,30],[40,50,60]   ],[ [70,80,90],[100,110,120]   ]])
d.ndim #Out[107]: 3
#[kodom table,kodom radif, kdoom sotoon]
d[0,1,0] #Out[109]: 40


#4d
#5d
#6d
#nazarie 11 bodi --> nazarie -->sakht atrin



#=========5-METHOD=================

import numpy

a=numpy.array([10,20,30])



#import ketabkhane as mokhafaf
import numpy as aliali
import numpy as harchi


#standard baraye harketabkhone
import numpy as np
#mige agha harja np didi manzor hamon numnpy\
#bejaye
a=numpy.array([10,20,30])
   

a=np.array([10,20,30])



b=np.array([['3x+4*x**2'],['4x+8x**2']])

b=np.array([[4,5,6],[10,2,0]])

#x=np.array[]


# Y= A*X +B 
#A yeseri zarib, b zaribe
#a -->numpy array, b -->numpy array

#===========5-method================
a=np.array([10,20,30])
#az 1 ta 100 barma besaze

a=np.arange(0,101)
#sakht 

#ye bodi misaze
b=np.arange(2,10)

# zarf=np.arange(start,end-1)


c=np.arange(0,101,2)

#yek bode
#fght too ye bod mide


#2 bod?
#aval ye bodibesazi bad 2 bodish koni

#az 0 ta 50 -->too radife aval
#radife dovom 51 -100
d=np.arange(0,100)
# 2 ta radif , 50 sotoon
e=d.reshape(2,50)


#reshape #roye oonz arf dot bezane
#a.reshape(2,10)


a=np.arange(0,20)
#yechize 5 radifo 4 sotoni
b=a.reshape(5,4)


#adad ro bejay etartibe
#random---------
#np.
a=np.random.randint(0,100,(10,))
#tadris msihavad






#-------------asssign
#mikham besazam
a=np.arange(0,100)

#ye chizi besazam hame sefr bashe
#shape --> (radif,soton) *ba pantez
#agha man 2 eradifo 3 soton
a=np.zeros((2,3))

#tabe az moteshakel az 1 ha mikhay>
a=np.ones((2,3))

#ye adad khodam bdm

a=np.full( (2,3),  7  )


a=np.empty((2,3))

#==============
#----1D------
#8 ta 0 besazi -->zero
a=np.zeros((10))
a=np.zeros((2,3))




#==================
#================
#assign ro yad grftim ani yek aray skahtim
#mitoni az amalgarhaye riaizi estefadde koni


a=np.array([10,20,30])
b=np.array([40,50,60])
new=a+2


new=a*2

#har elementi k tooey array + - *

c=a+b
new=a+b
new=a-b
new=a*b
new=a/b
new=a**b



#karaye riazi anjam bdi


#ya baiy az tabe haee eestefade kone 
#+ cj menah
#tabe ham darim
a=np.array([10,20,30])
b=np.array([40,50,60])


new=a+b
new=np.add(a,b)

new_arr=np.subtract(a,b) # a-b
new_arr=np.multiply(a,b) #a*b
new_arr=np.divide(a,b) #a/b
new_arr=np.power(a,b) #a**b
new_arr=np.absolute(a) #|a|

neww=np.absolute(new_arr)


#zarbe dakheli 
np.dot(a,b)
#zarbe dakhelie matrixs
#*** in zareb dkahele ba element element zzrb bshe ftrghd are
#==================
#new=np.absolute(np.subtract(a,b))

#========================
#TRAMAME TABE HAE K KHEDMATETON GOFTE SHOD

#-----QUIZ --->NUMPY#
#assign
#access dadn
#ham b ye bod ham b do bod
#ndim
#size
#shape

#va tabe ha
#arange, zxeros, one , ......
#dar yek file benam numpy_practic ekajhskdhzh
##ersal konid


#nokte: tamame mabahese numpy baraye yekabram shode
#bayad code bznid


#Q_L9_FNAME_LNAME
#AI.2024.PILEHVAR@GMAIL.COM

#ERSAL NAMAEEDD

#4SHANBE----------
#MATPLOTLIB



pip install matplotlib
pip install matplotlib.pyplot

#dakhele environentetoon
#ravshe1-->anaconda-->enveiremnet-->powrshel . type enter
#raveshe 2--> terminal-->conda activate env --> type enter


















