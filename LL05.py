
"""
Created on Sun Aug 18 17:46:05 2024

@author: Ali Pilehvar Meibody

L5
"""


'''
Python yek zaban
1-built in function ( print,inout,...)
2-keywords (dastoorat if else elif for while def)
 
zarf -->variable: {1-number(int,float,),2-str (tabe dashtan)
                   3-list ,set , touple, dic [tabe haee dashtan]}

'''

#Built in functions
#aval -->rangi 2--> parantezx dare 3--khoroj yek kari najam midan
print()
input()
type()
len()

#casting str int tbdil
int()
str()

a=-2
#absolute -->motlaghe 
abs(a)
#Out[42]: 2

a=[1,4,6,123,4,5]
max(a)
b=max(a)

min(a)

sum(a,) #Out[45]: 143
sum(list((1,2,3,4)))
sum([1,2,3,4])

#2**3
a=2**3
pow(2,3)

a=[1,4,6,123,4,5]
sorted(a) #tartib dehi

#horof A B C abc 
#123445
a=['Ali','ali',20,30,'BIA','bia']

sorted(a)




a=['Ali','ali','Bia']
sorted(a)
#A B C , a b c


a=list((1,2,3))
b=len(a)
print(b)

#mitoni too ham too ham brizi
#zarfg variable-->zakhire konan

print(len(list((1,2,3))))


#-----Keywords
if
else:
del
for
while
def

a=20

#==

a is 20
#Out[56]: False


#==
#moghayese


# if shart :

# == =! > <


# in  
#not in
a=[10,20,30]

20 in a
#aya 20 dakhel a hast?
#Out[57]: True

40 in a
#Out[58]: False

40 not in a
#Out[59]: True




#if ( shart ):
    #Misanje mibine true hast ya fdalse
    

#================
#hamrogeh gofti 'agar' felan beshe chi
#sharto besanji

'''
sakhtar
if shart:
    dastoorat [yek khaty ya sad khat]

'''
#@aval khat too python code benevisid
#magar mesle , if , else, for , while , try ,def, class


a=20
if a>10:
    print('ok')

#aval shart ro check mikone
#ag true (sahih bod)--> ejra mikne dastoore tooye body

a=5
if a>10:
    print('ok')

#shart
a==10 #aya a mosavbi ast ba 10 ? true ya false
a=10 # a ro bokon 10 --> 10 ro beriz dkahele zarge a


#==
#=!
#>
#<
#>=
#<=

#in
#not in
esm='salam'

if 'a' in esm:
    print('bale yaft shod')

#true bshe shart dastor 
#ag nashe
'''
yuek sharte
a>2
a<2
true false mide

'a' in esm
2 in esm
2 not in esm



'''
esm='ali'

if 'a' in esm:
    print('bale harfe a yaft shod')


esm='gol'

if 'a' in esm:
    print('bale harfe a yaft shod')


#gahi mikhay do shart ro biay check koni
a=30
b=40
#check koni a>20 , b>20
#ma vagfhty mikjaym dota sharto check konim
#1- ya jofteshh bayad sahih bshe
#2-ya hadeaghal yekodom azina

'''
har dota shaert bayad true bashe-->ham sene pedar ham sene madar
yeki az inj diota (hadeaghal yeki)-->ya sene pedar ya madar


'''
and #beyne do ta shart  #va  ham .. va ....
or #hadeghal yeki  # ya sene pedar ya madar

a=5
b=40

#bashgah 
#bayad har do nafar seneshon balaye 18 bashe

if a>18 and b>18:
    print('befarmaeed dakhel')


#yek bashaghe dgas
#hadeaghal ye nafar ham shdoe sensh balaye 18 bashe
if a>18 or b>18:
    print('befarmaeed dakhel')
    




#agar nabood (false)-->rad mikone mire baghie code
#ama agar yevaght khasti begii
#agar in shart true bod klare 1 ro kon 
#ag nabodo felan akro (kare 2)
#if else
'''
if shart:
    dastoorate1
else:
    dastooorat2
    
*soal agha chera jolo else -->shart nmziarim

agar a >20 benevis salam
agar nabodo ( a<=20)-->benevis khodafes



hamechi az sdhartemon miad
agar doros bod datsoore 1
agar nabood dastoore 2
dorahi

'''
#farghe if , if o else

a=20


if a>30:
    print('shoma ghabool shodi')



a=20

if a>30:
    print('shoma ghabool shodi')
else:
    print('shoma sene lazem ro ndri')



#gahi migi
#agha age sharte aval doros bod dastoore 1
#age nabood (dobare yek sharte dg mizari)

#yek dorahi hast true false
#dobare false (zamani k shart doros nis) --> dorahi mishe

#ag balaye 30 shod --> 1500
#1000
#200

if a>30:
    print('gheymat : 1500')
else if 
    print()


a=24
if a>30:
    print('gheymat : 1500')
elif a>18:
    print('gheymat : 1000')
else:
    print('shoma bayad 200 toman bdi')
#baze bandi mikoni
#yerk do rahi dar nazar bgir k dobare dorahi shode

#and or

if a>20:
    if b>30:
        print('salam')
    print('khodafez')
        
    
    
b='salam'

b.find('s') #Out[86]: 0


c=b.find('b') #-1 agarf nabashe #Out[87]: -1

d=None

#chizhaee k javabn nadaran--> -1 , None

esm=input('esmet chie')

shomarande=esm.find('b')


if shomarande==-1:
    print('shoma dar esmat b nadari')




#ya
if 'b' not in esm:
    print('shoma dar esmat b nadari')



if 'b' not in esm and 'a' in esm:
    print('name shoma ghabol shod')

    
# if shart1 and shart2
#QUIZZZZ----
a=['user1','user2','user3']
new_user=input('saalam esmetoon chist: ')

a.append(new_user)

print('salam liste jadimeon update shod: ', a)



#----
#adade 1 , adade 2 , amalgar
print('salam arz shod in yek barnameye macxhine hesab az tarafe GAMLAB hast')
print('---------------------')
print('---------------------')

adad1=float(input('adade avaleton ro befarmaeed:'))
adad2=float(input('adade dvometoon ro befarmaeed:'))
amalgar=input('amalgare morede niaz ro entekhab kon (jam,tafrigh,zarb,taghsim):')


#type(amalgar) #Out[93]: str
#print(amalgar) #jam

#agar nevesht jam biam adade 1 adad 2 jam konm printesh 
#@gaar--> if
#agar nabood

if amalgar=='jam':
    javab=adad1+adad2
elif amalgar=='tafrigh':
    javab=adad1-adad2
elif amalgar=='zarb':
    javab=adad1+adad2
elif amalgar=='taghsim':
    javab=adad1/adad2
else:
    print('amalgare morede niaz yaft nashod')
    

#------------
print('salam arz shod in yek barnameye macxhine hesab az tarafe GAMLAB hast')
print('---------------------')
print('---------------------')

adad1=float(input('adade avaleton ro befarmaeed:'))
adad2=float(input('adade dvometoon ro befarmaeed:'))
amalgar=input('amalgare morede niaz ro entekhab kon (jam,tafrigh,zarb,taghsim):')
if amalgar=='jam':
    javab=adad1+adad2
    print(javab)
elif amalgar=='tafrigh':
    javab=adad1-adad2
    print(javab)
elif amalgar=='zarb':
    javab=adad1+adad2
    print(javab)
elif amalgar=='taghsim':
    javab=adad1/adad2
    print(javab)
else:
    print('amalgare morede niaz yaft nashod')
    

#--------

print('salam arz shod in yek barnameye macxhine hesab az tarafe GAMLAB hast')
print('---------------------')
print('---------------------')

adad1=float(input('adade avaleton ro befarmaeed:'))
adad2=float(input('adade dvometoon ro befarmaeed:'))
amalgar=input('amalgare morede niaz ro entekhab kon (jam,tafrigh,zarb,taghsim):')

if amalgar.upper()=='JAM':
    javab=adad1+adad2
    print('javabe shoam shod:',javab)
elif amalgar=='tafrigh':
    javab=adad1-adad2
    print(javab)
elif amalgar=='zarb':
    javab=adad1+adad2
    print(javab)
elif amalgar=='taghsim':
    javab=adad1/adad2
    print(javab)
else:
    raise TypeError('lotfan amalgare morede naiz ro dobare benevisi')
    
    
a=int(input('adad bede begam zoje ya fard'))

#baghimondash b 2 --> agar 0 bshe zoje agar nashge farde

if a%2==0:
    print('zoj')
else:
    print('fard')
    
    
email=input('Insert your email')

#yekseri shart check konjim agar nabhod bgim agha emaielto doros
#ya bareax

if '@' not in email:
    print('not valid')
elif len(email)<24:
    
if 
if
if
    




emtiaz=0
if '@' in email:
    emtiaz=emtiaz+1

if len(email)<25:
    emtiaz=emtiaz+1
    
    

#
if emtiaz<1:
    
    
#****** Passdword
javab=input('confirm?')
a=['yes','si']

if javab in a:
    print('successss')




#===============================
#8review--> if if else, elif --> 'AGAR'
#===============================
#Halgeh ha----
#Tekrar--->10 bar print salam
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')


#100 bar bekham chi?
#for
'''
sakhatr

for tekrar:
    dastooorat
'''

#shomarande darim ---> a , b , c , i , zarf
#10 bar benevis print 

# agha bia ye i besasz
#ye range ham bde --> (1,2,3,4,5,6,7,8,9,10)
#i ro kari ndrim
#tekrarrrrr

for i in range(1,11):
    print('salam')



#40,41,42,43,44,45,46,47,48,49,50
for i in range(40,51):
    print('salam')

#vali norm
for i in range(0,10):
    print('salam')
    
    
'''
sakhatr

for tekrar:
    dastooorat
'''

#vaghtty khastrid 10 bar benevisdi salam -->tekrar
#az skahtare zirf

for i in range(0,10):
    print('salam')


#python chiakr mikoneeee
'''
***
i ro besaz 
range [0,1,2,3,4,5,6,7,8,9] 10 ta ragham

aval i ro mziare 0 dastore zir ro ejra mikone
i ro mziare 1 dastpre zir ro ejra mikone
i ro mziare 2 dastoore zir ro ejra mikone
.......
i ro mizare 9 dastoore zir ro tyekrar mikone 

miad biron mire edameye code

'''
for i in range(0,10):
    print('salam')

#yani khode i ro aya mitonim estefade konim

for i in range(0,10):
    print(i)

#[0,1,2,3,4,5,6,7,8,9]
#aval i ro mziare 0 --> print(i) --> 0
#i ro mizre 1 --> print(i) -->1
#....
#i ro mziare 9--> print(i)-->9

'''
0
1
2
3
4
5
6
7
8
9


'''


#0 ta 10 type koni
#[0,1,2,3.....,100]
#hasrdafe i ro az aval bzar 
#i o bzar 0 dastoore paeen (print(i))
#..
#i=10

for i in range(0,101):
    print(i)



#[0,1,2,3,4,5,6,7,8,9]
for i in range(0,10):
    print('salam')
    print('khoobi?')
    
    
for i in range(0,10):
    print(i)
    print('salam')
    


#----
for i in range(0,10):
    print('salam')

#yani khode i ro aya mitonim estefade konim

for i in range(0,10):
    print(i)


'''
for -->
yek shomarande niaz dare (i , a , b , ....)
#yek range , tabeye range, list , str
#yek dastoor ya bishtar

yek shomarande ke az start number, end number --> hery dastoor ro ejra
halghheye for

'''
    
for a in range(0,10):
    print(a)
    
#List

for a in list((1,2,3,4,5,6,7,8,9,10))


b_list=[1,2,3,4,5,6,7,8,9,10]
for i in b_list:
    print(i)
    
#nmaid 
#Miad shoamrande ro mziare too rangii
#bad done done dastore zir ro ejramikone ta tah
    
#adade dg bzara??
b_list=[40,54,276,4322,534]
for i in b_list:
    print(i)
    
    
    
for i in b_list:
    print('salam')
    
#i elzamie?-->:choon hsoamrandas ejaze bede
#halgehye for kar kone

#dar vaghty k shoam tekrar mikhay miotoni dar badaneye dastoor az i estefade nkoni
#gahi vagta niaz dari estefade koni

#dastemoon--
#ya shoma az raneg estefade mikoni
#tekrar

#vaght mgii felan ghadr (10 bar) yek dastoroio anjam midon
for i in range (0,10):
    print()
    

#iteration --> bazzressi , varresi
b_list=[40,54,276,4322,534]

for i in b_list:
    print(i)

#dare varresi mikone
#barsaye har jzoii k dar list hast felankaro kon

#pas shoam na tanha print

#mikhay y list dari mikhay b harkodom yedone ezadfe koni  printesh koni

b_list=[100,200,300,400,500]


'''
101
201
301
401
501
'''
#beram iteration->beram dakheel yek list , taghiresh bdm

for i in b_list:
    b=i+1
    print(b)

'''
101
201
301
401
501
'''


#hala man donbale karaye bsihtaram
#varesi haye sakht tar



#fek kon yek list
#az sene afrad
#mikham sen haek balaye 18 sal hast ro print konm(dastoor daste toe)

a=[10,5,43,65,17,23,19,28]

#beram tooye list , done donashono 
#varresii--> iteration
for i in a:
    if i>18:
        print(i)

#mitoni hamishe print nakoni , count (bezhmnori)
a=[10,5,43,65,17,23,19,28]
#c
#count
#zswiljse
count=0

for i in a:
    if i>18:
        count=count+1


#hichi ndad
#hich dastore print
#balke omde 
#count ro hey update

print(count) #5

#count+=1    count=count+1
a=[10,5,43,65,17,23,19,28]
count=0

for i in a:
    if i>18:
        count+=1

print(count)




#chiaye dg ro check konm
#dakhele list becharkham avse khodam

#dobare

for i in range(0,10):
    print(i)

b_list=[10,254,56,23]
for i in b_list:
    print(i)


b_list=[10,'vahid',56,'hamid']
for i in b_list:
    print(i)


#hatman baya dlist bashe
#str -->yek listi az characxter ha hast
esm='salam'
# s a l a m

for i in esm:
    print(i)
    
#ham too list, ham too str mitone iteration




#soal chekc konid esme karbar a dare y ana
esm=input('salam esmetpobegoo:')

#rahe aval
if 'a' in esm:
    print('a dar esme shoam vojod darad')




#rahe do
esm=input('salam esmetpobegoo:')
for i in esm:
    if i=='a':
        print('bale ma a darim')
        
        
        
'''
esm= mehran
i = m chek mikone 
i = e
i = h
r
a --> if i=='a' -- > bale ma a darim
i= n 

'''
    
#baran 
esm=input('salam esmetpobegoo:')
for i in esm:
    if i=='a':
        print('bale ma a darim')
        
#count    
esm=input('salam esmetpobegoo:')
count=0
for i in esm:
    if i=='a':
        count=count+1
        
        
  
        
#print(count)  
if count>0:
    print('shoma dar esmeton a darid')


#----Pishrafte tar
esm=input('salam esmetpobegoo:')
count=0
for i in esm:
    if i=='a':
        count=count+1
        
        
  
        
#print(count)  
if count>0:
    print('shoma dar esmeton',count,'ta a darid')


#====================
#====================
#QUIIZZZ-----
#-------------------------------------------------------------------
#quiz 1 --if
'''
-------------BMI CALCULATOR-----------------------
yek barname besazid ke vazn va ghad ro begirad az karbar
vazn ro taghsim bar ghad be tavane 2 kone ( yani aval vazn ro be tavane 2 kone
                                           badesh ghad ro taghsm bar oon adad kone)
agar oon adad kochiktar az 18.5 bood bege under weight, ag beyne18.5 ta 25 bood bege normal
age beyne 25 ta 30 bashe bege over weight agar beyne 30 ta 35 bood bege obese agar
balaye 35 bood bege very obese




یک برنامه بنویسید که وزن و قد رو از کاربر بگیرد و قد رو به توان دو کند و وزن رو تقسیم بر آن کند
اگر زیر 18.5 بود بگه کم وزن اگر بین 18.5 تا 25 بود بگه نرمال اگر بین 25 تا 30 بود بگه اضافه وزن
اگر بین 30 تا 35 بگه چاقی و اگه بزرگتر از 35 باشد بگه چاقی مفرط

'''


#----------------------------------Q2
#az karbar password begire * bezane (print)
#ba halgheye for inkaro anjam bdan



#Q3-----
#adade 5 ta 147 ro print konid ba estefade az for

#Q4------
#dar liste zir begardid tedade adade bishtar az 100 ro peyda konid
numbers=[10,21312,123,12,233,231,33,23,54,43,653,213,223,22,13,76]
#chanta adad dar liste bala hast k bishtar az 100 hastand



#Q5-----FUN - pishjrafte
#email
#yek  passwor dbegire
#behesh az 1 ta 4 emtiaz bde  poor, fair , good, strong
#bege chghd gahvie
# @ A m adad --> emtiaz





#----quiz Pishrafte
#-------
# Input:
# Enter countdown time in seconds: 10

# Output:
# 10 seconds remaining
# 9 seconds remaining
# 8 seconds remaining
# ...
# 1 second remaining


'''

Q_L5_FNAME_LNAME

AI.2024.PILEHVAR@GMAIL.COM


'''







        

        
    
    
    
