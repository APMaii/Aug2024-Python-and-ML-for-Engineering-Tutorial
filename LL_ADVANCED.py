
"""
Created on Sun Sep 15 18:10:29 2024

@author: Ali Pilehvar Meibody

L12--->project2
ADVANCED----------------
L13

"""
#built in function
print()
input()
#........
enumerate()	

a=['ali','vahid','reza']
#b done donaashon dastresi 
#save , data , mohasebat done done elemnt anjam
#index ha ham dastresi 
for i in a:
    print(i)
    #ali , valhid , reza
    
'''
0 ali
1 vahid
2 reza

enumerate(a)

'''
#yekseri tabe ha do ta chiz bht pas midan

def dotaee(a):
    b=a+10
    c=a+20
    return b,c

zarf=dotaee(10) #touple
print(zarf) #(20, 30)
#list, touple , set ---> elemne ro dakhele khdoehs negah dare
zarf[0] #bejay elist aksare tabe ha bshoma touple

#ham b b ham b c
zarf[0]
zarf[1]

aval,dovom=dotaee(10)
print(aval)
print(dovom)
'''
20
30

unzip --> az yehcizi k list , chanta value , joda joda bekeshi brion


'''
#enumerate(a)
#index , value too liste

a=['ali','vahid','reza']
for i in enumerate(a):
    print(i)
'''
(0, 'ali')
(1, 'vahid')
(2, 'reza')


'''

for index,value in enumerate(a):
    #hbarkari delet khas mitoni koni
    #skahtane data
    #BA TARTIB , SHOAMRE ROW
    print('shoamereye',index,' : ',value)

for index,value in enumerate(a):
    #hbarkari delet khas mitoni koni
    #skahtane data
    #BA TARTIB , SHOAMRE ROW
    print(index,value)

a=['ali','vahid','reza']


#bejay ein --->
for i in range(0,len(a)):
    print(i,a[i])
    
    
    
eval()

#tabe benevisi a bngure + 5 -->

def esm(a):
    return a+5


x=1
expression='x+5' #$tabeye eval mitone yek moadele ro bkhone va javabesho bde
result=eval(expression)
print(result)
x=2
eval(expression)


x=10
eval(expression)



#-------------
print('salam') #str
print(10)
print(10.2233)
print(1j)
print(True)

#ba + --,bayad ham tyep bashan
print('salam' + 'khobi') #salamkhobi
print('salam'+12)
#TypeError: can only concatenate str (not "int") to str



#chanta bzari ba comma , 
print('salam', 12)



sen=40
#mikham ebnevsisma sen shoma ahs 40 sal
print('salam , sene shoam hast ', sen)


#se charat adado dkahele yek str 
ghad=180
print('salam , sene shoam hast ', sen,'va ghade shoma ',ghad,'hast')

#f
#bejaye inke ''  f'' dakhele f mitonm variable bzaram {}

print(f'salam , sene shoma hast {sen} va ghade shom {ghad} hast')
#salam , sene shoma hast 40 va ghade shom 180 hast


#format

print('salam sene shoma {} has va ghade shoma {} hast'.format(sen,ghad))



#-----zip() ciombgine
a=['ali','hamid','reza']
b=[20,30,40]

#beham bechasbonm 
#numpy --> az tabe hash edstefade
#pandas --.az tabesha

#khdoe python 
combined=zip(a,b)

for aval,dovom in combined:
    print(aval,dovom)



#keywords----------------
if
else:
and
or
in
not


#---------------------
raise #yekja error ro inshekli benevisi

def sen(a):
    if a<100:
        print('salam khosh amadid')
        
    else:
        print('na sene shoma ziad ast')


sen(120)
#bv shekel error , ghermez rang 


def sen(a):
    if a<100:
        print('salam khosh amadid')
        
    else:
        raise TypeError('sene shoam kam ast')
#liste avale dore -->kalamate engliusi , tahesh error ha hast

sen(120)
#debugg 

#done done jahash raise bzari


as #Mokhafaf mikone

import numpy as np


#yek barnam eminevisi 
#ag error bde ch etefaghi miofte
#100 khat brname
#error dari ( syntax ---> , . character )else donoghtasho nzshte bash
#mantegh , for if else 
#8 erro moikhroe va kole barname vay msie
#error handling

#agar error dad agha jan ghat nakon 

#tru except


def test(a,b):
    new=[]
    for i in a :
        new.append(i+b)
        #c=a[i]+b
        
    print(new[1])
    print(2)
    #print(c)


test([10,20,30,40],10)

test(10,10)
#TypeError: 'int' object is not iterable

#toyek barname nevbisi
#shekrati google , amazomn , intel,....
#100000 tabe dare

def test(a,b):
    try:
        new=[]
        for i in a :
            new.append(i+b)
            #c=a[i]+b
            
        print(new[1])
    except:
        print('doste aziz barname nakhabid ama error daria')
    #print(c)
test(10,10)
print(2)
#ya too dele tabde
#ya biroone kole program (jaee k mikhay run koni)
#bdoen try except
def test(a,b):
    new=[]
    for i in a :
        new.append(i+b)
        #c=a[i]+b
        
    print(new[1])
    
    
def test2(a):
    print('salam')



test(10,10)
test2(10) #ddovomin tabe he k az avalin tabehe jdoa hasrt
#TypeError: 'int' object is not iterable



#ba try except


def test(a,b):
    try:
        new=[]
        for i in a :
            new.append(i+b)
            #c=a[i]+b
            
        print(new[1])
    except:
        print('doste aziz barname nakhabid ama error daria')
        
        
        
def test2(a):
    print('salam')

test(10,10)
test2(10) 
#salam


#---pishrafet tar
#fght print


def test(a,b):
    try:
        new=[]
        for i in a :
            new.append(i+b)
            #c=a[i]+b
            
        print(new[1])
    except Exception as e:
        print(f'man barename ro nakahbodam ama erroret hast : {e}')
        
    
test(10,10)


#lambda

#tabe equation ro bnvisi
#a+10


def moadele(a):
    return a+10



moadele(20) #30


#lambda


moadele=lambda a:a+10



moadele(20)

#Out[112]: 30


#quick function 

#esme tabe = lambda vorodi:returni k bayad bde


moadele=lambda a,b:a+b+10


moadele(10,20) #Out[113]: 40


def aval(a,b):
    c=a+b
    dovom(c,10)
    
def dovom(z,y):
    x=z-y



#dota tabe dari k doita kari ro anjam midan



#avalkio dovomi b ham bastegi drn shyd

#@backend (site)  telegram API fazahaye 
#message handler
#
'''
1-mahane 2-hafrtegi

2
.......
2
chize
3 




'''
def message()


def :
    
    
    
    
#tedade ziadi estefae mikonan

#tabe haye badi montazere tabe haye ghabli waysan


#poshte def benvisi async
#poshte dastoroatet await


async def aval(a,b):
    await c=a+b
    dovom(c,10)
    
async def dovom(z,y):
    await x=z-y

#tabe hato hamahang mikoni k montazere javab az tabe haye ghbli bmonan






#==========================================================
#==========================================================
#==========================================================
#==========================================================
#==========================================================
'''
-----CLASS-----------

def balad bodim
def bekar nmiad va nmitone moshekel maor hal , naize maor bartaraf bokone
classs





C---> Pishrafte hast 
C++ ---> C + Class


yekc hizi mese def -->esmehs hast class karaye bsihtari anjam mdie

class , object   --> object-oriented -->shey gera
paython yek zabane shey gera hast
[clas ro support mikone
 ]

'''

#---BANK BSAZIM

#BALANCE ((mojoodie hesab))
#variz ( variz)


def mojoodi(money):
    global m
    m=money
    print('mojodie shoma hast ',m)
    
    
mojoodi(200) 
    

def variz(b):
    new=m+b
    print('variz hsod, hala moodie shoma ast',new)
    


variz(100)
#variz hsod, hala moodie shoma ast 300

variz(200)
#zakhire konm dade hamo
#list


#mianbori nsit?



#in tabe ro fght man mitonm estefade konm ali 
#amir --> estefade kone

#yek chizi besazam applciartion
#chynd nafar botonan estefade konan

#shey --> shey bsazam object bsazammm



'''
def name(vorodi):
    body
    return khoroji

'''
#-------------------
#class--> yek cjhzii hast k havie koli adad haye sabet , tabe hast
#clas madule hast --> too dleesh mitone koli aasde sabet , tabe dashte bashe



class bank:
    #........
    
#esme class , 
#tabe ee bname bank
#nemigan tabge

#classi darim bname bank

#------- adad sabet , tabe 


#--------------
'''

class name:
    
    
class miatvanad shamele:
    adad haye sabet
    tabe ha
    
bashad





'''




class bank:
    zarf=40



#mesle tabe bank()
#rooberosh harchi bzari , yek obejct hsey


a1=bank()

#a1???
#a1-> 

type(a1)
#Out[127]: __main__.bank


#too delsh ysri chzia


a1.zarf #Out[128]: 40


#kafier shoam 
#a1 a2 b3 name esm number1 number2
#jolosh bank()

#yek shey msihan k harchi too dele classs , b ina vasl mishe


a2
#NameError: name 'a2' is not defined

a2=bank()
#a2 yek object az class bank
#too dle ebank yekseri adade sbate, tabe hast
#ina oto dele a2 ham hast



a2.zarf




class bashgah:
    ghad=180
    vazn=80
    
    
ali=bashgah()
ali.ghad#180
ali.vazn #80

#hal amitonim zharan hezar shey bsazim

vahid=bashgah()
#yek zarf msiazid dar sanie koli mohtaviati k dar cdlass bood miad dakhele in zrfe (object)

vahid.ghad
vahid.vazn

#------

#har objectet yekseri vizhegi dashte bashe
#ali , vaznp ghadi
#vahi , ye vazano gahde dg


#-----sakhtare doros class

class bashgah:
    
    def __init__(self):
        pass

#vgaghty yek shey khasti bsazi bnvis a1=bashgah()

#agar bkhay vorodi ham bgrie

#ali=bashgah(180,80)

class bashgah:
    
    def __init__(self,ghad,vazn):
        #inaro zakhire
        #yechizi has bname self
        self.ghad=ghad
        self.vazn=vazn
        
        
ali=bashgah()      
#TypeError: bashgah.__init__() missing 2 required positional arguments: 'ghad' and 'vazn'

ali=bashgah(180,80)

#@yek zarfi banme ali darim

#harjae az oocdet kafie bzni ali dot ro bzni b moshakhasatesh vasl shi

ali.ghad #180
ali.vazn#80



vahid=bashgah(160,70)
vahid.ghad #Out[145]: 160
vahid.vazn #70


#100 ta object bsazam


vahid.nesbat
#AttributeError: 'bashgah' object has no attribute 'nesbat'

#attribute , property --> megdhar sabet ha
# method ---> tabe ha


#class to delesh ya adad sabet, tabe
#class --> property , method
class bashgah:
    #in neshon mdie ch vroodi haee bayad bgire baray eobvject shoidan
    def __init__(self,a,b):

        #inja vorodi haro mirizijm too yek banke etelaati
        #trf harmoghe mizne objectesho masalan mzine ali
        #dot k mizne
        
        self.ghad=a
        self.vazn=b

ali=bashgah(180,90)


ali.ghad
ali.vazn
ali.nesbat


class bashgah:
    #in neshon mdie ch vroodi haee bayad bgire baray eobvject shoidan
    def __init__(self,a,b):

        #inja vorodi haro mirizijm too yek banke etelaati
        #trf harmoghe mizne objectesho masalan mzine ali
        #dot k mizne
        
        self.ghad=a
        self.vazn=b
        self.nesbat=a/b
        self.adade_khodam=4000
ali=bashgah(180,90)
ali.ghad
ali.vazn
ali.nesbat  #Out[157]: 2.0
ali.adade_khodam


vahid=bashgah(200,80)
vahid.ghad
vahid.vazn
vahid.nesbat
vahid.adade_khodam #baraye hame hamone

#1----class


#1.1.proeprty --->adaede sabet
#ina attribute .--> proeprty .

#1.2. methods---->tabe
#tabe method bsazim  
class bashgah:
    #in neshon mdie ch vroodi haee bayad bgire baray eobvject shoidan
    def __init__(self,a,b):

        #inja vorodi haro mirizijm too yek banke etelaati
        #trf harmoghe mizne objectesho masalan mzine ali
        #dot k mizne
        
        self.ghad=a
        self.vazn=b
        #fght dota moshakahse dashte
        #fght 2 ta proeprty dashte
        #ght 2 ta attribute dashte bashe
        
    #tabey einit -->shoro hbod yani frght mige chia begir baraye objecdt skahtan
    #va chiaro zakhrie kon
    
    def welcome(self):
        print('salam arz hsod bar moshatrie aziz ba ghade',self.ghad)
        
        
    
ali=bashgah(180,80)
        
ali.ghad
ali.vazn    
#methdo daran #ba msohakahste oon object kar mikone
ali.welcome() #paranet zyadet nre

#in tabe haa yek karei, algorithmi ro 
#rooye oon obejct piuade mikonan

vahid=bashgah(150,50)
vahid.welcome()



class bashgah:
    #in neshon mdie ch vroodi haee bayad bgire baray eobvject shoidan
    def __init__(self,a,b):

        #inja vorodi haro mirizijm too yek banke etelaati
        #trf harmoghe mizne objectesho masalan mzine ali
        #dot k mizne
        
        self.ghad=a
        self.vazn=b
        #fght dota moshakahse dashte
        #fght 2 ta proeprty dashte
        #ght 2 ta attribute dashte bashe
        
    #tabey einit -->shoro hbod yani frght mige chia begir baraye objecdt skahtan
    #va chiaro zakhrie kon
    #---npkteye kh fariiiii
    def welcome(abc):
        print('salam arz hsod bar moshatrie aziz ba ghade',abc.ghad)
        
        
        
    
    

#----------------------------
#ykeseri kara nmishe ba tabe najam dad
#vaghty mikhay integrated (peyvaste)
#obejct
#mavade shimaie, narm afzar windows haye motefavet
#bank , abshgah -->moshtari haye motefavet



#banabarin bayad clas bsazi
#vaghty kahsti class bsazi
#ch chiz haee az oon obejct mikhay? -->init bsazz
#harchi kahsi save bashe az trfe khdoet sabet baraye hame self.
#method ham ta delet khast ezafe kon


class bank:
    def __init__(self,name,idd,age):
        #in vorodi haro , name codea_meli , age
        #brize tooye self
        #self ->ghafase , 
        
        self.esm=name #valin vorid dar esm briz
        self.code_meli=idd #dovomin ro dar code_meli
        self.sen=age
    #proeprtyas-->msohakajhste
    
    #methhod
    #chra dar self chzii mirizim?
    #choon ddar method ha behsh niaz darim
    #va fgth bayad self ro seda konim
    #ba dot b oon ghafase brsim va oon value ro biarim biron
    
    def welcome(self):
        print('khosh amadid jenabe',self.esm)
    
ali=bank('ali',440,30)
ali.name #XXXX CHIZAEE K GAHFASE BANDI KRID FGHT
ali.esm
ali.code_meli
ali.sen

ali.welcome()
#khosh amadid jenabe ali


#migi age khanom bodo?
class bank:
    def __init__(self,name,idd,age,gender):
        #in vorodi haro , name codea_meli , age
        #brize tooye self
        #self ->ghafase , 
        
        self.esm=name #valin vorid dar esm briz
        self.code_meli=idd #dovomin ro dar code_meli
        self.sen=age
        self.jensiat=gender
    #proeprtyas-->msohakajhste
    
    #methhod
    #chra dar self chzii mirizim?
    #choon ddar method ha behsh niaz darim
    #va fgth bayad self ro seda konim
    #ba dot b oon ghafase brsim va oon value ro biarim biron
    
    def welcome(self):
        if self.jensiat=='mard':
           print('khosh amadid aghaye',self.esm)
        if self.jensiat=='zan':
            print('khosh amadid khanoome mohtarame',self.esm)

ali=bank('ali',440,30,'mard')
ali.welcome()
#khosh amadid aghaye ali


zahra=bank('zahra',456,25,'zan')
zahra.welcome()
#khosh amadid khanoome mohtarame zahra
class bank:
    def __init__(self,name,idd,age,gender):
        #in vorodi haro , name codea_meli , age
        #brize tooye self
        #self ->ghafase , 
        
        self.esm=name #valin vorid dar esm briz
        self.code_meli=idd #dovomin ro dar code_meli
        self.sen=age
        self.jensiat=gender
        self.mojoodi_avalie=0
    #proeprtyas-->msohakajhste
    
    #methhod
    #chra dar self chzii mirizim?
    #choon ddar method ha behsh niaz darim
    #va fgth bayad self ro seda konim
    #ba dot b oon ghafase brsim va oon value ro biarim biron
    
    def welcome(self):
        if self.jensiat=='mard':
           print('khosh amadid aghaye',self.esm)
        if self.jensiat=='zan':
            print('khosh amadid khanoome mohtarame',self.esm)

        #mojodi ha
    def balance(self):
        print('total balance:',self.mojoodi_avalie)
    
    
#esme zarfetam bzari ali

b=bank('ali',440,30,'mard')
b.sen
b.esm
b.welcome()
b.balance() #mojodim #total balance: 0

#---------varizo...

class bank:
    def __init__(self,name,idd,age,gender):
        #in vorodi haro , name codea_meli , age
        #brize tooye self
        #self ->ghafase , 
        
        self.esm=name #valin vorid dar esm briz
        self.code_meli=idd #dovomin ro dar code_meli
        self.sen=age
        self.jensiat=gender
        self.mojoodi=0
    #proeprtyas-->msohakajhste
    
    #methhod
    #chra dar self chzii mirizim?
    #choon ddar method ha behsh niaz darim
    #va fgth bayad self ro seda konim
    #ba dot b oon ghafase brsim va oon value ro biarim biron
    
    def welcome(self):
        if self.jensiat=='mard':
           print('khosh amadid aghaye',self.esm)
        if self.jensiat=='zan':
            print('khosh amadid khanoome mohtarame',self.esm)

        #mojodi ha
    def balance(self):
        print('total balance:',self.mojoodi)
    
    #variz
    #vaghty sedash bzne
    #b.deposit( intoo bnvise  )
#vghty khas azin atbe(method) estefade kone niaZ dre eyk vorodi bde

    def deposit(self,amount):
        self.mojoodi = self.mojoodi + amount
        print('success')
        print('your total balance is,',self.mojoodi)
        
#esme zarfetam bzari ali

b=bank('ali',440,30,'mard')
b.sen
b.esm
b.welcome()
b.balance() #mojodim #total balance: 0
#total balance: 0

b.deposit(200)
#success
#your total balance is, 200


b.balance()
#total balance: 200





b.deposit(100)
b.balance() #total balance: 300


class bank:
    def __init__(self,name,idd,age,gender):
        #in vorodi haro , name codea_meli , age
        #brize tooye self
        #self ->ghafase , 
        
        self.esm=name #valin vorid dar esm briz
        self.code_meli=idd #dovomin ro dar code_meli
        self.sen=age
        self.jensiat=gender
        self.mojoodi=0
    #proeprtyas-->msohakajhste
    
    #methhod
    #chra dar self chzii mirizim?
    #choon ddar method ha behsh niaz darim
    #va fgth bayad self ro seda konim
    #ba dot b oon ghafase brsim va oon value ro biarim biron
    
    def welcome(self):
        if self.jensiat=='mard':
           print('khosh amadid aghaye',self.esm)
        if self.jensiat=='zan':
            print('khosh amadid khanoome mohtarame',self.esm)

        #mojodi ha
    def balance(self):
        print('total balance:',self.mojoodi)
    
    #variz
    #vaghty sedash bzne
    #b.deposit( intoo bnvise  )
#vghty khas azin atbe(method) estefade kone niaZ dre eyk vorodi bde

    def deposit(self,amount):
        self.mojoodi = self.mojoodi + amount
        print('success')
        print('your total balance is,',self.mojoodi)
        
        #b.ATM( megdhare ppoli)
    def ATM(self,getting):
        self.mojoodi =self.mojoodi-getting
        print('success' )
        print('yo total balance is',self.mojoodi)
        
        
b=bank('ali',440,30,'mard')
#ba ali aba yek obejcti b 

#ba obejct haee mesle c d e .....

 
b.balance()

b.deposit(100)

b.balance()


b.ATM(50)

b.balance()



#---pishrtaftash koniudddd
b.balance()
#total balance: 50

b.ATM(200)
#yo total balance is -150

class bank:
    def __init__(self,name,idd,age,gender):
        #in vorodi haro , name codea_meli , age
        #brize tooye self
        #self ->ghafase , 
        
        self.esm=name #valin vorid dar esm briz
        self.code_meli=idd #dovomin ro dar code_meli
        self.sen=age
        self.jensiat=gender
        self.mojoodi=0
    #proeprtyas-->msohakajhste
    
    #methhod
    #chra dar self chzii mirizim?
    #choon ddar method ha behsh niaz darim
    #va fgth bayad self ro seda konim
    #ba dot b oon ghafase brsim va oon value ro biarim biron
    
    def welcome(self):
        if self.jensiat=='mard':
           print('khosh amadid aghaye',self.esm)
        if self.jensiat=='zan':
            print('khosh amadid khanoome mohtarame',self.esm)

        #mojodi ha
    def balance(self):
        print('total balance:',self.mojoodi)
    
    #variz
    #vaghty sedash bzne
    #b.deposit( intoo bnvise  )
#vghty khas azin atbe(method) estefade kone niaZ dre eyk vorodi bde

    def deposit(self,amount):
        #saghf bzaram
        if amount>10000:
            print('You can not deposit more than 1000')
        else:
            self.mojoodi = self.mojoodi + amount
            print('success')
            print('your total balance is,',self.mojoodi)
        #saghf dahste basham 
        
        
        
        
        
        #b.ATM( megdhare ppoli)
    def ATM(self,getting):
        if getting>self.mojoodi:
            print('Moojodi kafi nemibashad')
        else:
        
            self.mojoodi =self.mojoodi-getting
            print('success' )
            print('yo total balance is',self.mojoodi)
        
   
        
user1=bank('ali',400,30,'mard')
user1.esm #ch propertyu haee dare too delesh dare?

user1.mojoodi
#property haye yek object


#method ha
user1.welcome()

#khosh amadid aghaye ali


user1.balance()


user1.deposit(200)

user1.balance()


user1.ATM(100)
user1.balance()


user1.deposit(2383416943229879)
#You can not deposit more than 1000

user1.balance()


user1.ATM(200)
#Moojodi kafi nemibashad


#-------
#ketabkhan eh a
#Numpy,pandasm scikit learn
#CLASSS -->too dleesh koli tabe hast



#----------
#aya mishe man yek clas bsazam
#shobe


#niaz darid yek class jadid bsazid
#ama tamame method ha va proeprty haye class ghabli ro ham hamrash dashte bashe



class bank_markazi:
    def __init__(self,name,idd,age,gender):

        self.esm=name #valin vorid dar esm briz
        self.code_meli=idd #dovomin ro dar code_meli
        self.sen=age
        self.jensiat=gender
        self.mojoodi=0
   
    
    def welcome(self):
        if self.jensiat=='mard':
           print('khosh amadid aghaye',self.esm)
        if self.jensiat=='zan':
            print('khosh amadid khanoome mohtarame',self.esm)

        #mojodi ha
    def balance(self):
        print('total balance:',self.mojoodi)


    def deposit(self,amount):
        #saghf bzaram
        if amount>10000:
            print('You can not deposit more than 1000')
        else:
            self.mojoodi = self.mojoodi + amount
            print('success')
            print('your total balance is,',self.mojoodi)
 
    def ATM(self,getting):
        if getting>self.mojoodi:
            print('Moojodi kafi nemibashad')
        else:
        
            self.mojoodi =self.mojoodi-getting
            print('success' )
            print('yo total balance is',self.mojoodi)
    




#bank_meli

#hamon chziaro dashste bashe

#verasat ---> verasatesho

#1---ravehse

class bank_melat(bank)
#clase ajdi ( class ghabli)
#class jadide --> tamame property,emthdo haye clas ghablei ro b versat bbre , hamasho dahste bashe

#raveshe aval
class bank_melat(bank_markazi):
    def __init__(self,name,idd,age,gender):
        bank.__init__(self,name,idd,age,gender)
        
        
        
        
class bank_melat(bank_markazi):
    def __init__(self,name,idd,age,gender):
        super().__init__(name,idd,age,gender)



a=bank_melat('ali',440,20,'mard')

a.esm
a.welcome()

#tamame tabe haye ghabli ro miarew


#tabe ezafe konm bhsh

class bank_melat(bank_markazi):
    def __init__(self,name,idd,age,gender):
        super().__init__(name,idd,age,gender)

    def jadid(self):
        print('salam')

a=bank_melat('ali',440,20,'mard')

a.esm
a.welcome()
a.jadid()





#-------APPENDIX------------


Function	Description
abs()	    Returns the absolute value of a number
all()	    Returns True if all items in an iterable object are true
any()	    Returns True if any item in an iterable object is true
bin()	    Returns the binary version of a number
bool()	    Returns the boolean value of the specified object
bytes()	    Returns a bytes object
complex()	Returns a complex number
dict()	    Returns a dictionary (Array)
float()	    Returns a floating point number
input()	    Allowing user input
int()	    Returns an integer number
len()	    Returns the length of an object
list()	    Returns a list
max()	    Returns the largest item in an iterable
min()	    Returns the smallest item in an iterable
next()	    Returns the next item in an iterable
object()	Returns a new object
open()	    Opens a file and returns a file object
pow()	    Returns the value of x to the power of y
print()	    Prints to the standard output device
range()	    Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
reversed()	Returns a reversed iterator
round()	    Rounds a numbers
set()	    Returns a new set object
sorted()	Returns a sorted list
str()	    Returns a string object
sum()	    Sums the items of an iterator
tuple()	    Returns a tuple
type()	    Returns the type of an object








ascii()	        Returns a readable version of an object. Replaces none-ascii characters with escape character
bytearray()	    Returns an array of bytes
callable()	    Returns True if the specified object is callable, otherwise False
chr()	        Returns a character from the specified Unicode code.
classmethod()	Converts a method into a class method
compile()    	Returns the specified source as an object, ready to be executed
complex()	    Returns a complex number
delattr()	    Deletes the specified attribute (property or method) from the specified object
dir()	        Returns a list of the specified object's properties and methods
divmod()	    Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()	    Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()	        Evaluates and executes an expression
exec()	        Executes the specified code (or object)
filter()	    Use a filter function to exclude items in an iterable object
format()	    Formats a specified value
frozenset()	    Returns a frozenset object
getattr()	    Returns the value of the specified attribute (property or method)
globals()	    Returns the current global symbol table as a dictionary
hasattr()	    Returns True if the specified object has the specified attribute (property/method)
hash()	        Returns the hash value of a specified object
help()	        Executes the built-in help system
hex()	        Converts a number into a hexadecimal value
id()         	Returns the id of an object
isinstance()	Returns True if a specified object is an instance of a specified object
issubclass()	Returns True if a specified class is a subclass of a specified object
iter()	        Returns an iterator object
locals()	    Returns an updated dictionary of the current local symbol table
map()	        Returns the specified iterator with the specified function applied to each item
memoryview()	Returns a memory view object
oct()	        Converts a number into an octal
ord()	        Convert an integer representing the Unicode of the specified character
property()	    Gets, sets, deletes a property
repr()	        Returns a readable version of an object
setattr()	    Sets an attribute (property/method) of an object
slice()	        Returns a slice object
staticmethod()	Converts a method into a static method
super()	        Returns an object that represents the parent class
vars()	        Returns the __dict__ property of an object
zip()	        Returns an iterator, from two or more iterators







'''
Keywords:
Keyword 	Description
'''

True    	Boolean value, result of comparison operations
False	    Boolean value, result of comparison operations
is	        To test if two variables are equal
in      	To check if a value is present in a list, tuple, etc.
not     	A logical operator
or      	A logical operator
and	        A logical operator
None    	Represents a null value
del     	To delete an object
if      	To make a conditional statement
else        Used in conditional statements
elif	    Used in conditional statements, same as else if
pass	    A null statement, a statement that will do nothing
continue	To continue to the next iteration of a loop
break	    To break out of a loop
for	        To create a for loop
while	    To create a while loop
def	        To define a function
global	    To declare a global variable
return	    To exit a function and return a value
raise	    To raise an exception
lambda	    To create an anonymous function
class	    To define a class
import	    To import a module
from	    To import specific parts of a module
try	        To make a try...except statement
except	    Used with exceptions, what to do when an exception occurs
finally	    Used with exceptions, a block of code that will be executed no matter if there is an exception or not


as	        To create an alias
assert	    For debugging
nonlocal	To declare a non-local variable
with	    Used to simplify exception handling
yield	    To return a list of values from a generator








