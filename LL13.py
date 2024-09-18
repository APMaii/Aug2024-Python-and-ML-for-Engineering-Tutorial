
"""
In The Name of GOD

Created on Wed Sep 18 18:04:14 2024

@author: Ali Pilehvar Meibody

LL13
"""
#-----------
#L2
#ESMESHOOON 
#Description
#gahan --> unicode
import pandas as pd
df=pd.read_excel(r'desktop/....../file.xlsx')
#r poshte masir


#change column-------> 
#1-----> dar heyne import
df=pd.read_excel(r'desktop/....../file.xlsx',header=None,names=['esme1','esme 2'])



#2-bad az import
df=pd.read_excel(r'desktop/....../file.xlsx')
df.columns
#esme column haro neshon mide
df.columns=['esme1','esme2']


#uplaod kardid

def tabeye_prokject_2(data,application):
    stress=data['stress']
    strain=data['strain']
    #......    

import numpy as np
#arange, random 


import matplotlib.pyplot as plt
def beta_tabeye_prokject_2(stress,strain,application):
    
    if application=='plot':
        plt.plot(strain,stress)
        #title, xlaberl, ylabel
        plt.show()
        
    if application=='max_stress':
        max_stress=max(list(stress))
        return max_stress

stress=np.arange(0,100)
strain=np.arange(0,100)*20

beta_tabeye_prokject_2(stress, strain, 'plot')
beta_tabeye_prokject_2(stress, strain, 'max_stress')


#-----baragrdam

def tabeye_prokject_2(data,application):
    stress=np.array(data['stress'])
    strain=np.array(data['strain'])
    #copy paste
    if application=='plot':
        plt.plot(strain,stress)
        #title, xlaberl, ylabel
        plt.show()
        
    if application=='max_stress':
        max_stress=max(list(stress))
        return max_stress

#data=pd.read_csv(......)
#tabeye_prokject_2(data,'plot')


#vakonesh --> zaman,dama , darsad
#data --> 3 ta sotoon 


#24 

def asli_tabeye_prokject_2(data,application):
    time=np.array(data['time'])
    temp=np.array(data['temp'])
    percentage=np.array(data['percentage'])



    


def beta_tabeye_prokject_2(dama,zaman,percent,application):
    if application=='temp_time':
        plt.plot(time,temp)
        plt.show()
        
        
    elif application=='percentage_time':
        plt.plot(time,percentage)
        plt.show()
        
        
    elif application=='temp_percentage':
        plt.plot(percentage,temp)
        plt.show()
        
        
        
    #elif application=='max_percentage':
temp=np.random.normal(loc=24,scale=1,size=(100))
time=np.arange(0,100)/3
percentage=np.arange(0,100)

beta_tabeye_prokject_2(temp,time,percentage,'temp_time')
beta_tabeye_prokject_2(temp,time,percentage,'percentage_time')
beta_tabeye_prokject_2(temp,time,percentage,'temp_percentage')


#----ino bsazam bdm b A2_FNAM_LNAME
def my_plot(x,y):
    plt.plto(x,y)
    #plt.ylabek
    
    #plt.xlabel
    #......
    
    
    
    
def asli_tabeye_prokject_2(data,application):
    time=np.array(data['time'])
    temp=np.array(data['temp'])
    percentage=np.array(data['percentage'])
    if application=='temp_time':
        my_plot(time,temp)
        plt.plot(time,temp)
        plt.show()
        
        
    elif application=='percentage_time':
        plt.plot(time,percentage)
        plt.show()
        
        
    elif application=='temp_percentage':
        plt.plot(percentage,temp)
        plt.show()
        
        

temp=np.random.normal(loc=24,scale=1,size=(100))
np.argmax(temp) #Out[16]: 16

#----**
#error 
#chizi  k khasti
#google search

#python ro bnvisi
#numpy , pandas , .....


#---safe aval khdoe oon padckage pandas, mnumpy
#stackoverflow--> awlie


#---------

#===================
'''
temp=np.random.normal(loc=24,scale=1,size=(100))


'''
#====================

'''
========================================
========================================
========================================
========================================
========================================
========================================
 Machine learning and Artificial Intelligence
========================================
========================================
========================================
========================================
========================================

'''


'''
L1----> MACHINE (computer,mobile,...) -->BOX , FELEZ
NA HOOSH,DARK, YADGIRI HICHHHH INTELLIGENT

LAMP -->TRANSISTOR --> 0 1 --> 000010100010010010100010100100101001010
#PYTHON (IDE)---> TRANSLATOR

#DASTOOOOR

in adad zakhire
adad + -
if 
for



#-------
hooshmand vaghean anjam

#do nasl azh hoshe masnoe


'''
#---------Nasle 1---> yek hsohe masnooe sade
#hooshe masnoe nabode , jazabiat
#if else khodemon

msg=input('salam roozeton bekheyr janam dar kehdmatam')

if msg=='salam':
    print('salam')

elif msg=='khoobi':
    print('mersi to khoobi?')

elif msg=='mamnoon':
    print('chekhabar?')

#slam 
#Salam

msg.upper()


msg=input('salam roozeton bekheyr janam dar kehdmatam')

if msg.upper()=='salam':
    print('salam')

elif msg.upper()=='khoobi':
    print('mersi to khoobi?')

elif msg.upper()=='mamnoon':
    print('chekhabar?')

#------bishtar hoshmand
msg=input('salam roozeton bekheyr janam dar kehdmatam:   ')

if msg=='salam':
    print('salam')



msg=input('salam roozeton bekheyr janam dar kehdmatam:  ')

if 'SALAM' in msg.upper():
    print('salam')

#---------------
#-----1000 ta code

#prompt detection


msg=input('salam roozeton bekheyr janam dar kehdmatam:  ')

if 'KHARID' in msg.upper():
    print('baraye sefaresh b shomarey 009891900000000 tamas bgrii')
elif 'ADDRESS' in msg.upper():
    print('addresse ma jahanshahr hast')

#---ta yek had intelligent (hooshmand)

#support ha

#----------------------------
#cnc , automat , robot

#----
#for
#if
#TK -->pacjkage-->GUI
n=int(input('chanabr boresh bde'))
for i in range(0,n):
    send.signal()

#robot ---> nasle 1 
#rule-based


#40 m ---> 1.5 sanie

#laser bzni kamtar az 1.5 saanie baragrde

#jesme nazdik tar az 40 m , 20 , 10 


#time=

if time<1.5:
    
    break

#rule_base




#------NASL1 ---------


#NASLE 1------
#1-----> moshekel shoma bayad 10000 khat bnvisi
#done done
#support--> salam , kahrid ,s efaresh , bekahrma bekahri , bekharad,.......
#cnc , robot-->  40 bar yek karo najam bde , khodesho bhtr , ..........
#tashkhis ---> 1.5 agar omd, agar kam tar 1.3 chikar break 
#2-----
#improve , behbood nemiabe , pishraft nmikon b morore zaman
#

if signal !=0:
    #.....
    #.....
    
    
#rooye pash fght biofte

    
#---
#yad bnegireeeee




#----------------
#1--->kootah tar
#2---->ghoveye yadgiri

#---ENSAN--->MOJODE HOOSHMAND
#vorodi (input)--->cheshammone, gooshemone , damaghe,zaban , dastemoon --->
#maghz ( calculartion) --> yadesh migirim ,mantegh kasdb krdim
#khoroji --> tasmimie , actione , amlai (dast , dahan)

#------psudo code
'''
voordi 
calcualtion
khoroooji

if else
AI nasle 1


#------------------
voordi 
calcualtion (yadesh begire , yadgiri nadare)
khoroooji



#------skahte AI nasle 2
voorodiii
asli , body (Learning ) ghanoni, relationship, manteghi
khorooji ( decision ,print, amal)



#---> soal hja

'''

#1---->vooroodi---> data , dade , dataaaa  ( AI , Data_based  mobtani bar dade)
#2----> yad bgire az dade , ravehs haye statistical (amari) hast va bahash yad migire . rabete ee ro
#3- nesbat b oon rabete, kario najam , print , namayesh bde , tolid kone




#-------Tamame soalate hastio , jahano msihe b masaeli bnam input() outpu() tabdil krd
#-------masale e ek mikhay kar konim
#----ychizi bde , tahlilo pas bdm
#support --> customer bnvise (input) ---> ---> javab b soalesho
#---->
#----> dama , feshar evakonesh bedam -----> box ----> estehkam pishbini kone (khoroji)
#man mikham bhsh y ax bdm --->box----> sag ya gorbe (khoroji)

#AI BOX



#clc
#clear

'''
CORE------ HASTEYE BAHS

kole masaele jahan

input---> BOX --->output

AI --> boxe dar nazar bgire

ychi bdm bhsh ychi bgirm



#mesle ensan bashe
#1--vorodi ro bgire
#2(too dele box)--> az vorodi ha yad migire (ravehs haye amari), yek mantegh (rabeteye beyne vorodi va khoroji ro dar miare)
#3- khoroji bde

Tarife workflow (tarigehye kar) yek AI
chijori yad migire...........

ML , AI ,.........
AI ---> ( 70% ML )

#nasle 1 , behine sazi (riazi)--->riazi khales, gahdimi

#AI --> 70% -->ML -->MACHINE LEARNING


'''

#----------------
#Note1: kole masaele jahan ro tabdil kon b input ouytput  [yek rabete ee beytne vorodi va khoroji hast]
# AI 

# input ----> BOX ---> Output

#box(AI) -_.rabeteye beyne vroodi khoroji ro yad bgire (ravehs haye amari)
#ya dgrf
#bhsh vorodi bde , bar asase ooon rabete k yad grfte bht khoroji mide

#ravesh chie??? chijori kar mikone ... ejaze


#------------------

#----vARAGHO BVARAGRDOONIM
#yek mabhase dg

'''
Regression 
رگراسیون

SIMPLE -->SADE

ML NIST XXXXXXXXXXXXX


mesal:
    
    voorodi , khorojii dashte bashe
    va in dota mortabet bashan
    
    
    
3D printing.............
[har dastgahi dar har hite ee , dar nazar vbirid]
setting dare 
quality parameter ( estehkam , baraghi, rnagesh , kahrba bdon doros, tasmim mgirid k in khoobe ya bade , 10 az 100 , 80 az 100 , )


dastgahi --> 3d printing

setting ( dama , speed, infill percnetage (made a), angle )
dama=25 , speed= 80 , zavie = 60
. . . . . . tolid mikone ostokhone masnoee
mibri test mikoni--> [ inja barmaoon estehkamesh moheme, keshidandegi,l khastegish , ... rnagesh , ekyfiat] quality parameter

adadie 0 ta 10000   [ 0,1]  [5.65 ta 7.33232]


70000


#shoma mikhay b estehkam 10000

daama?
speed?
zavie?

dama ziad she estehkam ziad mishe?
speed ziad she /// // // ?
zavei / / / // / / // /  ?



hey bri try error
test hey test
ta sob......


#---------------
3d printing(setting ---> operation ---> quality)
electrospining (setting --> operation ---> quality (darsade takhalkhol))
injection machine (setting, dama,feshar, sorate , dore extreuder)--> operation ---> qualkity (estehkam , )
Non traditional cutting ( EDM, Waterjet ,....) (setting , faseley noke waterjet ta mahsol ,.) --> operttion --> (surface roughness)
Sulphur removal reactor setting (dama, catallyst,)-->operation --> quality ( benzine khobi has ya na --> khoob / bad   | parameter --> Co2 kg emission)
Osciloscope -->




input (daste mae , moteghayerre , ma taghiresh midim) ---> operation ----> quality parameter ( vabaaste hast , b aer asase gahblie)

#-----------
#natije giri-->zamani k ma migim 3 d printing mannzooramon tamame datsgah  ha va tamame jahaee shoma darid kar mikonide

3d printing(setting ---> operation ---> quality)

(input--->  ----> output(qualtiy parameter))




'''

#setting---->ma mitonim taghir bdim.....
# Temp
#(50-100)

#speed 
#(0-100)

#dg ham dre sabet dar nzr bgriid ( ya nmitonim ya nmsihe ya hrchi) sabet

#---quality parameter--->barmaon moiheme-->ma measure mikonim-->bar asase oon mgiim khobe ya bade
#--->estehkam --> ostokhone lagan ---> 7000
#nirooye ziad vared mikone --.hjarja shekast ---> mige inja hadeaksar nirooe --> bishtarin nirooe k oneste tahamol kone MaxForce MF - estehkam

#2000 esthekam kamesh

#4000 

#70000 estehakm bsihtar

#100000


#man chan mikham?/-->nazdike lagane ensan  


#---> 7000 



#---------------
#Miram tooy azmayeshgah manam o y datsgah
#made ro briz (PLA) 
#speeed, temp bzn --> chan bznm??
#boro vase jra


#---->chra khdomon adad nmgiim?
#choon hich etelaee ndrim ke

#sppeedo ziad bzrm --> estehakm ziad msihe?
#temp ziad bzrm ---> esthekam ziad msihe?

#spped , temp ch rabete ee ba estehakm drn???
#input output problem ---> relationship between inputs and output

#relationship between speed, temp and quantity parameter ( Estehkam)
#???????

#...........
#-----SPEED , estehakm chie

'''
farze avalie:  Yadeton bashe ma farz krdim --> k vroodi ha ba khrooji ha yek rbaete ee drn [ag ndhste bashn chi??? --> 100 , 200 , 300 ,40 0 10 20 30 7000 7002 70003]
farzie dovom: rabete khatie 


pas ghabol yek rabeteye dar tabiat jahan hasti , beyne speed va estehkam
sorat o estehkam hast? hcihki nmidone joz 'khoda'


speed ziad she estehakm ziad mishe ya na   khoda
ag speed 2 baraar she estehkam chan barabar msihe??   khdoa
-->ma nmdioonim ama mdionim yek rabete ee in beyn has
va ma mikhaym bdast biarimesh


'''
#FEK KON in rabtee he vojod dare


x=np.linspace(0,100,100)
y=70*x + 200


plt.plot(x,y)
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
plt.grid()
plt.show()

#MAN VA SHOMA AZASH BA KAHAB RNISTIM?

#in rabet emige speed ziad she --> estehkam ha m ziad mishe
#age speed 2 barabar ziad bshe
#y=70*x + 200
# speed ---> quality (estehkam)

#estehkam = 70 * speed + 200
#rabete dar nature (tabiat hast) khoda midane

#--------------
#tramame ravaebet vorodi khrooji khati

#y = a*x + b
#y khoorji
#x voroodi


#a=1 #b=0

x=np.linspace(0,100,100)
y=1*x+0


plt.plot(x,y)
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
#plt.xlim(100)
plt.ylim(0,1000)

plt.grid()
plt.show()



#shib tagir bdi a ro tagir bdi
x=np.linspace(0,100,100)
y=5*x+0


plt.plot(x,y)
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
plt.ylim(0,1000)
plt.grid()
plt.show()


#shib tagir bdi a ro tagir bdi
x=np.linspace(0,100,100)
y=10*x+0


plt.plot(x,y)
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
plt.ylim(0,1000)
plt.grid()
plt.show()



#arz az mabda --> b

x=np.linspace(0,100,100)
y=10*x+200

plt.plot(x,y)
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
plt.ylim(0,1000)

plt.grid()
plt.show()




x=np.linspace(0,100,100)
y=10*x-200

plt.plot(x,y)
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
plt.ylim(0,1000)

plt.grid()
plt.show()



#**** Hargoone kaht bkhay bsazi kafie bnvisi
#y= a*x + b
#ba tgjhire a va b mitoni har khati k doos dri ro bsaziiiii


#------Azmayeshgah
#rrabet ro nmdionim


#speed ---> estehkam ch rabete e dare??
#---------
'''
Mirim too azmayeshgah va maslaan 5 ta dade entekhab mikonim va 
5 bar azmayehs mikonim

az koja
1-->
2-->
3-->
4-->
5-->

DOE (design of experiment)

boxe data

speed , tmep 
(0,100)   (50,100)



#bar asase 
#CH ETDAD
#16 , 8 ,, 32

100 speed 100 temp
0 speed 50 temp 

#FCC BCC



#8 bar brm anhayat test konm
minitab
design expert anjam mide

#----Mahdoode , 10 million



#dastemon baze...
#ghadim data bode yek frdi dashte 

'''

#
a=np.array([ [10,1200],[20,2044],[30,4043],[40,5500] ])

# 5 tatest grfte
'''
speed 10 ---> rolid , ---> esthekam  1200 niroo mitone tahamol kone
20  ---> 2044
30 --> 4043
40--->500

vaghty miri migiri 
azmayehs mikoni ---> fahmidi rbaete he khatie , va vaghty 
speed zia dmsihe estehkam ziad msihe


y =  a*x +b

estehakm = a* speed + b
#in rabete dar jahan
chijori bdast bairam?/


crh amikha
estehakm = 4* speed + 5

#speedeto mziri toosh -->estehakm ro dr miari
bejay e inke
 #niazi nadari b azmayeshgah b--->nokteye bahse





'''





'''
Man faghat noghat ro daram 
chi mikham???? --->oon khate ro



masale -->regresssion


az noghatam ----> chijroi brsm b oon moadel (a*x+b)


'''

#estehkam = a * speed + b
#a o b ro nmidonm


for a in range(0,100):
    for b in range(0,100):
        
        
#a 1  b 0
#a 2  b 0
#a 3  b 0
#a 4  b 0

#------------REVIEW-----------------
#-----> 4 ta dade , noghte
# -0--> y= A * x + B dar tabiat
#A , B 
# 4 ta


#ravesh estefade konm ta rabete ro dar bairam


#ravesh-->regression


#y=a*x+b harchi khat delet bkahd bkshi dar jahan







#donabel kahjte --> A , B 


#datye mane
import pandas as pd
a=np.array([ [10,1200],[20,2044],[30,4043],[40,5500] ])


data=pd.DataFrame(a,columns=['speed','estehkam'])
plt.scatter(data['speed'],data['estehkam'])
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
plt.grid()
plt.show()
#============
#random a o b 
#a=1 b=0  --> COST PARAMETER:10000000
#a=10 b=0---COST PARAMETER:50000
#a=100 b=0  --> cost = 800
#a=100 b=200 --> cost = 780
#a=100 , b=600
#a=4 b=100




import pandas as pd
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


#dasti anja midam

#yek function

#maiod random , va khdoesh done done

#a ro hey taghir mide a=1 ...... b =0 ,....
#har kaht k mikeshe , majmooe mroabaate fasele ro hesab mikoen --> eyk adad --> msianje chgdh in khati k ma hads zadim b kole noghat nazdik
#cost ro baraye har kaht hesba mikone


#az beyne kole khat ha ooni k kamtarin cost ro dare mire va a , b sh ro dar miare

import pandas as pd
y=100*x+600
x=np.linspace(0,100,100)
plt.plot(x,y)
plt.title('3D PRINTING GRAPH')
plt.xlabel('Speed')
plt.ylabel('estehkam')
plt.ylim(0,7000)
plt.grid()
plt.show()

#baraye ensan --> ch adadi estehkam monaseb???
#7000
y=100*x+600
x=(7000-600)/100
print(x)
#@yek lagani bsazam k monasbe ensan bashe (esthekam =70000)
#x speed 64.0




#----------
'''
moshekle ma??-->
vcorodi khrooji

setting ---> quality parmaeter

dar jahane hasti yek rbaete ee vojdo dare
estehkam = A* x + B
ma agar in rabete ro bdonim kafie x ro bzri toosh y robdast bairi bjaye inke beri azmayesh anjam bdi





yekser data dahstim --> DATA ( 4 ta noghte)
regression --> miad random mire done done a , b haye motefave mizne (khate haye motefave mikeshe  khate1 , khate 2 ,khate 3,...kahte 10000)
bafraye harkodom faseleye in khat ro ba tamame oon noghat ro hesba mikone ( faselke ye harnogthe ba khat**2 + nogthe dovom b alave khat)
har khati k random hads zadim --> yekchzi dare bename cost (fasele)


az beyne 1000 ta khat --> ooni  k kamtarin fasele ro dare ---> khate bartar
a , b ---> tasmim migire

a --> A
b---->B

ma mitonim A va B ro bdas bairim???


Estehkam = A*speed + B

rabeteye beyne sorat va estehkam ro bdast biariii




****** 
input---> box -->output
speed --> box --> estehkam 



voroodii---> 4 ta noghte data
box (learning)--> relationship between x and y (A , B)
khoroji --> mziare too rabtee va y ro mide (pishbini mikone bar ase oon mantegh)



AI
x va y --> raveshe regression 



ravehs haye motefavet darim va ziadn
1 , 2 ,.....


LL14------
ravesh dobare dar hade 5 daghigeh review
(in gehsmataye akharo dobare ghabla z jalaseye badi)

codesho bznim

ravehs haye dgar ro ---> ravehs ML ro tadris konim



1---> agar fght yek x nabod chi? ham speeed ham temp
2---> agar rabete khati nabood chi?

#fekr mikonid
Q13_fname_lname


ai.2024.pilehvar@gmail.com


LL13
LL14
LL15
LL16
PROJECT3

HALE PROJECT

file -->telegram ghara nmigirad

'''





