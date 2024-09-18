#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In The Name of GOD

Created on Wed Sep  4 18:01:53 2024

@author: AliPilehvar Meibody


L10

course:
    section1[python]
    section2[lib, numpy,matplotlib,pandas]
    section3[AI]
    ....[deep learning]


"""
'''
    
    
YEK JALASE 1 SAAT (MABAHES , CLASS, KEYWORDS...)

Notes on Section1 [python]:
    
'''

#------ VORODII -->BOX --->KHOROJI
#vorodi haro bayad esm bsazi yani zarf k vaghty call
#bezaretsh dakheel zarf va azash estefade kon
#dota adad bgrie jam kone pa sbde

def esme_tabe(a,b):
    
def esme_tabe(num1,num1):
    c=num1+num2
    return c


esme_tabe(2,3) #In2  va 3 ro koja brize?

#in vorodi ha mitone yek adad bashe, str bashe , bool

def esme_tabe(a):
    print(a)
    
#hcih frghi ndre aval zarf bzari zarfo brizi too tabe
#ya inke msotagim hamono vagty call mikoni bzari
c=2
esme_tabe(c) #hrchizi bzari
esme_tabe(2)
a=2
esme_tabe(a)
esme_tabe(2)


#harchizi varede tabe koni
esme_tabe(1) #adad

esme_tabe(1.45) #adad


esme_tabe('salam') #adad

esme_tabe(True)

#list?

a=[1,2,3,4]
esme_tabe(a)
#edame mide


esme_tabe([1,2,3,4])


#numpy
import numpy as np
a=np.array([1,2,3,4])
esme_tabe(a)


#shoma vaghty chanta vorodi mikhayd begiri
#1--rahehs ine bgid agah list bde

#harja adade bzoorgtar 10 did beshmore

def dah_shomar(a):
    count=0
    for i in a:
        if i>10:
            count=count+1
            
    #print(count) #fght yani ahrj asedash konm 
    return count #Harja sedash krdm mitonm y zarf bzarmo brizm toosh



listtt=[20,34,33,2,3,1,5,7,30]
tedad=dah_shomar(listtt)
tedad=dah_shomar( [20,34,33,2,3,1,5,7,30] )

print(tedad)



#2---rahe dovom
#agha bde harchi mikhay
#bia bhm parameter bde

def dah_shoamr(a,b,c,d,e):
    count=0
    f=[a,b,c,d,e]
    for i in f:
        if i>10:
            count=count+1
    return count


dah_shoamr(20,34,33,2,3)

dah_shoamr(10,20)
dah_shoamr(20,22,1,2,2,3,4,5,5,3,2,23)
#fgth panja


#moshekl--> masalan 5 ta , 6 ta , 7 ta
#agar bkham agha bi nahayar




#agha harchi mikhay vroodii bde

def dah_shomar(*a):
    print(a[0])
    
    
dah_shomar(10,20,30,40,50,60,70,80,90,100)
dah_shomar(10,20,30,40,50,60,70,80,90,100,23,43 ,4324,42)


#-------default

def dah_shomar(a,b,c):
    return a+b-c

dah_shomar(10,10,10)

dah_shomar(10,10)



def dah_shoma(a,b,c=20):
    return a+b-c

#a ro ag nadi mitoni khdoesh default 20 mizare

dah_shomar


#-------
#2 ta maodele -->gas , liquid
#pressure #temperature
#hajmesho hesab kone
#baraye maye ha --> hajm= pressure * temp * 1.34
#baraye gas ---> hajm=pressure* 1000* n * temp 
# vorodii   pressure, temp, liquid_gas , n

def hajme_taadoli(liquid_or_gas,temp,pressure,n):
    
    if liquid_or_gas=='liquid':
        hajm= pressure * temp * 1.34
        
    if liquid_or_gas=='gas':
        hajm=pressure* 1000* n * temp
        
    return hajm

hajme_taadoli('liquid',200,2)
#TypeError: hajme_taadoli() missing 1 required positional argument: 'n'

def hajme_taadoli(liquid_or_gas,temp,pressure,n=200):
    
    if liquid_or_gas=='liquid':
        hajm= pressure * temp * 1.34
        
    if liquid_or_gas=='gas':
        hajm=pressure* 1000* n * temp
        
    return hajm

hajme_taadoli('liquid',200,2) #Out[76]: 536.0

hajme_taadoli('gas',200,2,3000) #Out[77]: 1200000000
hajme_taadoli('gas',200,2) #Out[78]: 80000000

def balaye_zamin(m,a):
    f=m*a
    return f

balaye_zamin(10,2) #Out[79]: 20

#koreye zamin , a --> 10
#hamishe

def balaye_zamin(m):
    f=m*10
    return f
balaye_zamin(10)

balaye_zamin(20)


#ke default-->hamishe a =10 bgire , shetab shetabe 10\
    #valia z ontrfm taraf ag bkahd avazesh kone betoone
    #dastressie ziad
    
def balaye_zamin(m,a=10):
    f=m*a
    return f

balaye_zamin(10)  #Out[84]: 100

balaye_zamin(10,2) #Out[85]: 20
#--------
def balaye_zamin(m,a):
    f=m*a
    return f

#
balaye_zamin(10,2)
balaye_zamin(m=10,a=2)


#agar shoam bkhay -->daste hsomas
#fght trf adad bzane 
#fght bayad esme argument a= felan
def balaye_zamin(m,a,/):
    f=m*a
    return f
balaye_zamin(10,2)

balaye_zamin(m=10,a=2) #kar nmikone

def balaye_zamin(a,b,/,*,c,d):
    f=a*b*c*d
    return f


balaye_zamin(10,20,c=10,d=20)



#-----ketabkhone ha ------
#parameer , default ......
print()



#======================
import numpy


#az dele numpy tabe hasho bekeshid  biron
#yek ->array --> araye misaze -->khoroji mdi emiriz

a=numpy.array([10,20])


import numpy as np
#dg gfotm np -->hamon nmpy
#sade tar code bzi

a=np.array([10,20])

import numpy as n
import numpy as x

#--->standard--->umpy ---> np
#pandas -->pd
#matplotlip-->mlp


#--------------------------------
import numpy as np   # hamishe improt ro balaye codeton bokoni

#list=[10,20,30] -->kond bodan(mohasebta), dobodi , yek bod 
#dobod-->radif , sotoon [jadval]

#0d
a=np.array(10)
a.ndim #0
a.shape #Out[107]: ()
#1d-->shabihe list
a=np.array(  [10,20,30,40]  )
a.ndim #1
a.shape #Out[109]: (4,)  -->4 ta adad
#2d
a=np.array(  [  [10,20,30],[40,30,20]             ]   )
a.ndim #2
a.shape #Out[113]: (2, 3)   2 ta radif , 3 ta sotoon
#3d......


#access
#1 d-->list
a[0]
a[1]
a[2]
a[2:6] #2,3,4,5
a[:4] #az aval
a[3:] # at akhar

#baray edobodi
#radif, sotoon
a[2,3] #radife felan comma, sotone felan

a[2,3:5] #radife 2 -->soton 3 ta 4 esho
a[2:6,3] #sotone 3 ,radife 2,3,4,5esho bde

#add
#tafirgh 
#dot
#+ - / *
#ya ba estefade az tabe

a=np.array([[1,2,3,4],[5,6,7,8]])
a.shape #Out[116]: (2, 4)

b=np.array([ [10,20],[30,40],[50,60],[70,80]   ])
#4 ta radi , 2 sotoon
b.shape #Out[119]: (4, 2)

#dot -->zarbe dakheli
#riaziat -->matrix

# matrixe aval (n*m )    bkhay zarbe dakhel matris (k*j)
#m=k

c=np.dot(a,b)


#===========
#assing
a=np.arange(0,100)

#reshape
#ham araneg
#shape e jadido

b=a.reshape(50,2)

b=a.reshape(2,50)


#random-->baid
#empty  shape  10   , (2,50)
#zero
#ones
#full -->ba felan adad poresh

#yek array besazi

#-------method + - add multiple ....pow
#yekseritabe hastan k dakhele numpy
#bezani np , tabe ro bekeshi
#too delesh array 


#round----------
a=np.array([-3.66,3.66])

new=np.floor(a) #b paeen gerd mikone
new=np.ceil(a) #b bala


#----yek array 1D mikhay biay miangin, maximum , minimu, sum

arr=np.array([20,30,432,12,32,32,23,34,2])
#mitoni brizi too zarf

np.mean(arr) #Out[128]: 68.55555555555556
np.max(arr) #Out[129]: 432
np.min(arr) #Out[130]: 2
np.sum(arr) #Out[131]: 617

#2D
arr2=np.array([  [10,20,30,40],[50,60,70,80] ])

np.mean(arr2)  #Out[135]: 45.0 doone done elemnta haro jam mikone taghsim bar kol
np.max(arr2)  #Out[136]: 80
np.min(arr2)  #10
np.sum(arr2)  #360

#vagty 2d ---> radif, sotoon
#sotooon-->axis=0
#radif--->axis=1

np.max(arr2,axis=0)  #array([50, 60, 70, 80])
np.min(arr2,axis=0)  #Out[140]: array([10, 20, 30, 40])
np.mean(arr2,axis=0) #Out[141]: array([30., 40., 50., 60.])
np.sum(arr2,axis=0)  #Out[142]: array([ 60,  80, 100, 120])


#radif ha-->khdoeton ejra konid -->quziebadi ersal shava

np.max(arr2,axis=1) 
np.min(arr2,axis=1) 
np.mean(arr2,axis=0) 
np.sum(arr2,axis=0) 



#-----
arr2


b=arr2[: ,2  ]


np.max(b) #Out[147]: 70


np.max(arr2[:,2]) #Out[148]: 70



#---------split
a=np.array([1,2,3,4,5,6])
new=np.array_split(a,3)


#-----where

new=np.where(a==2)
new=np.where(a==5)

a=np.array([10,23,34,45,50,60])

new=np.where(a>30)

#---------
#3 ta radif, 2 ta soton
b=a.reshape(3,2)


#----------- copy view
arr=np.array([1,2,3,4])
arr2=arr



arr[0]=100
print(arr) #[100   2   3   4]
print(arr2) #[100   2   3   4]

#harja numpy array 
#2 ta chizo baraabre ham ghrar dadi
#har taghiri jae dad onja ham etefagh miofte
#view
arr=np.array([1,2,3,4])
arr2=arr.view()

arr[0]=100
print(arr) #[100   2   3   4]
print(arr2) #[100   2   3   4]



#ag bkahy copy konii va taghira roye dovomie etegah
#az copy

arr=np.array([1,2,3,4])
arr2=arr.copy()

arr[0]=100
print(arr) #[100   2   3   4]
print(arr2) #[1 2 3 4]
#bejaye inke bnvsiim arr2=arr ya bnvsim arr2=arr.view()
#neveshtim arr2=arr.copy()


#============================
#---------JOIN---------------
#============================
#DOTA ARRAY RO BEHAM EBCHASBOONI
arr1=np.array([1,2,3,4])

arr2=np.array([5,6,7,8])


#axis=0 --->sotoon associated -->ham avikhte
#axis=1 -->radi associated -->ham avikhte


new=np.concatenate( (arr1,arr2) ) #axis=0

#axis=0 -->dar rastaye sotoon bechasboni
#new=np.concatenate( (arr1,arr2) ,axis=0)#---------


#radifi Numpy 1 D 


#1D-----> yek listeeeee soton , radiff matrah
#access [2]   niazi b comma
#az tabe ha estefade mikoni --> axis vojod ndre


#numoy arrat 2D -->radifo soooton
arr1=np.array([[1,2],[3,4]])

arr2=np.array([[5,6],[7,8]])



new=np.concatenate((arr1,arr2),axis=0)

new=np.concatenate((arr1,arr2),axis=1)




#vstack -->vertical stack --> amoodi
np.vstack()
#hstack -->horizontal -->ofoghi
np.hstack()


#dstakc
#stack....
np.stack()
np.dstack()




#=====================
#bkhay array ro jaee save koni tooye compue

np.save('esme_fil',kodom_array)

#save krdn
np.save('ali',arr2)


#lod krdn
np.load('ali')

np.load('ali.npy')


np.load('C://User/ali/arrray_ha/ali.npy')


b=np.load('C://User/ali/arrray_ha/ali.npy')
#dakheel yek zarf

#============================================
#==================MATPLOTLIB================

open('landing2.gif') #Out[200]: <_io.TextIOWrapper name='landing2.gif' mode='r' encoding='UTF-8'>

#FileNotFoundError: [Errno 2] No such file or directory: 'landin2.gif'






'''
search google

numpy -->bsihtar 
pandas -->
matplotlib

yek eetabkhoen jadid

donabel
getting start
user guid
documentation

tutorial
teaching


'''


#------MATPLOTLIB--------
#pip install matplotlib

import matplotlib.pyplot as plt #ag shod ok 
#ag nashod
#pip install matplotlib.pyplot
#plt


#va shoro mikonim baray erasm

#x = 1, y=5
#x=2 , y=10
#do ta noghte 
#Plt ketabkhonas
#rasm -->print
#naizi nsit brizi too zarf
#Numpy, pandas, scikit learn
#matplotlib , print

#dastooore
#yek tabe dre benam eplot
#beman x o y eto bde

x=[1,2]
y=[5,10]
plt.plot(x,y)




x=np.array([1,2])
y=np.array([5,10])
plt.plot(x,y)




#x ro nadi
#hkhdoesh ro az 0 ...
#x=[0,1,2,3,4,5,6]
plt.plot(y)


#*888888nokte-->naiz b hefz krdn nis
#dar nahayat shoam yedoone kode 10 hati az matplotlib ro

#--------
#do noghte ro  yeke abi vasl mikone
x=np.array([1,2])
y=np.array([5,10])



#-----fght khat---------
plt.plot(x,y)

#-----fght noghte---------
#dastam baze
#mikham fght noghte ro namayesh bade
plt.plot(x,y,'o')
#mikham setade bde bejaye  noghte

plt.plot(x,y,'*')
plt.plot(x,y,'x')
plt.plot(x,y,'H')

#-----ham khat  ham noghte---------
plt.plot(x,y,marker='o')
plt.plot(x,y,marker='*')


#size marker ro taghir bdm
#ms-->marker size
plt.plot(x,y,marker='*',ms=30)
plt.plot(x,y,marker='*',ms=50)
plt.plot(x,y,marker='*',ms=2)


#rangi konam -->noghte
plt.plot(x,y,marker='o',ms=50)
#mfc , mec  , ham toosh , ham doresh -->abie
#yek khato noghte, o -->nogthte o , ms -->50
#rango tgahir
#default hame rnaga abie
plt.plot(x,y,marker='o',ms=50,mec='r')
#mec-->doresho
#mfc-->toshoo
plt.plot(x,y,marker='o',ms=50,mfc='r')
#joftesh ro gehrmeze
plt.plot(x,y,marker='o',ms=50,mec='r',mfc='r')
#fght ghermez?
plt.plot(x,y,marker='o',ms=50,mec='m',mfc='g')

'''
tooye plt (matplot)


def plot(x,y, marker='o',ms=10,mec='b',mfc='b'):
    rasm
    
    
plot(x,y)
# az default ms=15 , blue


plot(x,y,marker='o',ms=20) 
plot(x,y,marker='0',mfc='r')



'''
#taghir bdim kahto
#yek kaht mikeshe
#dot anoghte vasl mikone

plt.plot(x,y)

#kahte frgh kone . kahte kamel
#line style-->ls
plt.plot(x,y,ls='-')
plt.plot(x,y,ls='--')
plt.plot(x,y,ls='-.')
plt.plot(x,y,ls=':')


#range line?
plt.plot(x,y)

plt.plot(x,y,color='r')
#*** mfc , mec -->noghte he ro rangesho taghir
#color , c -->range kaht ro taghir midn
plt.plot(x,y,c='r')


#rangaye dg
plt.plot(x,y,c='g')
plt.plot(x,y,c='y')

#tqarkibi az ghablia nogthe chin , g
plt.plot(x,y,ls=':',c='g')

#linewidth
plt.plot(x,y)

plt.plot(x,y,linewidth=20)



#hala baraye chan nogth eanjam bdi
x=np.array([1,2,3,4,5])
y=np.array([10,20,30,40,50])
#---- Shekle marker ha / marker style-----
'''
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline


'''


#----ranh ha / color-------
'''
'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White


همچنین برای رنگ ها کافیه برید سایت زیر
sitte e zir rangaro keshide va jolosh esmeshon
yani masalan bejaye 'r' kafie esme onaro bnvisid va rnagesh zaher mishe
https://matplotlib.org/stable/gallery/color/named_colors.html



#baraye colour map ha --> oonaee ke rangaye shedati hast
#yani bayad shedat bedid ham mitonid berid paeen begid
masalan az 0 ta 100 / biad gehrmez ba abi ya masalan zard b sabz ya ....

https://matplotlib.org/stable/gallery/color/colormap_reference.html


'''

#----- Shekle khat / line style -----
'''
'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'

'''

#mesal az chan noghte
#hala baraye chan nogth eanjam bdi
x=np.array([1,2,3,4,5])
y=np.array([10,20,30,40,50])

plt.plot(x,y) #fght khat , ahr 5 ta noghte ro ba ye kaht mcihsbone

plt.plot(x,y,'o') #Nogth eharo


plt.plot(x,y,marker='o') #ham noghte ham khat

plt.plot(x,y,marker='*',ms=20,mfc='r',linewidth=10,c='g') 



#-------formule

x=np.arange(0,100)
y=4*x

#100 ta x , y

plt.plot(x,y)
plt.plot(x,y,'o')

plt.plot(x,y,'o',ms=2)

plt.plot(x,y,marker='o',ms=2)


#sin , 
#math --> sin , cos --.fgth baraye 
x=0
import math


y=math.sin(x)
#numpy



import math

x=np.arange(0,100)

new_list=[]
for i in x:
    new_list.append(math.sin(i))


y=np.array(new_list)


plt.plot(x,y)

plt.plot(x,y,'o')

plt.plot(x,y,marker='o')


#---------
#na title na hichi.......
#dakheel shekl drim k taghir mdiim
#biron dairm-->titil e ,,
x=np.array([1,2,3,4,5])
y=np.array([10,20,30,40,50])
plt.plot(x,y,marker='o')

plt.title('nemoodare man')
plt.show()


#vase x va y ham title dahste basham?


x=np.array([1,2,3,4,5])
y=np.array([10,20,30,40,50])
plt.plot(x,y,marker='o')

plt.title('nemoodare man')
plt.xlabel('feshAr')
plt.ylabel('viscosity')
plt.show()

#khoshegl tar

x=np.arange(0,100)

new_list=[]
for i in x:
    new_list.append(math.sin(i))


y=np.array(new_list)



plt.plot(x,y,marker='o',ms=10,mfc='g',c='r')
plt.title('nemoodare man')
plt.xlabel('X haye man')
plt.ylabel('Sinoose x haye man')
plt.show()




plt.plot(x,y,marker='o',ms=10,mfc='g',c='r',ls=':')
plt.title('nemoodare man')
plt.xlabel('X haye man')
plt.ylabel('Sinoose x haye man')
plt.show()


plt.plot(x,y,marker='o',ms=10,mfc='r',c='g',linewidth=20)
plt.title('nemoodare man')
plt.xlabel('X haye man')
plt.ylabel('Sinoose x haye man')
plt.show()

#---------Matplotlib---- PLOT
#PIE CHART
#HISTORGAM (RANDOM STATISTIC)
#BAR
#SCATTER


#open file + PANDAS L11 PROJECT 2 RO MIDIM



#L12 - L16 ---> AI RO KHEDMAT TADIS 




#---------------------------
#quiz
#az numpy shoro konid estefade konid
#+ - 
#dot
#tabe haye join
#reshape

#8 ta nmpy array 
#be onvane Y 
#hamradifash x ham bdim arange

#x o y hae baham abrabar bashan

#b halat haye mokjtalef rasm konid




a=np.array([[2,3,4,5,6,7,8],[2,3,4,5,6,7,8]])
b=a+3

c=b*2


x=c[0,:]
y=c[1,:]*2


plt.plot(x,y,marker='o',ms=10,mfc='r',c='g',linewidth=20)
plt.title('nemoodare man')
plt.xlabel('X haye man')
plt.ylabel('Sinoose x haye man')
plt.show()


#------
#Q_L10_FNAM_LNAME
#Q_L10_AMIR_GHASEMI

#ai.2024.pilehvar@gmail.com
#------









