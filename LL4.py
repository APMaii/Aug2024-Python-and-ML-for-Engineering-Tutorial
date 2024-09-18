"""
In The Name Of God

Created on Wed Aug 14 17:55:19 2024

@author: Ali Pilehvar Meibody

----L4-----

"""


'''

#Overview
Python--Zaban
mesele har zaban

Vocab (kalamat)---> Built in function (narenji)

Grammar (dastoorat)->Bnafash

baghie chizharo-->Zarf dar nazar migire




'''
#Vocab (kalamat)---> Built in function (narenji)
print()
open()
input()
len()
type()
int()
str()
float()
bool()
#dakhele tabe haye dakheli ham mitoni
#moteghayer bzari ( a , b)
#ya khdoet mostaghim chizi bnvisi

#dastoorat
if
else:
for
while

esm=
zarf=
variable=
moteghayer=

'''
dakhele moteghayer ha (zarf)
1-numbers (adad ha):
    1.1. int [ 1,2,3,4,5,6,7,8,...]
    2-.float (ashari example: 1.4223)
    3.complex ( 1+3j)
    
    amalgarha mohasebe --> + - * 
    amalgharhaye moghayese--> > < >= <=  == =!

2.boolean ( True , False)
'''
a=2*3-1
# ()  ** * / + - olaviat
#acal zarbo anjam mide bad -

# ma pishenhad mikonim az parantez estefade koni
a=2* (3-1)


#amalgarhaye dg ham darim --> sharti
#to mikhay besanji , moghayese koni

a=True
b=False
#dar kenare inke mitoni inaro zakhir ekoni
#mitoni yeseri maodelat ro
#moghayese koni

print(4>2) #True

a=4090812
b=321218
print(a>b) #True
print(b>a) #False


print(a>=b) #True
print(a<=b)


print(a=b) #ghalatt.......
#in yani a mosavi ast ba b --> assign , meghdardehi
#agar bekahhi moghayes ekoni
print(a==b) #aya a ba b barabar ast?
#False
a=4
b=4
print(a==b) #True

#if , for ,.....

'''
3-str -->reshte
ali 'ali'
2 '2'

'' darand--> yani str hastand (harf,kalame,jomle)

'''
#3.1 assign
esm='ali'

#3.2 type
print(type(esm)) #<class 'str'>

#3.3. size (len)
print(len(esm)) #3
print(len('ali')) #3

#3.4.access  esme zarf beraket [index]
#index ha az 0 shoro msihod
esm[0] #Out[28]: 'a'
esm[1] #Out[29]: 'l'
esm[2] #Out[30]: 'i'
esm[3] #IndexError: string index out of range

#3.4.1. slicing 
esm='alipilehvar'
esm[0:4]
#esm_zarf[start:end]
#yani k man indexe start , ..., end -1
##** end ro shamel nmishe
esm[0:4]
#0 , 1 , 2 ,3    [4 shamel nmishe]
#Out[32]: 'alip'

#sade sazi
esm[:4] #az 0 b bala
esm[4:] #ta akhar


esm[0:8:2] #az 0 ta 7(8-1) , 2 ta 2 ta
#Out[33]: 'aiie'

#3.5. function -->
#function --> baraye khdoe pythonb bood-->rangi mishod
#esmo minvshti parantez too delsh chizi
print()
#bnaraye hame chi boodan
print(2)
print('ali')
print(2.4)

#vali ina --> str function --> tabe haye makhsose string ha
a='salam'
a.upper() #Out[34]: 'SALAM'
#esme zarf ro biarim roosh noghte bznim tabeye morede nazr ro estefade konim
#eshtemalan mikhay zkahirahs koni
#emal nmishe balke yechi tahviul mide *******
#uyani nemire a ro taghgir bde
#balke khoroji mide
print(a) #salam

b=a.upper()
print(b) #SALAM

#quiz L3.1
text='hello, dear students, please interact with other studentd for improving your skills in programming and please note that this is really important and vital part of your life in the new life of programming'
print(type(text)) #<class 'str'>
print(len(text)) #203 harf, character, space
text.upper()
b=text.upper()
print(b)

text.count('a') #Out[45]: 13

new_text=text.replace(',','')
jadid=new_text.split(' ')


#quiz l3.2
#یک برنامه بنویسید که از کاربر یک عدد بگیرد 
#و عدد رو تقسیم بر ده کند + ۸ کنه 
#، نمایش بده بگه عدد محاسبه شده ی شما فلان هست
adad=input('Salam, beman yek adad bedid: ')
new=(adad/10)+8 #TypeError: unsupported operand type(s) for /: 'str' and 'int'

print(type(adad)) #<class 'str'>


#int

adad=int(input('Salam, beman yek adad bedid: '))
new=(adad/10)+8
print('adade jadide shoma hast: ',new)





adad=float(input('Salam, beman yek adad bedid: '))
new=(adad/10)+8
print('adade jadide shoma hast: ',new)


#فان------------------------------------
#از کاربر یک پسورد بگیرید و ستاره چاپ شود
#سختی موضوع: تعداد ستاره به اندازه ی تعداد پسورد باشه


#fun
password=input('lotfan pass bnvisid:')

type(password) #Out[58]: str
len(password)


password=input('lotfan pass bnvisid:')
print('your password is :',len(password)*'*')


#Pishrafte

adad=input('3 raghami bde:')

print(adad[::-1])

b=adad[::-1]
print(type(b)) #<class 'str'>

#yek str grfdte
#vcharacterasho az akahr b aval nvshte

esme_kamel=input('lotfan esm va esme falimitoon ro bbnvisid: ')
final=esme_kamel.title()
print('esme kamele shomast: ',final)



#-----b soorate adadi azat begire

adad=int(input('yek adade 3 raghami bde: '))
#print(type(adad)) #<class 'int'>

#876

# 876= 8 * 100  + 7 * 10 + 6
#adad=876
sadgan=int(adad/100)
dahgan=int((adad - (sadgan*100) ) / 10)
yekan=adad- (sadgan*100) - (dahgan*10)

#print(sadgan) #8
#print(dahgan) #7
#print(yekan) #6

#678 = 6*100 + 7*10 + 8
new_adad= (yekan*100) + (dahgan *10) + sadgan

print('adade varooneye shoma shod :', new_adad)


# //  khereje ghesmat 
# % baghimande
adad=int(input('yek adade 3 raghami bde: '))

sadgan=adad//100
dahgan=(adad - (sadgan*100) ) // 10
yekan=adad- (sadgan*100) - (dahgan*10)
new_adad= (yekan*100) + (dahgan *10) + sadgan

print('adade varooneye shoma shod :', new_adad)


#----Variable ( Zarb ha )-----
#chanta chiz , chanta moteghayer, chanta adad zakhir ekonim chi
#List , set , .....
# 4   87  74 
#1.assign (meghdardehi)
a=[34,65,10,23]
b=list((34,65,10,23))

print(a)
print(b)

sent='hello I am new student'
bb=sent.split(' ')

#2- type
print(type(a)) #<class 'list'>

a=['ali','mohsen','vahid']

a=[10,10.5,1j,'mohsen',True]


#3-access (dastressi)
a='salam'
a[2] #Out[90]: 'l'

a=[34,65,10,23]
a[2] #Out[91]: 10 joze x om va az 0 shoro mishe

#** dar asl str yek no list hast k 
#az jozhaee b name character tashkil shode va
#b ham chasbondatesh

a=[10,10.5,1j,'mohsen',True]
a[4] #Out[92]: True
a[1:4] #Out[93]: [10.5, 1j, 'mohsen']


#change-------
#aval access koni bad taghir
a[3]

print(a[3]) #mohsen
a[3]='ali'
print(a) #[10, 10.5, 1j, 'ali', True]


#msle str ha ham function darim------
#fght baraye list hast
#insert---
#ezafe koni
a=[10,20,30,40]

# a=[10,20,25,30,40]
a.insert(2,25)
#kodom index, che chizi ezafe koni
#chizi pas nmidee**********

#str ha---> tavabe khoroji dahst
#---> bayad zakhirash mikrdi
#vali khode zarfge asli taghir nmikrd


#***ama dar list ha -->tavabe apply emal mikone
#rooye zarfe asli, variable asli
#mkhoroji nmide
print(a) #[10, 20, 25, 30, 40]


#------Farghe emal ba khorooji------\
#function hash str-->khoroji dare, emal nmishe
esm='salam'
esm.upper()
print(esm) #salam


#function haye list--> khoroji ndre, mostaghim emal mishe
a=[10,20,30,40]
a.insert(2,25)
print(a)




#-----------LIST FUNCTIONS------
#insert(index,value)
a=[10,20,30,40]
a.insert(2,25)

#append(value)
#ag bkham b tah ezafe konm chi
#bayad hey beshmoram bgm felan index
a=[10,20,30,40,50,60,70,80,90,100,110]
a.append(22)
print(a)
#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 22]


#---Join-----
a=[10,20,30,40]
b=[50,60]
c=a+b
#yek zarfe ezafe sakhtim a o b ro chasbondim

a.extend(b)
#b ro ezafe mikone b a


#ewmovw
a=['ali','reza','vahid','hamid']
a.remove('vahid')
print(a)#['ali', 'reza', 'hamid']

#ba index hazf konam
a=['ali','reza','vahid','hamid']
a.pop(2)
print(a) #['ali', 'reza', 'hamid']
 

#aya mishe yek liste khali sakht?
listt=[]

#yek list ro khalish kon
a.clear()
print(a)


del a
print(a) #NameError: name 'a' is not defined

del b
del c

#delet va ckear fargh dre
'''
append()	Adds an element at the end of the list

clear()	Removes all the elements from the list

copy()	Returns a copy of the list

count()	Returns the number of elements with the specified value

extend()	Add the elements of a list (or any iterable), to the end of the current list

index()	Returns the index of the first element with the specified value

insert()	Adds an element at the specified position

pop()	Removes the element at the specified position

remove()	Removes the first item with the specified value

reverse()	Reverses the order of the list

sort()	Sorts the list
'''
a=[10,5,4]
a.sort()
print(a) #[4, 5, 10]
a.reverse()
print(a) #[10, 5, 4]



# set , touple, dictionary 
#mesle list hastan
#assign, access, 
#manetgh hamoone

#list--> tekrari, hazf koni , add koni, tartib (index)

#-------------------------------
#------------------------------
'''
Kole python : yek zaban hast k 3 ghesmat dare

1-Vocab (kalamat)---> Built in function (narenji)
print, input, open, ....

2-Grammar (dastoorat)->Bnafash

**1,2, reserve shdoan -->rangi mishan
***baghie chizaro bnvisi sefid--> zarf

3-baghie chizharo-->Zarf dar nazar migire
    1-numbers, 2-str , 3-list (shabih set,touple,dict)
    
*assign , access, function

'''
#---Grammar--->Dastooorat--------

#ta alan python chika mikrd
#vaghty mineveshti mese safe chat ta send nazani
#kole neveshte haye shoma hich taghiri dar CPU 
#taghiri ijad nmikone,
#send payameto too etlegram
#run bzni codeto (ghesmate codeto) too IDE (spyder)

#run 
#az bala b paeen
#asz chap b rast mikhone
#ignore-->: # ''' ''' comment , point , note

#gahi vaght ha ma niaz darim
#vasate code az bala b paeen mikhone
#ye sharti bzarim 
#ya khodemoni --> ( agar ...)



#SHART AGAR ------> IF

#harjae goftri agar felanbeshe chiii
#---> yek sharti ro bekhay check koni (hamoon agararo)
#if ....

'''
structure:
    
if shart:
    
    dastoorat

'''
IF #NameError: name 'IF' is not defined

#donoghte nazari XXXXX
#shart ro b if bechasboni XXXXX
#AG DASTORATETO ZIRE IF BENEVSII XXXX
#yek tab fasele


#shart --> amalgharhaye sharti estefade koni
# > < == =! >= <=

a=40

#Mikhaym bgim ag in adad bishtar az 30 bod felan karo kon

#----> AGAR inb shart sahih book , felan karo kon
#----> shart (shart) ,, kar (dastoor)
'''

if shart:
    dastoorat


Agar in joori shod(shart) in karo (dastor) anjam bde
'''
#agar bishtara az 30 bodo adad ---> benebvise tabrik


a=

if a>30:
    print('tabrik')

    

#test---
a=40

if a>30:
    print('tabrik')

    
a=20

if a>30:
    print('tabrik')
#hichkari nmikone


#*** Agar in joori shod(shart) in karo (dastor) anjam bde



if a>30:
    print('tabrik')
#ch biozorgtar bod ch nabood
#ch shart sahih bod ch sahih nashod
#mire edameye codo mizne




a=40
if a>30:
    print('tabrik')

b=60
print(b)
    
    

a=20
if a>30:
    print('tabrik')

b=60
print(b)
    

#ch shart anjam bshe ch nashe
#python edameye code ro run mikone

#hala agar shart sahih bood --> dastore akheli 



#logic mantegh
if True:
    print('tabrik')


a=40
print(a>30)



if a>30:
    print('tabrik')

#logic -->mantegh





#-----------------

if e>30:
    print('tabrik')
#NameError: name 'e' is not defined
#* dakhele shart ro tarif krde bashi



#=====================
#tarhe masale: az taraf (karbar sen begire)
#bege agar senesh bishtar az 18 ghast behesh bege
#shoam senet ghanonie 


#agar ... inakro kon
#structure if estefade mikonm

a=int(input('sene shoam cheghadre:'))
if a>18:
    print('sene shoma ghanoonist')

#-----agha
'''
mikham begam -->
agar in shart bood inkaro kon
agar nabood oonkaro 



#too ghabli migoft
age shart sahih bod kare 1 ro bokon
agar nabod velkesh kon

ye dorahi
agar in shart sahih bood kare 1 bokon
agar nabood kare 2

if else



sakhtar:
    
if shart:
    dastoor1
else:
    dastoore2


'''
#sorat masale
#agar senesh balaye 18 bood bgo ghanonie
#g nabood ghanoni nist

a=int(input('sene shoam cheghadre:'))
if a>18:
    print('sene shoma ghanoonist')
else:
    print('sene shoma ghanooni nist')


#dota nokte-------
#yadeet bashe mitooni chnata shart bzari too codet
#mikhay bgi ag beyne 18 ta 30 bood
#ag 30 ta 50 bood
#......
#4 ta shart mikhjay bzari

a=int(input('sene shoam cheghadre:'))


if a>30:
    print('shoma baleghi')


if a>20:
    print('javani')
    
    
if a<18:
    print('shoma ghanoni nisti')


#yek moshjkeli -->
#yek sharte shoam chanbar dastor ejra bshe
#if else

#fardi k 50 saleshe
#in set asharte jodast
#@baiz vaghta karbord dare bazi vahta nadare

#ag taraf 
#range --> if else haye donabel dare

if a>30:
    print('shoma baleghi')
else if 



a=40

if 50>a>30:
    print('shoma')



#========
#nokteye akhar
a=40

if a>20:
    print('shoma balaye 20')
    print('shoma ghanoni hastiu')
    b=a+10
    print(b)
    print('tabrik')

#ta zamani k dar badaneye if hasti
#mitoni dastoor bdi

#56,7 , 1 ,.. dastoro mitoni bdi 
#ta zamani k dakhelsh hasti

if a>20:
    print('shoma balaye 20')
    print('shoma ghanoni hastiu')
    b=a+10
    print(b)
    
    
print('tabrik')







'''

=================================================
=================================================
=================================================
=================================================
====================QUIZZZZZZ====================
=================================================
=================================================
=================================================
=================================================

'''



'''
ai.2024.pilehvar@gmail.com

subject :  Q_L4_FNAME_LNAME
Q_L4_AMIR_AKBARI


--dar yekfile python 

'''

#----quiz1

#list--> a==['user1','user2','user3']
#esme jadid az karbar begirim
#b tahe list ezafe kone
#va namayesh bedahatesh


#-----quiz2
#ye mashin hesab besazim 



#az karbar adade aval begire
#adade dovom
#bad bege  che amalgari ro mikhay fingilish(jam ,tafrigh)
#** 3 ta input dare
#hesab kone va namayesh bde


#-----FUN------(veryyy optional)
'''
yek barname e benevisid ke betone tashkhis bede adad zoje ya fard
'''


#pishrafte-------
'''
yek barname benevisid ke email address begire az karbar
va tebghe email rule haye maroof bebine ke aya email
vgaghe eie ya alaki ( validation)
'''

'''
ai.2024.pilehvar@gmail.com

subject :  Q_L4_FNAME_LNAME
Q_L4_AMIR_AKBARI


--dar yekfile python 

'''



