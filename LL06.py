
"""
In The name of GOD
Created on Wed Aug 21 17:46:22 2024

@author: Alipilehvarmeibody

L6----


python-->zaban
harchizi k benevisi reserve shode
1-narenji (built in function -tabe haye dakheli)--> print(),iunput(),...
2-dastoorat (keywrod) --> is and or if if else elif for while def class , ....

harchize dg ro-->zarf , variable dar nazar migire
variable --> (numbers (int,float,complex),str('',function variabl.upper() khoroji),
              list , [], variable.append() apply ,touple,set,dict)


if --> 


IDE---> psudo code -->shebhe code
python , run kol
az bala b paeen az chap b rast mikhone
# ''' ''' , ignore mikone

vasatesh aghi ma mikhaym sharr bzarim (agar)-->if
agar inshe inakro kon -->if

agar inshod inakro kon agar nashod kare 2 -->if else

ma mitoonim to shbhe ciode 100 ta if , if else
if too
if a>20 :
    if b>30:
        ifc>40:
dastoorate shartii,
            

Tekrar, varresssi : halghe haye tekrar
Halghe --> 1-for 2-while

tekrar, avrresi 
agha bia az start ta end yek karo hey tekrar kon
(az start yeka dad ta 1-10 , az sare yek list ta tahe list)

zamani k tahe halghamon maloom bashe az for estefade mikonim
zamani k tahe halghe (10,20,30),shart -->while


"""

'''
sakhtar

if shart:
    dastoorat ( 1doone yta dah)

edame code
shart= == != > < >= <=  is in not in 
#and or 


if shart:
    dastoroate1
else:
    dastoorate2
    
    

#===========for

for i in ....:
    dastooorat(1doone ya dah ta)
    
i shomarande bood
... --> yek start va yejk end
ke baid i ro az start ta end hey bzare hey dastoor ro ejra kone



'''



for i in range(0,10):
    print('salam')

#i ro mizae 0 dastooro ejra mikone (print mikone salam
#i ro mziare 1 print mikone salam
#....
#i ro mizare 10-1=9 -->dastoor (print salam)
#i ro 9 , tahesh i ==/////10 halgeh biron
#va edameye code

'''
10 bar salam print


'''

#bekhatere inke hey i ro taghir mide mitonim biam
#Mostagim az i estefade konim
for i in range(0,10):
    print(i)
    
#miad i ro 
#i ro hey az start ta end tagir mdie va 'dastoor ro ejra'
#kare ma chie

# yek inke (start,end)
#dastooor
for i in range(0,10):
    print(i+1)



#tabeye range

for i in range(0,10,2):
    print(i)
'''
0
2
4
6
8
'''
#range yek raveshe
# range(0,10) --> [0,1,2,3,4,5,6,7,8,9]
#range (1,10) ---> [1,2,3,4,5,6,7,8,9]
#range(0,10,2) --> [0,2,4,6,8]
#range(0,10,3) --> [0,3,6,9]


#range(0,10)

#range(start,end-1,chanta chanta)

#range(0,10,1) 0,1,2
#range(0,10) -->hamin manie bala ama khasti atgir

#az 0 ta 100 5 ta 
range(0,100,5)

#in barat yek list mzsaze --> mitoni baiy azash too for estefade koni

for i in range(0,100,5):
    print(i)


for i in range(0,101,5):
    print(i)


a=range(0,100,5)
type(a) #Out[7]: range

#list , range
#class


#soal soale sare jaa
#range yekia z chiz haee hast k ma dar for estefade mikonim
#list

for i in [1,2,3,4,5]:
    print(i)


a=[1,2,3,4,5]
for i in a:
    print(i)

#tekrar -->list-->jaye range bazi mikone
#be ma in ide ro mide
#k az for fght baraye tekrar estefade konim
#baarye varredi , bazzresii-->iteration


#brii too ye list, bri to y kalame becharkhi done done
#start--> az avalin joz, harf ta end-->akharin harf, akahrin joz
#yek dastoori wejra koni ( bbinatesh , if count ,....)



b_list=[10,20,30,40]

for i in b_list:
    print(i)
    
#bazrresi iteration
for i in b_list:
    if i>25:
        print(i)
'''
30
40
'''
count=0
for i in b_list:
    if i>25:
        count=count+1

print(count)
#2

#ag bkham bgam oono bekesh biron chi 
#too ye liste dg ee


b_list=[10,20,30,40,50,60,70]
list_jadid=[] #************

for i in b_list:
    if i>25:
        list_jadid.append(i)
        
        
print(list_jadid)
#[30, 40, 50, 60, 70]


wanted_list=[]
#[0,1,2,...100]
for i in range(0,101):
    wanted_list.append(i)


print(wanted_list)





#i yani ahrchi tooye ....
#*** i ro index
b_list=[10,20,30,40,50,60,70]
new_list=[]
for i in b_list:
    if i>25:
        new_list.append(i)


#mitoni az ye rah dg ham bri
#az raveshe dg (indexi)
b_list=[10,20,30,40,50,60,70]
new_list=[]
#i -->0,1,2,3,4
for i in range(0,len(b_list)):
    if b_list[i]>25:
        new_list.append(b_list[i])



#for i in range(0,7): ***
#b_list[0]
#i=0




#------NEW_CASE
b_list=[10,20,30,40,50,60,70]
new_list=[]
for i in b_list:
    if i>25:
        new_list.append(i)


#balaye 25 boro indexo dar bi
#kodom indexa adade balaye 25 
#dar nahayat yek list az indexe oon adasdi bdede k az 25 bishtare
b_list=[10,20,30,40,50,60,70]
new_list=[]
for i in range(0,len(b_list)):
    if b_list[i]>25:
        new_list.append(i)


#for--->
#for i in range(start_numb,end_numb)
#for i in list,str

#***for i in range(0,len(list))



#-----------
for i in range(0,10):
    print('salam')

'''
shomarande 
start -->end
dastooor
paayne halghe
sharhe hal:
    i ro 0 , dastoor
    (afzayesh)i ro 1 , dastoor
    ,.
    i=9 , dastoor , tahe halghe mia dbiroon
'''
'''
i ro tarif koni 
i=start
shart bezari braye end

'''
#az i=0 boro ta zamani k i<10
#dastoor
'''
***ejra nakon
i=0
while i<10:
    print('salam')
'''

#i=0 
i=0
while i<10:
    print('salam')
    i=i+1
    
    
for i in range(0,10,1):
    print('salam')
    

'''
************
i=start
while i<end:
    print('salam')
    i=i+addnumb
    
    
for i in range(start,end,addnumb):
    print('salam')
'''
i=0

while i<10:
    print('salam')
    i=i+1

'''
salam
salam
salam
...
salam

10 bar salam ro type mikone
az 0 ta 10 -->[0,1,2,3,4,5,6,7,8,9]
for i in range(0,10):
    
'''

#---ravesh haye naghs
#eshtebahan start ro nanevisi
while i<10:
    print('salam')
    i=i+1
#NameError: name 'i' is not defined
    



#-------
i=20
while i<10:
    print('salam')
    i=i+1
    
#--khali
#varede halghenemishe
#start --> too shart 



#-----
'''
#nazaniid

i=0
while i<10:
    print('salam')
    
'''
#choon chizi nazashtie zafe she
#ta abad i=0
#endless loopp , looop bi payan





i=0 #start
#too shart bayad joroi  bashe k i betone vared she
while i<10:
    print('salam') #dastoor i if..
    i=i+1 #shomarande ro taghir bde
    
#mesle for , i , j , k ,a , 
for j in range(0,10):
    print('salam')
    
    
j=0
while j<10:
    print('salam')
    j=j+1
    
#===========
#for haye too dar tooo
for i in range(0,10):
    for j in range(0,5):
        print(i,j)
    
'''
i=0 ---> (0,0) (0,1) (0,2) (0,3) (0,4)
i=1 --> (1,0) (1,1) (1,2)  (1,3) (1,4)


'''


#======
#if , else


for i in range(0,10,1):
    print('salam')

i=0
while i<10:
    print('salam')
    i=i+1
    
    
#------
for i in range(0,10,2):
    print('salam')

i=0
while i<10:
    print('salam')
    i=i+2
    

#--------------
#----MIX------- 
#FOR IF ....
# 5, 6,....147
#tekrar , halghe
#start= 5 , end=147

for i in range(0,147):
    print(i)

#0,...146

for i in range(5,147):
    print(i)
    
#5....146

for i in range(5,148):
    print(i)
#5....147

#inaro bia brizs too ye list-------
#ye list bsaz [5,6,7,8,...148]
#nokte-->mige print nkon , briz too
listt=[10,20]
listt.append(30)
print(listt)



new_list=[]
for i in range(5,148):
    #XXX print(i)
    new_list.append(i)

print(new_list)

'''
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
 112, 113, 114, 115, 116, 117, 118, 119, 120, 121,
 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
 132, 133, 134, 135, 136, 137, 138, 139, 140, 141,
 142, 143, 144, 145, 146, 147]

'''

#------------------------------
#for ---> tekrar , print , count , append



await context.bot.send_message(
    chat_id=[99389223896],
    text=(
        f"Attention: Unauthorized access attempt by user {user_id}. \n\n"
        f"Error Message: {error_message}"))

await context.bot.send_message(
    chat_id=[3287979879],
    text=(
        f"Attention: Unauthorized access attempt by user {user_id}. \n\n"
        f"Error Message: {error_message}"))




developer_ids=[9939223896,3287979879]

for i in developer_ids:
    await context.bot.send_message(
        chat_id=i,
        text=(
            f"Attention: Unauthorized access attempt by user {user_id}. \n\n"
            f"Error Message: {error_message}"))
    
    
for i in range(0,10):
    print(i,' remaining second.')


for i in range(0,10):
    print(10-i,' remaining second.')

#0 , 1 , 2 , 3 ,4
for i in range(0,10):
    print(i,' remaining second.')




for i in range(10,0):
    print(i,'remaining start')

i=10
while i<0:
    print(i,'remaining time')
   
    
   
for i in range(10,0,-1):
    print(i,'remaining time')


for i in range(0,10,-1):
    print(i,'remaining time')



a=input('password: ')
print(len(a)*'*')


a='a123' #a=input('password: ')
for i in a:
    print('*')

'''
*
*
*
*
'''
print('ali','vahid')
print('ali','vahid',sep=' ')

print('ali','vahid',sep='*')


print('salam')
print('khoobi')

print('salam',end='\n')
print('khoobi',end='\n')

print('salam',end='')
print('khoobi',end='')
#salamkhoobi

a=input('password: ')
for i in a:
    print('*',end='')
    
#raveshe dovom 
a=input('password: ') 
count=0
for i in a:
    count=count+1
    
print(count*'*')
    


#------------------------
#quiz 1------------
#ba wile benevisid


#mix-----------------------------------
#dakhele
a=input('say yes or no')
#agar goft yes 10 bar benevsi mersi
#ag gof no yekbar benevis khahesh

if a=='yes':
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
    
        
if a=='no':
    print('khahesh')

a=input('say yes or no')
#agar goft yes 10 bar benevsi mersi
#ag gof no yekbar benevis khahesh

if a=='yes':
    for i in range(0,10):
        print('salam')
    
        
if a=='no':
    print('khahesh')
    
#chijori mitoni dar dele if for bzari
#yek shart ro mire chekc mikone
#dastooremon khodsh halghe

#fasele ha dar python kh moheme

#eshtebaha*****
if a=='yes':
    for i in range(0,10):

    print('salam')
    
    
    
#ag gof yes , 10 salam khooobi
#salam khoobi-->dastorii hast k too dele for
#hamash bayad too dele for bash

a='yes'
if a=='yes':
    for i in range(0,10):
        print('salam')
        print('khoobi')
    
    
a='yes'
if a=='yes':
    for i in range(0,10):
        print('salam')
    print('khoobi')
    
#if , for , else , ... badane (dastoor)

#**ghaalat
if a==20:
    print('salam')
    else:

#ghalat
if a==20:
    print('salam')
else:
print('khoobi')
   

#dorost
if a==20:
    print('salam')
else:
    print('khoobi')    

#nokte-->harchizi k dastoor dare  , if , else, elif, for, while , 
#bayad dastoro(dastoorat) --yek tab fsasele dashte
# bashe ta bere tooye badane (body)


#if , else ,  elif --
if 
else:
    
    
    
#----fori bzni k too delesh if -->varredi
a_list=[10,20,30,40]
for i in a_list:
    if i>30:
        print('bale')
 
        
a_list=[10,20,30,40]
new_list=[]

for i in a_list:
    if i>30:
        new_list.append(i)
#samte chap negah dar
#yek alamate msoalase baraxe sabz bahash kar kon


#dastoorat
pass
break
continue


for i in range(0,11):
    print(i)
      

#i==4 oono anjam nade
#bargard rtoo shoamreshe
#b code bala negah kon
#ag i shod 4 , dastoro ejra nakon boro badi

for i in range(0,11):
    
    if i==4:
        #bi mn edame bde
        continue
    
    print(i)
    
    
#gahi vaghta mikhay bgi agah ag 4 shod asan az kole
#halghe bia birooon
#barnagard too halghe
#4 shod ejra nakad vali abrgahst edame dad halghe
#agha bai biroon-->beshkoon halghe
for i in range(0,11):
    
    if i==4:
        break
    
    print(i)
    



#pass---> kari 
#20 ta tabe o 

if i==4:
    #yek shart inja hast
        
#SyntaxError: incomplete input

if i==4:
    pass #yadet abashe inja sharte
        
#Hosel nadari, bnayad bsihtar vaght



for i in range(0,10):
    #skadkj



for i in range(0,10):
    pass


#overalll
#Komaki dar if , for ,...

pass #hosele nadari , mikhay nsfe nime bzari badna por koni, fght ejra bshe
continue #b oon shart rressidi , ejrash nkon bargard too halgeh edame bede
break   #b oon shart residi , ejrash nakon , ama dg barnagard too halgeh (az halghe bia biroon , beshkon (break))
    
#halgeh --> bepar azin shoamrande, beshkon
#halgeh ee hast (for, while)--> if



#===============DEF=============
'''
SATHE : 1 , 2 ,3 ,4
REZAYAT_CLASS : A,B,C,D

**A -->BEHTARIN

'''



'''
code-->
sakhtar

mashinhesab


1-voorodii: khdoet, input, open, url (site)
2-calculation(mohasebta) (+,- ,...if,else,..,AI)
3-khoorji (print, save, site namayesh,..)


'''

a1=float(input('adade 1:'))
a2=float(input('adad2: '))
a3=input('amallgar: (jam/tafrigh/taghsim/zarb')

if a3.upper()=='JAM':
    c=a1+a2
    print(c)
elif a3.upper()=='TAFRIGH':
    c=a1-a2
    print(c)
else:
    print('amalgare mojod nist')
    #raise Typeerror('amalagr nist')
    
#vaghty taraf minevise jam dar code bala
#edame ejra nmishe

if a3.upper()=='JAM':
    c=a1+a2
    print(c)
    
if a3.upper()=='TAFRIGH':
    c=a1-a2
    print(c)

#computatione ezafe -->mohasebat



#1-vorodi
a1=float(input('adade 1:'))
a2=float(input('adad2: '))
a3=input('amallgar: (jam/tafrigh/taghsim/zarb')

#Mohasebe
if a3.upper()=='JAM':
    c=a1+a2
    print(c)
elif a3.upper()=='TAFRIGH':
    c=a1-a2
    print(c)
else:
    print('amalgare mojod nist')
    #raise Typeerror('amalagr nist')
#shebhe code --> ejra k mikone
#voroji


    
#aya mitonam yek box dashte basham
# vorodiii ---> [] --> khoroji
#shebhe codi


#bale chera nashe
#tabe --- [] jabe 


'''
Tabe (function)-->baraye ma yek jabe misaze
k kare bala ro(shebhe code)--> vorodi -->[dele khdoesh]-->khoroji mide


1step---> khode tabe ro besazish (ch vorodi , too delesh chiakr, khoroji)
2step--> estefade -->sedash bezanim (call)

#baghie afrad , khdoet 

'''



#tabe keyworde def misazi (baanfsh)

#aval b tabe at (jabe he) esm bdi

#daghighan mesle esme zarf ha ghavaninesho
#2 * ..
# 
#_

mashin hesab
mashin_hesab
print
#bvaraye esme tabe ham vojod dare
#yekseri vorodi 



def mashin_hesab():
    #dastooorat (calculation)
    #khoroji


'''
STEP1--->SAKHTESH ****
def esm(voordi):
    badane ( calcualtion, khooroji)



1-vorodi
2-claculation
3-khoroji
-->jabe




STEP2-->CALL



'''


#woorat masale
#yek jabe bashe k vorodi va khorojid ahste bashe

#voroodi --> adade1,adade2, amalgar
#mohaseb anjam bde va khoroji bde behem

#b onvane zarf mirizim tooye parantez
def mashin_hesab(adad1,adad2,amalgar):

    if amalgar=='jam':
        c=adad1+adad2
        print(c)
    elif amalgar=='tafrigh':
        c=adad1-adad2
        print(c)
    elif amalgar=='taghsim':
        c=adad1/adad2
        print(c)
    elif amalgar=='zarb':
        c=adad1*adad2
        print(c)
        
        

#******** Har zaman k run mikoni , chizi behet nemide
#balke sakhtaresh ro hefz mikone IDE
#tabe he ejra nemishe , skellet (badane)-->hefzesh
    

#yek chzi bename mashin_hesab vojod-->jabas
#gahblia --.zarf
#in chie ->jabas (vorodi m khoroi)




#step1--->sakhte tabe
#3 ta vorodi --> jabe (mohaseb) --> print



#step2------estefade kone az jabe
#3ta vorodi jabe khoroji
#call (seda zadan)
#sesme tabe

#vorodi ro koja bdm?

mashin_hesab(20,30,'jam')


'''
vaghty run mikonm
python az bala b paeen mikhone
mige too reservam esmi b in nam nis(print, if ) rnagi
mitone zarf bashe ya jabe
agar ma 
hamchin jabe e darsm
hamino barmigarde bala
barmiagrdebala mibine bale in jabe vojod dare va 3 ta vorodi migire
doabr ebarmigrde migbine ahan 3 ta vorodi behesh dadim
vorodi haro migire mirbre too tabe

'''
mashin_hesab(23,3223,2323)


#----------
#yekshanbe
#kMEL TABE , ketabkhone o .....
#A1_PROJECT
#besazid ----> tabe bayad dar delesh yek formuli
#yek akri k dar reshteye khdoeton ahst ro anjam bde
#list beheton midim ide begirid


#ZARF , IF , IF ELSE , FOR , WHILE 
#MIX HA -->hatman tamoom
#va varede tabe



#-----Q2-----
#BMI_CALCULATOR --> DEF
#jabe --> bmi_calcualtor
#2 ta vorodi , print ( chaghi, ....) harmogeh k sedash bznim






#-----Q3------
#tabe drim bnam setarezan
#vorodi azatoon str (passworde) -->print (****)





#--QUIZ -->TABE BENEVISID
#Q4,5,6,7,8,....

'''
Q_L6_FNAME_LNAME

ai.2024.pilehvar@gmail.com


Q1,Q2,Q3

ghabl az yekshanbe ersal farmaeed


'''
























    












