
"""
In The Name of GOD

Created on Sun Sep  8 17:43:48 2024

@author: apm

L11-------------
SECTION1--->PYTHON , built in function , keywords, logic,variable type (int,str,list)
Section2-->libs (math,numpy,matplotlib,statistics,pandas)
section3---> AI

"""
import numpy as np
a=np.array(1)
a=np.array([1,2,3,4])
a=np.array([[1,2,3],[4,5,6]])
a=np.arange(0,100,2)
a.ndim
a.shape
a.resize()
#+ - * / 
# np.add()  np.
#np.concat()   np.vstack()  np.hstack()
#niazi nist k hamaor hefz konim ama tarigehye estefad o bayad bfhmim

#list -->function -->apply mishod
#str -->khoroji midad
np.add(arr1,arr2)
arr1=np.array(1)
arr1.add()


#**alageh mandan
#ALAGHEMANDAN---> DOCUMENTATION KHONDAN SHORO KONID
#BALATAR --> GITHUB SOURCE CODE np.add chiak rmikone
#add --> def add(input) -->tooye body


#-----plt----.RASM-----------
#rasm ---> haminjori, dade hato bekhay analys , yek khato , data
#bekhay result hato a=320 b=4500 
#matplotlib --->documentation
#Mohemtarin-->
#niazi b hefz nist --> b inke ghelgeh ro yad bgiri


#ye 10 khatesho hamishe copy mikoni va nesbat b khast ehat taghiresh midi

import matplotlib.pyplot as plt
# matplotlib.pyplot in ketabkhoans ... yani dastressi bhsh spyderam
#plt-->yani harj agoftm plt manzorma in ketabkhone esm toolanias


plt.
#yani boro tooye plt
#yani in ketabkhone boroo too delesh felan tab ero var


#-----tabe haye ziadi dare
#plot
#scatter
#bar
#pie
#..... algahmenadan-->documentation


#tabeye plot 
#adad , list , numpy array
#do ta noghte  [0,10] xet 0 yet 10 . [5,20] xx-->5 y--20 
#x haro ye taraf   
x=np.array([0,5])
#y haro ye taraf
y=np.array([10,20])


#dota noghte darim
#***** in xe dota noghte oon y dota noghte


plt.plot(x,y) #yek khat rasm mikone -->dota noghte ro bham michasbne


#ag 4 ta bahse 4 taro mcihasbone
x=np.array([0,5,10,20])
#y haro ye taraf
y=np.array([10,20,33,40])

plt.plot(x,y)

#fght noghte-->yek arg  o ,x *  -->che shekli noghte
plt.plot(x,y,'o')
plt.plot(x,y,'x')
plt.plot(x,y,'*')

#ya kaht 
#ya noghte
#ham khat ham noghte  (marker)
plt.plot(x,y,marker='*')

#range birone noghte, range dakhele nogthe ha
#size noghte
#khdoe style khat nogth echin , 
#sizesho
#rangesho taghir

#default -->abi, size mamoli 
#arg--> 
'''
marker='o'  shekle noghte
ms=  marker size . andazeye noghte =50
mec=   biroon   rnag ('r','g',...)
mfc= dakhel
ls= style khat  : -- -.
linewidth -->andaze khat
c=   range khat 

'''

plt.plot(x,y,marker='*',mec='r',mfc='g',ms=20,ls='-.',linewidth=13,c='y')
#hamey settinf ha ag chizi nanevsi abie
#in dakhele tasvir bood
#bayad brionesham title ha
plt.plot(x,y,marker='*',mec='r',mfc='g',ms=20,ls='-.',linewidth=13,c='y')
plt.title('nemoodare man')
plt.show()

#man abray edars plt.show()
#tahe tamame codaton
#harja rasm khasti
#plt.show()


plt.plot(x,y,marker='*',mec='r',mfc='g',ms=20,ls='-.',linewidth=13,c='y')
plt.title('nemoodare man')
plt.xlabel('salam paeen')
plt.ylabel('salam chap')
plt.show()

#fontesho ?? bale

#------LIST , TOUPLE, SET , DICTIONARY
'''
DICTIONARY
Hello : سلام
play : بازی


'''
#int too zarf mirizi , str 
#list --.chanta adad ro too khodesh mzire
#touples,et,dictionary-->chanta zarfo too delesh b soorat haye mokhtalef mizare

#mese list, 
listt=[1,2,3,4]
#shift + bracket -->
zarf={ 'hello' : 'salam' ,
      'play':'bazi'}
#kilid :content
#bjaye index
zarf['hello']
zarf['play']
#ba adad ham bokonm
zarf={ 'size' : 14 ,
      'language':'farsi',
      'size_title':20}

zarf['size'] #Out[25]: 14

zarf['language'] #Out[26]: 'farsi'

#---------------

plt.plot(x,y,marker='*',mec='r',mfc='g',ms=20,ls='-.',linewidth=13,c='y')
plt.title('nemoodare man')
plt.xlabel('salam paeen')
plt.ylabel('salam chap')
plt.show()


#por okon-->template
myfont={ 'family':    ,
        'color':    ,
        'size':     }



myfont={ 'family': 'serif'   ,
        'color':  'red'  ,
        'size':  20   }

plt.plot(x,y,marker='*',mec='r',mfc='g',ms=20,ls='-.',linewidth=13,c='y')
plt.title('nemoodare man',fontdict=myfont)
plt.xlabel('salam paeen')
plt.ylabel('salam chap')
plt.show()
#baray ehar title
#title()  xlabel()  ylabel()
plt.plot(x,y,marker='*',mec='r',mfc='g',ms=20,ls='-.',linewidth=13,c='y')
plt.title('nemoodare man',fontdict=myfont)
plt.xlabel('salam paeen',fontdict=myfont)
plt.ylabel('salam chap',fontdict=myfont)
plt.show()

#------

title_font={ 'family': 'serif'   ,
        'color':  'red'  ,
        'size':  20   }

xy_font={ 'family': 'serif'   ,
        'color':  'green'  ,
        'size':  10  }



plt.plot(x,y,marker='*',mec='r',mfc='g',ms=20,ls='-.',linewidth=13,c='y')
plt.title('nemoodare man',fontdict=title_font)
plt.xlabel('salam paeen',fontdict=xy_font)
plt.ylabel('salam chap',fontdict=xy_font)
plt.show()


#+===========
#do ta khhat
#avalie abi -->efault ha
#narenji 

x1=np.array([0,5,10,20])
#y haro ye taraf
y1=np.array([10,20,33,40])


x2=np.array([2,7,11,30])
#y haro ye taraf
y2=np.array([30,60,73,80])

plt.plot(x1,y1,c='r')
plt.plot(x2,y2,c='g')
plt.show()

#plot()---> rasme khat hast
#=====================
#data -->noghte , point --> scatter()

x1=np.array([0,5,10,20])
#y haro ye taraf
y1=np.array([10,20,33,40])

plt.plot(x1,y1) #4 ta nogthe ro ye khat khali
plt.scatter(x1,y1)
#hamoon
plt.plot(x1,y1,'o')


#yekam bishtar access mide b point ha
#chiza arg 

plt.scatter(x1,y1)

plt.scatter(x1,y1,color='r')
#**color tooye plot range khat ro avaz mikrd
#scatter ->fght ba point, rnage point ro avaz mikone

#na tanha range kole noghat avaz koni
#done done
liste_colors=['r','r','g','g']
#bejaye 'r' list ro bzae
plt.scatter(x1,y1,color=liste_colors)


#---- shedat bzari
#bejaye inke begam 'r' 'r' 'g' 'g'
colour_shedat=[10,20,30,40]

plt.scatter(x1,y1,c=colour_shedat,cmap='viridis')
#shedate paeen ro ch rngi konam?

#https://matplotlib.org/stable/users/explain/colors/colormaps.html

plt.scatter(x1,y1,c=colour_shedat,cmap='inferno')
plt.colorbar() #hatman bzn mitoninzni

#bejaye coloru shedat --> bdoe sevomo midan

#size  hamaro
plt.scatter(x1,y1,color='r',s=60)

#ya done done
liste_size=[10,20,30,70]
#bejaye 60
plt.scatter(x1,y1,color='r',s=liste_size)


#alpha -->shafafiat



plt.scatter(x1,y1,color='r',s=liste_size)
plt.scatter(x1,y1,color='r',s=liste_size,alpha=0.2)
#0 ta 1
#kamrang tar .....
#baraye har nogthe

alpha_list=[0.1,1,0.5,0.6]
plt.scatter(x1,y1,color='r',s=liste_size,alpha=alpha_list)

#--->scatter-->baraye noghat hast
#vali valiii
#ejaze mdie na tanha hameye nogat setting avaz kon
#vase done donashon ham avaz konam




#dakhel
#koli------------
#4 ta noghte  scatter-->data point
#khat --> plot() --> y = 2*x -->moadele ro rasm kone



x1=np.array([0,5,10,20])
#y haro ye taraf
y1=np.array([10,20,33,40])
c_shedat=[10,20,30,40]
size_list=[50,30,20,10]
alpha_list=[0.1,0.4,0.4,1]
plt.scatter(x1,y1,c=c_shedat,cmap='viridis',s=size_list,alpha=alpha_list) #dakhel
plt.title('NEMODARE ZIBAYE MAN',fontdict=title_font)
plt.xlabel('mokhtasat')
plt.ylabel('porosity') #font dict mitoni
plt.colorbar()
plt.show()


#yekam bsihtar 
plt.title('NEMODARE ZIBAYE MAN',fontdict=title_font,loc='left')
#left
#right
plt.title('NEMODARE ZIBAYE MAN',fontdict=title_font,loc='right')

#pad


plt.title('NEMODARE ZIBAYE MAN',fontdict=title_font,loc='right',pad=40)


#bad az title ghrar bgire
#------
x1=np.array([0,5,10,20])
#y haro ye taraf
y1=np.array([10,20,33,40])
c_shedat=[10,20,30,40]
size_list=[50,30,20,10]
alpha_list=[0.1,0.4,0.4,1]
plt.scatter(x1,y1,c=c_shedat,cmap='viridis',s=size_list,alpha=alpha_list) #dakhel
plt.title('NEMODARE ZIBAYE MAN',fontdict=title_font)
plt.xlabel('mokhtasat')
plt.ylabel('porosity') #font dict mitoni
plt.colorbar()
plt.grid()
plt.show()

#grid bandi
#too delsh .. 


#kadie copy apste va bri kamel bbini

x1=np.array([0,5,10,20])
#y haro ye taraf
y1=np.array([10,20,33,40])
c_shedat=[10,20,30,40]
size_list=[50,30,20,10]
alpha_list=[0.1,0.4,0.4,1]
plt.scatter(x1,y1,c=c_shedat,cmap='viridis',s=size_list,alpha=alpha_list) #dakhel
plt.title('NEMODARE ZIBAYE MAN',fontdict=title_font)
plt.xlabel('mokhtasat')
plt.ylabel('porosity') #font dict mitoni
plt.colorbar()
plt.grid(axis='x')
plt.show()




#-----------------------------
#----------------------------


x1=np.array([0,5,10,20])
#y haro ye taraf
y1=np.array([10,20,33,40])
c_shedat=[10,20,30,40]
size_list=[50,30,20,10]
alpha_list=[0.1,0.4,0.4,1]
plt.scatter(x1,y1,c=c_shedat,cmap='viridis',s=size_list,alpha=alpha_list) #dakhel
plt.title('NEMODARE ZIBAYE MAN',fontdict=title_font)
plt.xlabel('mokhtasat')
plt.ylabel('porosity') #font dict mitoni
plt.colorbar()
plt.grid(color='green',linestyle=':',linewidth=2)
plt.show()

#PLOT, SCATTER , BAR, HIST
#====================================
#=============================
#=============================
#=============================
#=============================
#-----PIE CHART---------------
#yek dayere k az chan bakhsh tahskil shod ebashe
#a harkodom y andaze e dahste bashe
#roosh yechizi bnvsii


#dayere .  size, label

lab=['apple','banana','cher','daa']
size=[50,30,10,10]
plt.pie(size,labels=lab)
plt.show()

#array
lab=['apple','banana','cher','daa']
size=np.array([50,30,10,10])
plt.pie(size,labels=lab)
plt.show()


#rang ahto hamkhdoet

lab=['apple','banana','cher','daa']
size=np.array([50,30,10,10])
myc=['green','red','blue','black']
plt.pie(size,labels=lab,colors=myc)
plt.show()


#-------

lab=['apple','banana','cher','daa']
size=np.array([50,30,10,10])
myc=['green','red','blue','black']
ex=[0,0,0.2,0]
plt.pie(size,labels=lab,colors=myc,explode=ex)
plt.show()


#===============documentation


#---------------------------
#bar , histogram, 
#barchart-->dade haye sotooni 
#label , megdhar
x=['A','B','C','D'] #LIST, ARRAY
y=np.array([3,8,1,10])
plt.bar(x,y)
plt.show()


x=['A','B','C','D'] #LIST, ARRAY
y=np.array([3,8,1,10])
plt.bar(x,y)
plt.title('NEMODARE ZIBAYE MAN',fontdict=title_font)
plt.xlabel('case ha')
plt.ylabel('jamiat')
plt.show()

#rang

x=['A','B','C','D'] #LIST, ARRAY
y=np.array([3,8,1,10])
plt.bar(x,y,color='r')
plt.show()


#andaze sotonha

x=['A','B','C','D'] #LIST, ARRAY
y=np.array([3,8,1,10])
plt.bar(x,y,color='r',width=0.1)
plt.show()
#yek adad beyne 0 ta 1



#plot() scatter() pie() bar() -->dakhele tasvir ., argument haye khas
#title. xlabel, ylabel, plt.show() plt.grid() --> birone tasvir baray ehame yekie

#------------
#histogram---------- --> baraye distribution -->tozih

#random 
import random
#pip install random ag nabood

#yek adade random beyne 0 ta 10 bhm bde
a=random.randint(0,10)
print(a) #7  #4  #3
#integer --> randint
#havaset hardfe k run koni codo random
#frgh

#float ashari
#float beyne 0 o 1
a=random.random()
print(a)
#0.4268899519316225
#0.2771309483194745

#float to yek range 0 1 . 0 ta 10 
#0 ta 100 
#0 ta 200 
#150.32  , 140 , 130  , 10 , 60
#
#0 ta 200 bhm yek float bde
# 100 , 50 , 1 , 199 baham abrabare?

#---->distribution ha chist 


#do no toziii---> uniform , normal(gussian)

#ag bkhaym baraber --> uniform 
#ag na bekhaym begim notght emarkazii --> normal



#review---------
a=random.randint(0,10)
#1-yek adade sahih beyne 0 ta 10 , 4 , 5 6,7

a=random.random()
#2-yek adade ashari beyne 0 ta 1


#3-ag yek adade ashari beyne yek range (start to end)
#3-1 -->hame shanseshon yeki-->uniform
a=random.uniform(0,10)
#az beyen 0 ta 10 yek adade float
print(a)
#1.5892620535412394
#1.093201532087521
#3.5930833160340656

#3-2 nromal , gussian -->mitoni to begi k az koaj ehtemalash bsihtar
#mean , dispersion
#mean-->kodoma dad bishtar ehtemal midi bht bde
#chghd 
#0 ta 10 -->
a=random.gauss(5,2)
print(a)


#dispersion --<kamtar konm , bishtar 5 mide



#-------------------
#choice entkehab mikone
a=random.choice([1,2,3,4])
print(a)



#shuffl---------- (train, test)
random.shuffle([1,2,3,4])
print(a)




#------NUMPY --> AZ HAMIN TBAE RASNDOM
#numpy--.random dare , tabe

a=np.random.randint(0,100)
print(a) #83 , 12


a=np.random.randint(0,100,size=(2,5))
print(a) #83 , 12

#random abram yek array 2 ta radif, 5 ta sotoon
#hame element haro , yek adade random beyen 0 ta 100 vardar


#np.array()
#np.arange
#np.random

#float beyne 0 ta 1
a=np.random.rand()
a=np.random.rand(100)

#rnage ro taghir bdm 
#uniform , nroml

a=np.random.uniform(0,100,size=(2,5))

# yek array 2 ta radi 5 ta soton 10 ta adad
#adadaro mrie beyne 0 ta 100 random mzire float
#uniform -->adadi entkehab mikoen beyne 0 yta 100
#shanse yeksan daran



#agha boro holohosh hamaro 50 behem bdi 
#random abla paeeen
#loc --> miangin miu , too kodom adad ehtemal
#scale= -->dispersian , bsihtar bashe adad aprt tare

a=np.random.normal(loc=50,scale=1,size=(2,5))

#yek array 2 ta radif , 5 ta sotoon
#10 ta
#in 10 ta ro aksaran doroavre 50 por mikone


#--->hist

a=np.random.uniform(0,100,size=(800,))

plt.hist(a)
plt.xlabel('adade entekhabi')
plt.ylabel('faravani')
plt.show()

#nroml

a=np.random.normal(loc=50,scale=1,size=(800,))

plt.hist(a)
plt.xlabel('adade entekhabi')
plt.ylabel('faravani')
plt.show()


#hist()-->fsaravaani , uniform, gussian yad grftim



'''
OVERVIEW:
    MATPLOTLIB
    
    RASM
IMPORT matplotlib.py plot as plt
plt. esme tabe


plot() ---> KHAT   too ye parante  (x,y,marker= , mfc= , mec, ms, s, c,ls, linewidth=)
scatter()--->noghte . betonim baarye done done noghat moshakahst liste_colour, liste_size , ...
pie() ---> yekd ayere label, andaze 
bar() ---> yekseri dade haye sotooni
hist() -->faravani ra namayesh (uniform , gussian) distribution (tozie dade)

#ina hame dkahel boodn moraba
#brirone morab dastet baze
plt.title() #to dele hame onchizi k mikhay bnvisi , fontdict= , pad, loc
plt.xlabel()
plt.ylabel()
plt.grid() #rangesho, nogthe , sizes


#****
plt.show()



#inaro chanbar 
#yek tmeplate hamishe save dari
copy paste x o y taghir midi



#3d , .........
#3d scatter.....

plot() ,....
surface(),....

https://matplotlib.org/stable/plot_types/index.html

** seaborn


normal , gussian




'''
#================================
#----------PANDAS----------------
#-------------------------------
#---------file handling---------------
#--------------------------------
'''
psudo  code
1-vroodi--> a=20 , a=np.array() , arange(),def(),file ro bairim???
2-body --->moahsdbat
3-khoroojii-->print, return (def),, plot rasm mikrdim


'''
#python-->built in functiontabe dakheli --> open
#txt. ax , csv ,...
'''
.txt
.csv (excell )
.png
.jpg
#ax

'''
open()

#yek tabe ast --> dota vorodi
open(  vroodi1 , vorodi2  )
open('esm ya masiresho',' ')

#vorodi1

#kh sade -->  esme file dot format .txt .csv .png .jpg

open('koli.txt') #aksaran in kar shdoani nsi


#spdyere shoam ->foldere door oftade 
#axeton , fil e yeja dg bashe


#rahe aval--->miri samte rast Files, jaee k filet has ro mari
open('koli.txt')

#rahe dovom---->bejaye inek bri smate rats too file ha
#beri rooye filet bzni, proeprties, directory
open('/Users/apm/Desktop/koli.txt')
open('C://Users/ESM/downloads/koli.txt')

#ttx csv,png, jpg

#------directory---------
#mikhay chiakr koni?
#1---file eto bkhoni ---> r 
#2---> chizi benesvisi --> w  
#3--->b tahesh chizi ezafe koni --> a [ag file e vodoj nadahste bashe msiazatesh]
#4---> filet voojod nadahste bde ,e rror bde -->x

#mikham bkhonm
open('koli.txt','r')



#ag bkhay taghir bdi
open('koli.txt','w')

#b tah efile 
open('koli.txt','a') #ag file e nabashe msiazzatesh
open('koli.txt','x')  #ag nabashe nasaze
#x va a b tah ezafe mikone
#ama ag file vojdo ndshte bashe a misaze, x error 

#in tabe behet khoroji mide


zarf=open('koli.txt','r')

zarf.read()

#chanat character
zarf.read(5)

#y line
zarf.readline()


zarf.close() #tamam



#bazesh
zarf=open('koli.txt','w')

zarf.write('ezafe shavad')

zarf.close()



zarf=open('koli.txt','a')
zarf.write('ezafe shaavd')



#----TEXT ----
#in kar ---> kh kh mansoookhe

#tabe haee tooye ketankhone ha hastan -->open 
#khdoeshon open() --> ax , data va va a........

#csv, excelll   pandas.open_file('koli.txt')

#-----------------------------
#------PANDAS------------------
a_list=[1,2,3,4]

a1=np.array([1,2,3,4])
a1[1] #Out[193]: 2

a2=np.array([[1,2,3,4],[5,6,7,8]])

a2[2,3] #radife felan, sotone felan

#biam baraye array bejaye idnex, esm bzaram
#pandas

#pip install pandas

import pandas as pd
#Series , DataFrame
#series ,.......
#1---> array 1 bodi hast 
b1=pd.Series([1,2,3,4])


b1=pd.Series([1,2,3,4],index=['a','b','c','d'])
b1[1] #Out[194]: 2
b1['b'] #Out[195]: 2



#manam mitonm 2 bdoy ---> DataFrame

b2=pd.DataFrame([ [1,2,3,4],[5,6,7,8]])



b2=pd.DataFrame([ [1,2,3,4],[5,6,7,8]])
#ag esme radif ro taghir ->index
#ag esme soton -->column

b2=pd.DataFrame([ [1,2,3,4],[5,6,7,8]],index=['a','b'])

b2=pd.DataFrame([ [1,2,3,4],[5,6,7,8]],columns=['temp','pressure','time','quality'])


#pandas-->man array daram fght to mitoni beja idexo soton esm bzari
#ag array1 bodyy ----> pd.Series()
#ag do bodie soton radif, jadval ---> pd.DataFrame()

#index-->idnexa
#column

b2=pd.DataFrame([ [1,2,3,4],[5,6,7,8]],index=['a','b'],columns=['temp','pressure','time','quality'])



#-------------------
#open-------
#csv , excell, docs ,....... vared koni
a=pd.read_csv('ftir_output.csv')



#===============================
#dota sotooon 


#in data ro be soorate numpy darim 

#dade haye azmayeshgahi? -->koli radif, koli sotooonn 

#yek dade ee darim 
#search,payam ,......
#too htieye khdoeton 
#------------------


#---------------------


















