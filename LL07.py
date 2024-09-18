
"""
In The Name of God
Created on Sun Aug 25 18:06:24 2024

@author: Ali Pielhvar Meibody


L7

RECAP:
review 5min
function 
terminal , ... 
ketabkhone ha
A1 (PROOZHE 20%) -->tabe tamom
A2 (30%) --> ketabkjhane ha
A3 (50%) -->entehaye dore

faghato faghat in 3 porozhe jebari hastand
quiz ha ,..-->ekhtiari (tasir daran)




Review:
    python yek zabane
    harchi minevisi yeseriash reserve (rangi)
    sefide-->zarf (variable)
    
    reserved :
        1-built in function (print(),input(),len())
        2-keywords (dastoorat) (if , if else, for , while , def, class , ..)
        
    variable(zarf):
        assign esm_zarf = 
        bool True False
        int , float , complex (numbers)
        str --> a s 3 ali salam arz shod
        str.function()  a='salam'  b=a.upper()
        
        list --> mitoni koli
        list.function()  a1.append()  -->apply
        
    Structure barname: quiz, man :psudocode (shebhe code)
    1-voorodi 
        assign (a=2,b=3) , input() , open() 
    2-mohasebat --> + - , ....if , for , while , ... AI
    3-khoroji --> save too variable (c) ,save to desktop,uploade website, print() ,khoroji
"""


#--yek barnameye mohasebati nano etchnology

'''
120 khat

'''
#ghanone newton  niroo = shetab * jerm

#Helium
acc=10 #shetab
mass=5 #jerm

#sabet
boltzman=22768172
force=acc*mass
U=force*10**boltzman
C= force*223834
Final=U+C

'''
az final

b=c+final
'''

#dobare b ye zareye dg miresam
#Hydrogen
#mass #acc

#--dobare batyad bnvisam
acc=8 #shetab
mass=1 #jerm

#sabet
boltzman=22768172
force=acc*mass
U=force*10**boltzman
C= force*223834
Final=U+C


#100 bar bekham estefade konam 
#hey copy paste
#hey???


#=--> ey kash yek box (jabe) bood
#behesh vorodi midadam , khoroji midad
#tasmame in mohasebato mirikhtam dakheelsh

final(8,1)


#tabe sazi


#---------Function (tabe)-----
#1-sakhtar : jabe (box)
#2- vorodii dare vamohasebe , khoroji 


#STEPS:
    #1-define --> tarifesh koni (chanta vorodi , ch mohasebasti anjham mide va ch khoroji ee mide)
    
    
    
   # hrmoghe khasti estefade kon
    #2-call -->seda bzni estefade koni
    

'''
def func_name(vorodi1)
def func_name(vorodi1,vorodi2)
def func_name(vorodi1,vorodi2,vorodi3)



def func_name(vorodi1,vorodi2,vorodi3):
    mohasebat (yek khat)
    ya chan khat
    




'''

#tarhe masale--> mikham a ro begire + b kone + 10 kone
#niaz b jabe daram -->naiz b function? --> tekrar
#if --> 'agar' 
#for -->'varresi','tekrar'
#def --> ' skahjtar vorodi khoroji 

#pas-->tasvib -->ye box mikham
#soale aval-->der mikjhaym?-->yes
#soale dovom--> vorodi hash chie? 2 ta vorodi
#soale sevom khorojish chie? --


#a, b na harchi delet khas hare eesm
#dota esme zarf bayad bzari

def jam(a,b):
    c=a+b+10
    print(c)
    
#vaghty run mikoni hichi nmide 
#bayad run koni **--> k python skahatre in tabe ro beshnase ba esmesho


#bad az run-->mifahme jam , va mdioni tooo delesh chie


#sakhtam-->define

#estefade--> (nokte nahaee) call sedaw zadan

#esme tabe ro sseda mzini
#() ***
#too parantez vorodi ha

jam(4,5)  


'''
python az bala mikhone

sefide--> na built in functione na hichi
b parantez mirese mifhme zarf (variable)-->yek tabas
aval chekc mikone in tabe vojod dare ya na (run , define) --> 
NameError: name 'tafrigh' is not defined

hala k check mikone mibine hast
mibine chanta vorodi mikhad 2 ta ok , brmirgde 2 ta ro migire azat va ejra mikone

4 o mzire a
5 o mzire b
va moahasebato anjam mide ****

'''
tafrigh(2,3)

jam(4,5)  #19


#vaghty seda zadi -->print kardd
#tabe ha -->tabeye bedoone khorojii
#print-->khoroji nist ******


#khoroji:joloyue jaee k sedash mzinim 
#khoroji -->ydchizi basrgrdone ma zakhriahs konim

f=jam(4,5)
#f ro y zarfe khali bgir
#tabe ro ejra kon 4+5+10=19
#f=19 --> 

#19 ychizi print shod


print(f)
#None



#asgar bkhay khoroji bde
#yani 
#----case1
def jam(a,b):
    c=a+b+10

f=jam(4,5) #hcihi nayovord



print(f) #None
#----case2
def jam(a,b):
    c=a+b+10
    print(c)


f=jam(4,5) #19 fght print shod ama


print(f)

##----case3
#aya dastoori vojod dare bgim mohasebe k krdi
#oon meghdaro oonjaee k call kardim abresh grdon
#baresg gardoon-->return
def jam(a,b):
    c=a+b+10
    return c
    
f=jam(4,5)  #f=19

#chizi print nkrd
print(f) #19 -->return



#--case 4
def jam(a,b):
    c=a+b+10
    print('salam')
    print(c)
    return c


f=jam(4,5)


print(f)



#---------------
#-----
#dota mesal
#1---> agha ye tabe mikham k adade 1 , adad 2
#sallam arz shod adad 1 bozorg tar az adad 2 hast


adad1=30
adad2=60


if adad1>adad2:
    print('salam adade 1 bozorgtar az adade 2 hast')
    
if adad2>adad1:
    print('salam adade 2 bozorgtar az adade 1 hast')






#in diota zarfe man gharar hey avaz she










a=342176412716498
b=138127312763127



def bozorg(a,b):
    if a>b:
        print('adade 1 bozoregtr astg1')
    if b>a:
        print('adade 2 bozorg tr ast')
        


bozorg(4,5)


a=bzoorg(4,5)

#hadafe-->fght behem etela-->print

#print --> ba khoroji frgh dre



a=342176412716498
b=138127312763127

bozorg(a,b)


#jolkosh zarf bzaram

c=bozorg(a,b)
print(c)

#khorojii-->yechizi bht pass bde harj asedash zdi bveizish too zarff

def bozorg(a,b):
    if a>b:
        print('adade 1 bozoregtr astg1')
    if b>a:
        print('adade 2 bozorg tr ast')
        

    
a-b

b-a







a=40
b=50

bozorg(a,b)


#pas miham bgirmsh badasn estefade konm
#fght nmikham k namayehs bde

def bozorg(a,b):
    if a>b:
        c=a-b
        return c
    if b>a:
        c=b-a
        return c
        



a=3287
b=321182



f=bozorg(a,b)





d=121*f
print(f)

print(d)





#nesbat b application
#fght namayehs bede ekhtelafo

#-case 1 fght namayesh -->khoroji ndre
def bozorg(a,b):
    if a>b:
        c=a-b
        print(c)
    if b>a:
        c=b-a
        print(c)
        
#case 2-->khoroji bde

def bozorg(a,b):
    if a>b:
        c=a-b
        return c
    if b>a:
        c=b-a
        return c



#ham namayehs bde ham khoroji
def bozorg(a,b):
    if a>b:
        c=a-b
        print(c)
        return c
    if b>a:
        c=b-a
        print(c)
        return c



a=3213
b=12112

f=bozorg(a,b)

print(f)



#=====================

#mikhay ye esm az karbar begiri 
#@teade a hasho beshmori

esm=input('esmeto begoo')

count=0
for i in esm:
    if i == 'a':
        count=count+1


print('dar esme shoma  ',count, 'doone a vojod darad')





#==========================
#fek kon ytek code 200 khat


#step 2-->call
#


#---tabe
#step1-->bnesazish
#step2-->call -->aya mikhay chizi namayesh bde fght (khrooji)
##vali ag bkhay sedash koni va bht chizi brgrdoine bayad ye return too dele
#tabe bezari




#=========TABE --> BOX   VORODII----> BOX --> KHOROOOJI

#yek tabe boxe vorodi dashte nadashte , khoroji dahste nabd


#--------case 1 voorodi-->box ---> 

#vorodi dare khrooji ndre 
def jam(a,b):
    c=a+b
    print(c)
    
    
jam(4,5)

#nmitonm
a=jam(4,5)



#--------case 2 voorodi-->box ---> khorooji

#vorodiii dashte bashe khodori ham 

def jam(a,b):
    c=a+b
    return c #harjae k sedash zadim 


a=jam(4,5)


#--------case 3 -->box ---> 

#---na voroodi na khoroji


def welcome():
    print('khosh amadid')


welcome()

a=welcome()


#------case 4 -->box---> khoroji

def pi():
    return 3.14


a=pi()


pi=3.14
a=pi




#------------------------------
# Vooordi---> box ----> khorooji
 
#karbord-->yek sakhtario --.sedash bzniiii

f=m*a

#mass, acxc , -->arg
def newton_law(mass,acc):
    
    force=mass*acc
    return force



b=newton_law(10,2)



#jerme 20 
c=newton_law(20,3)



d=newton_law(100,2)




#----------------

f=newton_law(100)

#TypeError: newton_law() missing 1 required positional argument: 'acc'


#agha bsoorat eby default a=9.8
#mnikham hamrogghe sedash krdm ag fght mass --> f=mass* 9.8
#ag ham khdoet khasi ham f=mass*20


#yek arg deafult
def newton_law(mass,acc=9.8):

    
    force=mass*acc
    return force


#mesle ghabl
b=newton_law(10,2)
print(b)

#fght jerm
c=newton_law(10)
print(c)


d=newton_law()


def newton_law(mass,acc=9.8):
    '''
    mass --> int
    acc --> int (optional, default:98)
    dsadsjhhgajh
    output-->force based on second law of newton
    
    '''
    
    force=mass*acc
    return force


f=newton_law()



#asg tabe e 2 vorodi dre
#-->koli-->ag kasi khast estefade kone bayad hatman 2 ta vorodi b tabe bde call

#ama ag bkhay bgi agah ag dot adad k anajm bde
#ag fght ydone dad oonyeki dg ro default 98 23 -->
def esm(vorodi1, vorodi2=23):
    
    

    
#ghjanone newton fght baraye mavade mamolie , sang , machine
#quantum_material --> az in ghanoon peyravi


#@ghabli  jerm,shetab -->box---> niroo
#box 
#jadid  jerm,shetab ,type_made--->box-->niroo


def newton_law(mass,acc,mat_type):
    
    
d=newton_law(10,2,'yes')
 
    
def newton_law(mass,acc,normal_or_not):
    
    if normal_or_not=='yes':
        force=mass*acc
        
    if normal_or_not=='no':
        force=mass*acc*0.4554
        
    return force

    
d=newton_law(10,1,'yes')

jadid_kashf=newton_law(10,1,'no')




#hala skahte agha yeki dg mikah destefade
def newton_law(mass,acc,normal_or_not):
    
    '''
    

    Parameters
    ----------
    mass : int
        جرم
    acc : int
        شتاب
    normal_or_not : str
        if your material is nromal type(yes) if not type no

    Returns
    -------
    force : int
        this force is calculated based on second law .

    '''

    if normal_or_not=='yes':
        force=mass*acc
        
    if normal_or_not=='no':
        force=mass*acc*0.4554
        
    return force



#--------
#if , for , else and ....

#-------------
#for-->halghe
break #az halghe bia biron
continue #b halghe edame bde
#barayew halghe


for i in range(0,100):
    break


#mikhay yek shasrt bzzrim
end=53
for i in range(0,100):
    print(i)
    if i==end:
        break


#tabe anjam bdi .......
#break , continue -->aaz halghe bia biron
#bekhay bgi masalan az tabe bia biroon=-->return

def new(end):
    for i in range(0,100):
        print(i)
        if i==end:
            break
    return     
        



def jam(a,b):
    c=a+b
    print('salam')
    return c

al=jam(10,5)



def jam(a,b):
    c=a+b
    return c
    print('salam')

al=jam(10,5)



def newton_law(mass,acc,normal_or_not):
    
    if normal_or_not=='yes':
        force=mass*acc
        return force
        
    if normal_or_not=='no':
        force=mass*acc*0.4554
        return force
    
    
    
def newton_law(mass,acc):
    force=mass*acc
    return force
        
    
a=20
b=30
newton_law(20,30)




def newton_law(a,b):
    force=a,b
    return force


#esme zarfe vorodi ha daste toe



def jam(a,b):
    c=a+b
    return c




new=jam(4,5)




print(a) #NameError: name 'a' is not defined
print(b) #NameError: name 'b' is not defined
print(c) #NameError: name 'c' is not defined
print(new) #9


#tamame motegahyer haee--->local 




#---zarf ha (variable)
#global
#local


a=20

def jam(a,b):
    c=a+b
    return c




new=jam(4,5)



print(a)

print(c)

#agar bekham y zarf bsaszamm too delesh k hamishe 
#biroone tabe ham beshe sedassh zad
#bejaye zrf movaghat -->zarfe daem


def jam(a,b):
    global c
    c=a+b
    return c


new=jam(4,5)
print(c)


#--------------
def newton_law(mass,acc):
    force=mass*acc
    return force




d=newton_law(10,2)


d=newton_law(mass=10,acc=2)


#----yeja shoma salah midoni-->khodet

#fght adadi bayad vared koni
def newton_law(mass,acc,/):
    force=mass*acc
    return force

d=newton_law(10,2) #d=20
d=newton_law(mass=10,acc=2) #erro




def newton_law(*,mass,acc):
    force=mass*acc
    return force

d=newton_law(mass=10,acc=2)

d=newton_law(10,2) #TypeError: newton_law() takes 0 positional arguments but 2 were given



#tarkibi

def newton_new_law(a,b,/,*,c,d):
    formul=a+b+c+d
    return d


#----------
#a,b,c,d -->yekseri argument
#ghabl az / --> bayad fasgaht adad gozsshte she va tartib moheme
#bad az setare jhastan-->fght bayad esme arg ham bgi mass=10


newton_new_law(1,2,3,4)



g=newton_new_law(1,2,c=3,d=4)


#=================================
#=================================
#=================================
#=================================
#=================================
#=================================
#=================================
#=================================
#=================================
#=================================
'''
A1



A1_fname_lname

A1_SINA_AKBARI

ai.2024.pilehvar@gmail.com


fght 'yek' file A1_SINA_AKBARI.py 
.zip .rar .docs hichh XXXXXXXXXXX



5 
















'''





