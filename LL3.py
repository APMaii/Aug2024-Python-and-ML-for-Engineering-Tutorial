"""
In the name of god
Created on Sun Aug 11 17:48:40 2024

@author: apm

L3


hadaf--> dastoor bedam be machine
python-->yek zbaan mabeyn (intermediate) ensan (english) av machien ( binary 0,1)

khodemon pythono yad bgriim --> dore
machien pythoin ro yad bgire -->anaconda

yer safe chatbeynemon niaz darim --> IDE --> mesle spyder

code minevisim dakhele ide (spyder)

vaghty minevisi -->hich etefaghi nmiofte --> ta zamani ke
run ro bzni ( send to telegram)

vaghty run ro mizani--> python (machinemon) shabihe ensan
ke ketabe english mikhone 

*** az bala b paeen
az chap be rast

age be # ya ''' ''' ignore --> consider nmigire
dar nazar nemigire
--> comment point nokte 

mesle har zabani -->
vocab(kaalame) ----> built in function ( narenji)
dastoorat --> grammar --> banafsh

baghie chizaro--> be onavne esme zarf midone

"""

#ASSIGN -->meghdar dehi --> dakhele zarf
#********* ZARF -->?  Variable (moteghayer)


#aval esm mizarim
#yeseri ghanon dasht

#mohtaviate zarf chie?
#1-numbers ( int, float, complex)
sen=17
vazn=60.6
bordar=3j



#2-boolean
#sahih ghalat
#true false
True
False
#b onvane mohtaviate zarf berizi dakheel yek zarf
tasmim1 = 'sahih'
#ya
tasmim2 = True

tasmim3= 'True'

#mohtaviate zxarfe 2 va 3 yeksane? -->kheyr

#3-horof, kalame, jomle--> reshte --> str
esm='ali'

# ali barabarnist ba 'ali'
#avalie esme zarfg dar nazar migire
#dovomie yek reshte
ali = 20

print(ali)
print('ali')


#flashback-->harmoghe to biayt paeen chizi taghir bdi
#run bshe taghir mikone

a=20
b=30


a=13

print(a) #13


#-------
a=20
b=30

a=13
print(a) #20


#review ta alan faghat rajebe kalamate sefid--> esme variable
#baghie 1-python built in function ( tabe haye dkaheli python)
#2-dastoorat ( if , for , while , function ,.....)


#------1---------
#--------Tabe haye dakheli ---> Built in function -->narenji
#mohemtarinaashon

#ina dg mese gha;lia zarf niustan
#vaghty sedashon mikonim yekseri vazayef szakhire shode tooye python
#va miad barat anjham mide

#tabe haye dakhelie python
#python yekseri tabeye dkaheli dare

#tabe--> yekseri chizi migirer yechizi mide

#Print function--->namayesh
#40 khat neveshti vasatehs mikhay bbini felan zarf
#toosh chie
#ya ye  mohasebe mikoni mikhay bbini oon mohasebat chan mishe

#yek rah ine ke save koni =->mire smate rast bala
#yek mogeh haee kh ziadan variables ha va mikhay
#Mostaghm namayeshesh bede
#rahe hal-->estefade az built in function print

print()

#function --> dota paranytez
print #error Out[21]: <function print(*args, sep=' ', end='\n', file=None, flush=False)>


#zarfi k mikhay bbini ro bnvisi
print(sen)

print(vazn)

#agar tarif nakarde bashim chtor
print(ghad)
#NameError: name 'ghad' is not defined
#ya vaghean hamchin chizi shoma tarif nkrdi
#ya eshtebahe typiu krdi 
#runesh nkrdi
moadel=18.5

print(moadel)
#zamanie k run nkrdm
#NameError: name 'moadel' is not defined

#zamani k runkrdm
#18.5


#joda az esme zarf biari mitoni khodet mostaghim chizi tosh bnvisi
print(20)

print(2378632876387)

#str ham
print('salam')


#--hala agare bekhaym chanta bzarim chtor
#chanta zarf , chanta neveshte

# az virgool ,   ya az +
#agar az + estefade koni bayad tamame ajzaee k seda mizani
#ham type bashan ya ahamshon number 

#asma zamani k az virgool estefade mikoni in limitation ( mahdsodiatr ) ro nadari


print( 'salam' + ' khosh oomadid')
print('salam',' khosh oomadid')


print('salam man maodelam ' + 20 + 'hast') #ghalat (bayad ham type bashe)
print('salam man maodelam ' , 20 , 'hast') #no limitation


#mitoni onjm vasat zarf ham biari
esm='ali'
field='NANO'
print('salam man ', esm, 'hastam va be fielde ',field,'alaghe daram')

print('salam man  ali hastam va be fielde  NANO alaghe daram')


a='salam man  ali hastam va be fielde  NANO alaghe daram'
print(a)


#yek nokte
a=20 #@ino adad dar n
b='20'

print(a)
print(b)

c=a+2
print(c)

c=b+2
print(c)

#flash abck -->amalgar-->baraye mohasebate
#=
#+
#-
#* zrb
#/ taghsim
#** tavan 

#amalgarhaye moghase ee
#==
#=!
#>
#<
#>=
#<=


#is is
#and or








#doroste joftehson ro 20 namayesh mide
#ama avali ro adad dar nazar migire mitoni mohasebatbahash koni
#ama dovomi ro b chesmhme reshte mibine yani tarkibi az
#kalamate va horoofate mojdo dar keywprd-->nemitoni mohasebat


print('salam','khoobi') #be soorate default fasele mindaze beyne dota , 3 ,...

print('salam','khoobi',sep='*') #daste toam abze mitoni bgi
#berjay efasele setare bndaz


print('salam','khoobi',sep='7')



#-----
print('salam')
print('khoobi')
#salam
#khoobi

#too defaulte tabe neveshte khte aval ejra shod yek 
#enter bzn bad kahate badi

print('salam',end='*')
print('khoobi')
#salam*khoobi



#nokte-->< tabe haye dakheli koli dastressi bht midan
#koli mazaya ama ma darim sade tarin halatesho felan yad midim

type()
len()

#1- rangi shodan-->tabe dakhelian
#ychizi bayad bhsh bdim ychizi bde -->parantez

#tabe ye type-->bneeht mige toye zarf az chi tashkil shode
esm='ali'
#b goosheye samte rast negah kon
#$har setaro mitoni dashtebashi
type(esm) #Out[49]: str
len(esm) #3
print(esm)

#casting -->taghir 
#bala eshare krdim 

a=20

type(a) #Out[53]: int

#mikham taghirsh bdm str konam
#y str -->adad
#adad--> sahihe (int)->float (ashari)
#asharie mikham
#b in tabdilk ha migan --> CASTING
#$yekseri tabe dakheli ham baraye hamin kar sakhte shode
int()
float()
complex()
str()
bool()



#taghiresh bdi k chi ?
#mikhay brizi too y zarfe dg
a=20
type(a)

b=str(a)
 
print(a) #20
print(b) #20



type(b) #Out[58]: str




#---- int float

a=20.5
type(a)

#mikham sahih --> float -->int (casting)
b= int(a)

# a o int kon beriz too b 
print(b) #20
type(b) #Out[62]: int


#barax-0--> int--float

a=20
type(a)

b=float(a)
print(b) #20.0
type(b) #Out[66]: float


#----vorodi az karbar mnigire
input()



#sade tarin
#bebin to shayd bekhay yeja ba doostet bazi koni
#too console barat ychi minvsie va az karbar adad 
#hroof , kaloame mitone begire


#ya shayadam yek code bashe


# hadaf-->az karbar begire
#yeja bayad zakhire kone

#hamishe input ro joloye yek zarfg (variable)
#baqaraxe ghabglia

#mikhay sene karbar

input()
#dastoresh

#too delesh harchi benevisi ro baraye karbar neshon mide

input('salam senetoon ro vared namaeed')


#hrchi dakhele parantez benevisi too console miare
#jolosh bayad karbar eychizi benevise
#va ooni k karbar minevise ro migire

#mirizish too ye zarf pas poshte input niaz b y zarf dari

sen_karbar = input('salam senetoon ro vared namaeed: ')

print(sen_karbar) #30



esm_karbar= input('salam esmetoon chist: ')
print(esm_karbar) #Ali


#nokte---> dar taamme halat ha--> tabeye input 
#Khorojish ro b soorate str mide -->havaseto jam kon


sen_karbar = input('salam senetoon ro vared namaeed: ')

print(sen_karbar)

#flash abckj-->farghe a=20 va b='20'
#shoam nmitavanid az amalgarhaye riazi baraye
#mohasebat estefade konid agr adadceton bsorate str 
#zakhire bashad


#hadaf-->y barname sene karabr ro begri taghsim bar 10
#namayesh bde

sen_karbar=30

jadid=sen_karbar/10
#sen_karbar/10 = jadid ghalateeeee ava
#****aval zarf ro bayad besazi

#a+b=c ghalat#
#c = a+b



print(jadid) #3.0


#-------
sen_karbar = input('salam senetoon ro vared namaeed: ')

jadid=sen_karbar/10

print(jadid)


#TypeError: unsupported operand type(s) for /: 'str' and 'int'

#vaghtyt adade 30 ro gozashtam
#input motasefane hame chi rto b soorate str zakhire

type(sen_karbar) #Out[80]: str


#-------
#str --> int    reshte -->adad   casting
sen_karbar = input('salam senetoon ro vared namaeed: ')

type(sen_karbar) #Out[82]: str

sen_karbar2=int(sen_karbar)
type(sen_karbar2) #Out[84]: int

jadid=sen_karbar2/10

print(jadid) #3.0



#kolesho
sen_karbar=int(input('salam senetoon ro vared namaeed: '))
jadid=sen_karbar/10
print('adade jaddoei ma hast: ' , jadid) 




#-------------
#********************************
#shebhe code
#1- vorooodi (1.1. assign (zarf variable)
                #1.2. input (az karbar begiri)
                #1.3. import koni az jaee 
                #1.4. open() az file))

#2-mohasebat
            #maalgarha
            #if for (dastoorat)
            #hooshe masnooe

#3-khoorji
            #zakhriash koni to y zarf 
            #zarfe ro save koni too my computer
            #zarfe ro namayesh bdi (print)

    
#mesal-->az karbar y adad begir va taghsim bar 10

#`1-vorodi
sen_karbar=int(input('salam senetoon ro vared namaeed: '))
#2-mohasebat
jadid=sen_karbar/10
#3-khoroji
print('adade jaddoei ma hast: ' , jadid)     


#-----------------------------
#1-NUMBERS ( INT, FLOAT, COMPLEX)
#basic note:
a=20
b=30

'''
vaghty kalame sefid-->esme zarfmidone
ag vojod nadashte bashi misaze va joloye mosavi ro
mirize dakheel zarf

ag vojod dashte bashe khalish mikone va .....

shoma ag bekhayn amalgarha ro estefade konid

a ro mikhay ba b jam koni nmitoni bnvisi
a+ b = c
chon aval bayad zarfe c ro bsazi
'''
c=a+b

c=a*b

c=a**b


#-------------
#2-STR------ string reshte
#mohemtrin nokte--> ' ' dakhelesh horof, kalame, jomle

#ali  'ali' frgh dare --.esme zarfe yekodom  reshtas
# 20  '20'   yekodom adade yekodom stre 20  (amalaiate riazi nmitoni rooye str anjam bdi)

#deep
#2.1.-----> Assign (meghdardehi)
esm='Ali'
field='NANo'
#input o ... --> 
#hadaf-->yek zarf vbsazi str berizi dakhelesh

#2.2. type
type(esm) #Out[97]: str

print(type(esm)) #<class 'str'>

#2.3. andaze va size oon zarf
len(esm) #Out[101]: 3

esm='ali '
len(esm) #Out[103]: 4 #space ham dar nazar migire

name='alipilehvarmeibody'
len(name) #Out[104]: 18

print('esme shoma az ',len(name), 'horoof tashkil shode')
#esme shoma az  18 horoof tashkil shode


#2.4. access -->dastresssi
#manmikham tooye oon reshte b felan adadesjh 
#dasstresi dashte basham
name='alipilehvarmeibody'

#18 ta horof dare

#Mikham masalan b 5 omish dastresi peyda konam?
#namayeshesh bdi ya mikhay to y zarf brizi
#ya mikhay taghiresh bdi

#hadaf-->access

#az beraket estefade mikoni []
#chandomin? --> INDEX
#*****
#nokteye aval-->  index ha az 0 shoro mishe


#b a too alipilehvar nmigan harfe aval migan indexe 0
#l -->nemigan harfe dovom migan indexe 1

#esme zarf minvisi + [] too beraket indexe morede nazaro
name='alipilehvarmeibody'


name[0] #Out[106]: 'a'

#shishomin horof---< panjomin index 
name[5] #Out[107]: 'l'

#mitoni printesh koni
print(name[5]) #l

#brizish too y zarfe

panjomin_index=name[5]

#bn chanta harf dsastresi peyda konjid bayad hamon ebraket
#az indexe 2 ta indexe 4  (ipi)
#structure --> esmezarf [ start : payan + 1]
name[2:5] #--> indexe 2,3,4 bht mide
#'ipi'

name[2:4] #indexe 2 ta 4 --:> indexe 2 , 3 
#'ip'


#bekhay bgi az aval ta indexe 10
name[0:11] #Out[113]: 'alipilehvar'
#alternative -->jaygozin rahat sazi
name[:11] #Out[114]: 'alipilehvar'


#mikhay az uindexe 4 ta akahr
len(name) #Out[115]: 18 yani indexas az 0 ta 17 
name[4:18] #Out[116]: 'ilehvarmeibody'
#sade
name[4:] #Out[117]: 'ilehvarmeibody'

#agar poshte do noghte : chizi nazariyani az 0 
#agar bad az : chzii nzri yani ta tah


#2.5. str function v(tabe--> kara baramon anjam)
#*** flash abck-=->built in function -->narenji mishe va 
#vase khdoe pythone mitoni vase adad ha , str ha , bool ha va hamechi
#etseade koni

#khode str yekseri function dare k rangi nemishe (*1)
#(*2) fght baraye str ha hast
#(*3)-->enevehstane fgrh dre

print()

#rooye zarf noghte bzni
a.print() #structure



#mnesal
a='salam'
type(a)
len(a)

#upper
#kafie aval esme zarf ro bnvism bad ye noghte bad tabe ro roosh bznm
a.upper() #Out[121]: 'SALAM'

b=a.upper()
print(b)
#SALAM


a='SALAM'
b=a.lower()
print(b) #salam

#aksare mavaghe zakhrash mikoni too y avriable e dg
#$ama man bkhatere tadris 
#zakhir enmikonm ta sari too consle namayesh dade bshe

a='salam khosh amadid'
a.upper() #Out[128]: 'SALAM KHOSH AMADID'


#d ro bshmaram

a.count('d') #Out[129]: 2
a.count('h') #Out[130]: 2

b=a.split(' ')

a='salam, khosh amadid'
b=a.split(',')


a='salam'
#s--> K
a.replace('s','k') #Out[136]: 'kalam'

a.replace('a','b') #Out[137]: 'sblbm'


a.find('l') #Out[138]: 2

#inae k is dare behet true false mide


a='salam'
#alephba tashkil shdoe ya na

a.isalpha() #Out[139]: True


a='salam3442234'
#alephba tashkil shdoe ya na

a.isalpha() #Out[140]: False



sen='232786'
sen.isdigit() #Out[143]: True
 
sen='232786ui'
sen.isdigit() #Out[144]: False


esm='ali'
esm.islower() #Out[145]: True

esm='Ali'
esm.islower() #Out[146]: False




'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''







#quiz L3.1
text='hello, dear students, please interact with other studentd for improving your skills in programming and please note that this is really important and vital part of your life in the new life of programming'
#این متنمون هست , کار اول : کل متن رو تبدیل به حروف بزرگ کنید
#کار دوم این هست که ببینید چند تا حرف a داخل این متن هست
#و کار آخر این هست که کل کلمات متن را جدا کنید



#quiz l3.2
#یک برنامه بنویسید که از کاربر یک عدد بگیرد 
#و عدد رو تقسیم بر ده کند + ۸ کنه 
#، نمایش بده بگه عدد محاسبه شده ی شما فلان هست





#پیشرفت-----------------------------
#یک عدد سه رقمی از کاربر بگیرید و برعکسش را نمایش بدهید


#فان------------------------------------
#از کاربر یک پسورد بگیرید و ستاره چاپ شود
#سختی موضوع: تعداد ستاره به اندازه ی تعداد پسورد باشه





'''
subject:
Q_L3_FNAME_LNAME


ai.2024.pilehvar@gmail.com

'''





