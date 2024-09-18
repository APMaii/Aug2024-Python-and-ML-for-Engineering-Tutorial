
"""
IN THE NAME OF GOD

Created on Wed Sep 11 18:05:45 2024

@author: apm

L12 -->PROJECT2----------------

"""
import numpy as np
a=np.array([1,2,34])
a=np.array([[1,2,3],[4,5,6]])
#bkhatere list -->sari nist , do bodi nmsihe

#jadval -->numpy array 2 bodi besazimm

#list, numpy array 

#------FILE HANDLING---------
#FILE txt. csv . docs .gif jpg png

#built in function --> open
#fileton directory --> c://desktop/users/ali/fodlere 28/payanname.docs
open('c://desktop/users/ali/fodlere 28/payanname.docs')

#yek khorji , too zarf

zarf=open('c://desktop/users/ali/fodlere 28/payanname.docs')

#yek rahe dg k sade tare

zarf=open('payanname.docs') #samte rast FILES , directoryt hamonaje bashe k filet has
#[paynname.docsz not ofund]. there is no such file in directory
#yani spyder dastressi nadare b oonjae k filet vojod dare


#----arg 
#bahash kar koni
zarf=open('payanname.docs','r') #fght bekhoni
#w--->chizi bnvisi -->kolesho pak mikone v aminevise
#a ya x---> ezfef krdn
#a-->ag file vojdo ndshtebashe mrie msiaze va minvise
#x --.error
zarf.read()
zarf.readline()
zarf.write()
#*******applicsble karbodrdi nist

#azin ravehse open --> axi bkshi 
#data [ excel, csv , ...]
#frmat txt 
#python in formata nmishae --> str 'dshjgdsjgdksdhkah salma khobi 23635 2725 2375 2375 2378523'
#jadval sotoon radif


#dat amikhaym bkshim biroon , ?????????
#excel, c sv , jdval dahste basham ??
#----------
#pandas -->
import pandas as pd
#spyderemna dastrsi b in ketabkhone dare

#koli fucntions ttoosh dahst ,mtionstm estefade konm
#man mese numpy 
#numpy-->array array 1 body (list)   array 2 body (jadval)
#pandas-----> series (list1 bodi)   2 body--. Dataframe
#sade tarinesh ine --> esme radifaro , esme columna khdoet bsszi

#-------1bodi ha
listt=[10,20,30,40]
array=np.array([10,20,30,40])
#access
listt[1] #20
array[1] #20
array[1]= 100
print(array)

#pandas --> yek bodi --> numpy array 1D Series (SSS BOZORG)

jadid=pd.Series([10,20,30,40])
#bartari nesbast b numpy-->msihe index haro esmesho taghir dad

jadid=pd.Series([10,20,30,40],index=['a','b','c','d'])
jadid[1] #Out[46]: 20 hamoen base hamone
#koamki bma mikone
jadid['b'] #Out[47]: 20

#bartarie pandas-->[[ bma ejaze mdie esm gozari konim va b datamon rahat tar dastrsssi peyda konim]]


#-----2bodi------
#liust= XXXXXXXX
#bartarie numpuy
array2=np.array([  [10,20,30,40],[50,60,70,80]   ])
array2.ndim #2
array2.shape #Out[51]: (2, 4) 2 ta radi 4 ta sooton
#dastersii
#b 20 
#kdoom radif , kdoom sotooon
array2[0,1] #Out[52]: 20

#pandas 2 bodi bsazim
#12 bdi ha series 2 bodi ha DataFrame
#D , F bzoorg yadet nre ****

jadval=pd.DataFrame([[10,20,30,40],[50,60,70,80]])
#sdakhtanesh hcih chizi frgh nmikoen  ba numpy moo nmzine
#fght bto ejaze esm gozari mdie ba argument haye ezafe k too delet series, datframe

#mikahm radifamo nam gzoair konm
jadval=pd.DataFrame([[10,20,30,40],[50,60,70,80]],index=['a','b'])

#fght sotonamo
jadval=pd.DataFrame([[10,20,30,40],[50,60,70,80]],columns=['dama','feshar','time','output'])


#ham soton ahm radif mikham esm bzrm
jadval=pd.DataFrame([[10,20,30,40],[50,60,70,80]],index=['a','b'],columns=['dama','feshar','time','output'])

#mitoooni
array2=np.array([  [10,20,30,40],[50,60,70,80]   ])
#yek array hast
jadval=pd.DataFrame(array2,index=['a','b'],columns=['dama','feshar','time','output'])

#dotaye balaee ba ham frghi ndrn
#avalie khodmon dasti datahro nvshtim 10203040 ...
#dovomi aval yek numpy array dshtim msotaggim gzoashtiemsh inja(tabdile numpy array b dataframe)
'''
flashback-->
index   'alipilehvar meibdoyu'  a= indexe 0 ,..
list [10,20,30,40]   20 -->indexe 1
numpyarray 2 bnodi --> index msihdo row (radif ha)

inndex-->zamnai k esme moteghayer (zarf) sedsa mikzdim
braket mizashtim av bhsh acces 9dastresi
'''

jadval=pd.DataFrame([[10,20,30,40],[50,60,70,80]],index=['a','b'],columns=['dama','feshar','time','output'])
#ham indexash (radifahs) esm dre ham column ha soton ha esm dre

#------accesss--- dastresssiiii
#az numpyu  yadete vghty do bodi shodi 
#hamrogeh gfotn acces bgi kdoom radif kdoom sotoon



#--------row------ radif dasteresi peyda koni
#b rdovomin radif
#alan msihe radife b ya b soorat eghaidmi bgam radife 1
jadval.loc['b'] #50,60,70,80
jadval.iloc[1] # 50,60,70,80 radife 1 mikham kolesho

#.loc --> ba esmesh
#ag bkhay ba index seda koni ---> .iloc


#----------column ---->yek sotoon
jadval['dama']
jadval['feshar']
#doat sotoon
jadval[['dama','feshar']]

#pad masalan kahte 161 mige agha sootone feshar ro az jadval koelsho bde

#ya yek element --->
#-----element--- yani yk adad bkhay bkshi biron
#msln 50 ro mikham
jadval.loc['b','dama'] #Out[67]: 50
#ag bkhay indexi bnhsh dastresi peyda koni?
jadval.iloc[1,0] #Out[68]: 50

jadval.loc[ : ,'dama'] #mese 160 fght yek jadval


#----------------------------
#pandas gfo man dovomin bartarimo nshon midm
#mitonm rtabe haee too delasm drm k shoam bri va oon jadvaletro import koni inja
#

open() #hamsho etxt
#yek tabe drm (pandas) --> migirm va bsoorat eyek datafram (sotono raidf) tahvilet midm

pd.read_csv('directory')

#csv
#excel
#.....

#ya esme file ro  --> payanname.csv
# azmayeshgah.csv
#frit.csv
#valy baay doon rist FILES rooye file morede nazaret abshi k datsreis dshte bashe



#reahe docvom esme fileto ba driectorysh bnvis
#'C://USERS/DESKTOP/FOLDER 23/payananme.csv


pd.read_csv('ftir.csv')
#in khoroji mide

#Khoroji ro mirizi oto yzarf

jadval=pd.read_csv('ftir.csv')


a=open('/Users/apm/Desktop/MAIN/Hojjat Emami/Span network/Compact zip file/open that/experimental/f5.xlsx')
#kh az format haro support nmikoen


#pas har ketabkhoen omde yek tabe sakhte 
#excel, csv ,.. pandas
#ax ha , film ha , ----> opencv

jadval=pd.read_excel('/Users/apm/Desktop/MAIN/Hojjat Emami/Span network/Compact zip file/open that/experimental/f5.xlsx')



#in formate ddatframe o bokonm numpy?




a_array=np.array(jadval)

#==================
#man vaghty yek data daram
# ch formatie ---> .csv .xlsx .png .jpg .mp4 .doc .docx .txt

'''
.doc .docx .txt   -->matne tooshoi dar bairi
zarf=open('directory/ / / /khode_file.format')
zarfe str--->


.csv .xlsx
#jadvale , str  , dataframe 
a=pd.read_csv('directory/ / / /khode_file.csv')
b=pd.read_excel('directory/ / / /khode_file.xlsx')


.png .jpg .mp4
open()

ketabkhaneye opencv -->koli pardazeshe tasvir rule based
AI (ML BASED)
'''
jadval=pd.read_excel('/Users/apm/Desktop/MAIN/Hojjat Emami/Span network/Compact zip file/open that/experimental/f5.xlsx')



#mitonm numpy ham save konm??
#avalk pandas vared kon
a_array=np.array(jadval)


#----------
'''
np array to pandasl dataframe
a=np.array([10,20,30])
b=pd.DataFrame(a)


pandas datframe to nupy array 
a=pd.DataFrame([sdsdssdsd])
a=pd.read_csv()
b=np.array(a)
'''
#-[-------]

#hal;a k tonestim yek jadval bsazim
#k esm dahste bashe sotoon l, radif ha

#hamhcnin csv, ... --> injori vard konm 

#b aoon datframe chiakr miotonm konm???
#----------

#-------PANDAS
#ya khdoeton dastii vard koni datroi
a=pd.DataFrame([[1,2,3,4],[5,6,7,8]])# index , columns esm gzoair koni

#ya ye data improt koni
a=pd.read_csv('C:/USER/ / / / / /DATA.csv')


#a yek datafream ehast k sootn va ... dare
#access
#---row  iloc()  loc()
#----columns  []
#elemnt --> iloc(,)  loc ()


#---FUNCTION HA

data=pd.DataFrame([[10,20,30,40],[50,60,70,80],[90,100,110,120]],index=['a','b','c'],columns=['dama','feshar','time','output'])

#maximum chande
#rooye avriable mzinm .max()
data.max()

#numpy max  , min , ... 
#kodom radif , kodom sotoon

data.max(axis=0)  #too har soton max ro mide
data.max(axis=1) #too har radi max ro mide

#hamchnin
data['dama'].max() #Out[82]: 90

#yani toye data , sotone dama maxz kodome
#bishtar miran too ye sotoon va max ro mikhan

#kole datat ro sort koni--------
#tartib bedi
data=pd.DataFrame([[10,20,30,100],[50,60,70,40],[90,100,110,30]],index=['a','b','c'],columns=['dama','feshar','time','output'])

new_data=data.sort_values(by='output')


#concat dota darfram join

df1=pd.DataFrame([1,2])
df2=pd.DataFrame([3,4])

zarf=pd.concat([df1,df2])

#-------REMOVE----------
#data vared mikonid
#yek seri soton , radifo , dade ro hazfd koni (paksazi)


a=np.random.uniform(0,10,size=(50,3))


data=pd.DataFrame(a,columns=['Temp','Time','Modulus'])

#rewal word --> data=pd.read_csv('..data')
#yek soton ro hazf koni............
#sootne modulus ro nmikham

data2=data.drop(columns='Modulus')
#return mide yani bayad brizi otoye ye zarfe dg
#datae taghir nrkde ama data2 hazf shod

#hamishe aksare tabe haye pandas replace=False
#age nakhay dobare too zarfe jadid brizi va hamon
#khode datat taghir kone -->true

data.drop(columns='Modulus',inplace=True)
#inpalce=tru yani agha taghirati k goftmno roohamini k dot xadam (data ) emal kon man zarfe jhadid nmikham

zarf=data.drop(index=1) #radif ro hzzf krd

#.drop() baraye hazf krdne
#ag bnvisi index=..  oon radife delkahheto mitoni hazxf koni
#ag bnvisi sotoon --> on sdoton edelkhaheto mitoni hazf koni

#inpalce=True
data.drop(index=1,inplace=True)


#har taghiri dd (rmeove)
#tahesh
#********* plt.show() yek nokt einjori
data.reset_index(drop=True,inplace=True)


#----------YEK SETP GAHEL MACHIEN LEARNING HASTIM--------
#toonestim datamoon ro bairim tooye spyder
#besoorate dataframe zakhriahs kridm



data=pd.read_csv('data.csv') #va

#data--> ekdataframe do bdoi , yekserei radif dare , yekseri sotoon
#sotoon ha ham esm daran

#mikahm inp bdm b mdoele hooshe masnooee va yueseri kara konm
#ama moshkel......


#STEP0---->DATA CLEANING 
#PAKSAZI DADE 
a=np.random.uniform(0,10,size=(50,3))
data=pd.DataFrame(a,columns=['Temp','Time','Modulus'])

#az azmayeshga omde read_csv



#ag dade moshekl dahste bashe---> model haye ma run nashan , ya bema javabe doro snadamn , accuracy paeen biad
#naiz darim bstep 0 -->data cleaning



#moshekle data chia mione bashe????
'''
1-empty cell   yek adad khali bashe (khataye ensani, khataye dastgah, import) NAN None
2-wrong format    #asdad bashe str has
3-wrong data  (dama ha hame balaye 0 , -10)
4-duplicated (tekrari)


dalilesh harchi mikahd bashe
ama in 4 ta mroed -->moshekel data
pas---> ag ina residgegi nashan
momekne mdoele ma k data ro migire asan run nashe, moshekl dahste bashe , accuracy paen bashe va va va....

'''

#------1-EMPTY CELL----
a=np.random.uniform(0,10,size=(50,3))
data=pd.DataFrame(a,columns=['Temp','Time','Modulus'])
data.loc[5,['Temp']]=None
data.loc[17,['Temp']]=None
data.loc[20,['Temp']]=None

#---kari b bala nadahste bashid
#fk konid data -->az azmayeshgah omde

data.info()
'''

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50 entries, 0 to 49
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   Temp     47 non-null     float64
 1   Time     50 non-null     float64
 2   Modulus  50 non-null     float64
dtypes: float64(3)
memory usage: 1.3 KB

dataframe 50 ta radi fre 3 ta sotoon
baraye har sotooon nvshet type chie va 

47  non-null
50 radif
3 null-----> empy cell


'''
#1.1.tashkhis 
#felan ba data.info()
#empty cell haro tshkhis dadi

#sade tarin akri k mitoni koni
#bgei agha boro harjaaa harjaa empty cell has rmemoev kon oon radifo
data.dropna(inplace=True)
data.info()
'''
data.info()
<class 'pandas.core.frame.DataFrame'>
Index: 47 entries, 0 to 49
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   Temp     47 non-null     float64
 1   Time     47 non-null     float64
 2   Modulus  47 non-null     float64
dtypes: float64(3)
memory usage: 1.5 KB

47 ta sootron
hamashon 47 non-null
empty cell nadari


'''

#agha man nmikham hazf konm oon dade haro 

#data ziad dri 50 ,100 ,300 , 24834289619872398
#remove koni
#fill , adad bzaram
#bajye inke khali haro hazf konim chon koel radif hazf mishe etellate bararzeshe ma ham hazf msihe
#mitonim bgim bejaye inke hazf koni boro jaygozin bzar

#sadettarin ine ye adad khdoet bzari
data.fillna(10,inplace=True)

#pishrafte tar
#hey zarf misazam shoam inpalce=True

mymean=data['Temp'].mean()

new_data=data.fillna(mymean)

#ffil bfill 

new_data=data.fillna(method='ffill') #haraj khalie gjhablairo mizare

new_data=data.fillna(method='bfill')


new_data.info()
'''
 0   Temp     50 non-null     float64
 1   Time     50 non-null     float64
 2   Modulus  50 non-null     float64
 
 bejaye rmeove khdom pro krdm
 na tanha hame non -nuull
 bejaye 57 non null 50 non null
''' 

#2------wrong format gahlate

#temp--.float ,int  str 


data=pd.DataFrame([['1',2,3],['2',5,6]],columns=['temp','pressure','modulus'])

data.info()


'''
data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2 entries, 0 to 1
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   temp      2 non-null      object
 1   pressure  2 non-null      int64 
 2   modulus   2 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 180.0+ bytes
'''

#pandas

data['temp']=pd.to_numeric(data['temp'])

#oon sotoni k adadi nbdoe to adadi 


#-----3-moshekle mantehi dre
#masalan dama ya ychiz balay e0 bashe 
#ama shoam yeseri adad dama - dare

#aval baya dtashkhis bdi 
#bad egdham koni

#baraye tashkhis chikar konim??

#for done done bgrdid

data=pd.DataFrame([[20,2,3],[50,5,6],
                   [30,2,3],[70,5,6],
                   [20,2,3],[80,5,6],
                   [90,2,3],[100,5,6],
                   [20,2,3],[24,5,6],
                   [-10,2,3],[28,5,6],
                   [22,2,3],[20,5,6],
                   [20,2,3],[20,5,6]],columns=['temp','pressure','modulus'])

#n az format na khalie na hcihi
#khode data msohekel m,anteghi
#hala b har dalili

#aval tashkhis

#for bzni bri too tmep ha va bbini
count=0
for x in data.index:
    if data.loc[x,'temp']<0:
        count=count+1

print(count) # 12 doone damaye zxire sefrf vodjod dare

import matplotlib.pyplot as plt
y=data['temp']
plt.plot(y,'o')

#baraye tashkhi dota rah dri
#11---> for bzni too sotonet
#2-->sotoneto rasm koni

#hala k fhmidiii
#ya miokhay hazf koni ya mkhay .....


#hazf
for x in data.index:
    if data.loc[x,'temp']<0:
        data.drop(x,inplace=True)

#jaygozin koni
for x in data.index:
    if data.loc[x,'temp']<0:
        data.loc[x,'temp']=20 #y amiangine ...
        
        
#@jaee k data ziad dri hazf
#jae k dat akam dari batrjih midi chizi hazf nkoni



#4------Duplicated
#dade haye tekrari
b=data.duplicated()

#datat akme va mikhay bbini 

#vaghty daTaty ziade

#duplicated ejaze dari --.eyb nddrre tekrair bashe check nakon 

#@ye zmaon ejaze ndri
#mostaghim hazf oni duplicated haro
data.drop_duplicates(inplace=True)



#--------BAD AZ DATA CLEANING-------
#vaghty akret tamom shod
data.reset_index(drop=True,inplace=True)
#-----

'''
PANDAS ---> SERIES (NP.ARRAY 1 BODY K MITONE INDEX NAME BZRI)
DATAFRAME --> NP.ARRAY 2 BODY , COLUMN , INDEX ESM BZZARI

VA .. MITONIE EXCELETO, CSVITO BNA ESTEFADE AZ TABEYE READ_CSV , REWAD_EXCEDL
b soorate yek datafrasme too yek zarf brizi


vaghty rikhti 
ba info() mitoni info bgriii


#step 0 ghabla z ahrkari bayuad shoam  chika --.data cleaning
1-empty cell ---> info() , dropna() , fillna( mitoni adad bdi , mean, method='ffil','bbil')
2-wrong format --> to_numeric() rooye oon soton anjam bdi
3-worng data -->logical manteghi tashkhis--> for bzni (count) . plt.plot() / eghdam-->hazf koni drop() loc =
4-duplicated ->datat kam bodo duplicated() true false / ag ziad bod agar mikhasti k hazf koni . drop_duplicated()
 
va abd az tamiz krdne hameye ina
az reset_index yadet nare estefade koni


hala dateye to amade ye kar krdne

np , list series--> ketabkhone h aestefade koni



'''


#------------------
#==================
'''

request-->yek tabe benevisid k chanta application dahste bashe

a=pd.read_excel('')
dar a data fram dre


def 





'''



data=pd.read_excel('/Users/apm/Desktop/MAIN/Hojjat Emami/Span network/Compact zip file/open that/experimental/f5.xlsx')


#tdatash column stress , strain
#---harchi


'''

def(data,application):
    
    if application=='calculation':
        
        
    elif application=='plot':
        
    
    





'''

tabeyeshoma(data,'plot')
tabeyeshoma(data,'calcualtion')

'''
Tabe ee bayad besaziiid k dota vroodi bgire

yeki data
yeki oon kari k karbar donmableshe

'''

#hezaran data
#stress strain
#wave 
#ftri 
#

data=pd.read_excel('/Users/apm/Desktop/MAIN/Hojjat Emami/Span network/Compact zip file/open that/experimental/f5.xlsx')



def test(data,application):
    if application=='plot':
        x=data['Wavenumber  (cm -1)']
        y=data['Transmitance (a.u.)']
        plt.plot(x,y)
        plt.show()     
        
    elif application=='calcualt':
        print('salam')
    
    
    




data=pd.read_excel('/Users/apm/Desktop/MAIN/Hojjat Emami/Span network/Compact zip file/open that/experimental/f5.xlsx')
data.columns

test(data,'plot')

test(data,'calcualt')



'''

def test(data,application):
    
    if applciation=='plot':
        
    elif applciation=='max':
        yekare dg
        
    elif applciaation =='ssjdhn'
    
    
sakhataaaaaarrrrr


nesbat b rehste , alaghe , akri k mikahy anjam bdid
dorooze dg bbande paym bdid va bgid dar ch zmain eee kar mikonid

oon dastgahe mrotabety , dataye mortabete


polymer, stress strain 
dastgah 

data --?
data.csv

soton --> stresss 10,20,30,40,50,60,...
soton-->strain  1,2,3,4,5,6,7,8,9,......



#rasmesh konim 
rasmesh ch sheklie



#max stress

#max strain

#....



#-------B BESMELLA.....

data= dataframe yek sootonm stress yek soton strain

def Stress_Strain(data,application):
    stress=np.array(data['stress'])
    strain=np.array(data['strain'])
    
    if application=='plot':
        plt.plot(strain,stress)
        plt.title(-----)
        ....
        plt.show()
        
    elif application=='maxstress':
        maxstress=stress.max()
        return maxstress
    
    elif application=='maxstrain':
        maxstrain=strain.max()
        return maxstrain
    
    
    elif application=='alipilehvar':
        apm=maxstreeess+maxstrain
        return apm
    
    applicatyion---- 
    
    
dataee k entekhab krdiddd

data=pd.read_
Stress_Strain(data,'plot')
    

***naizi nsit too dle tabe dataframe baz 




#aval bgi ch dataee mikhay akr koni????


taraf ch dataee mitone b tabeye man bde


az koja entkehab


made nazare khdoet dare -->search bzn , ide bgir , ide rahnamaee
agar chzii monaeb peyda nkrdi


ai.2024.pilehvar@gmail.com 2 rooze


FTIR

shedate jaz
toole moji 

dota sotoon

'''


#entkehabe esme sootn

def FTIR(data,application):
    '''
    data= .csv .excell
    columns name=toolemoj , shedat
    application:
        plot --> drawng the wavelength on intensity
        maxintens--> maximum ....
        min....
        constant -->
        formula---->>
        
    
    '''
    x=np.array(data['toolemoj'])
    y=np.array(data['shedat'])
    
    
    
    if application=='plot':
        
        plt.plot(x,y)
        plt.title('----')
        plt.grid()
        plt.show()
        
    elif application=='max_attraction' :
        maxatract=y.max()
        return maxatract


#------
#telegram 
#-------
def Stress_Strain(data,application):
    stress=np.array(data['stress'])
    strain=np.array(data['strain'])
    
    if application=='plot':
        plt.plot(strain,stress)
        plt.title(-----)
        ....
        plt.show()
        
    elif application=='maxstress':
        maxstress=stress.max()
        return maxstress
    
    elif application=='maxstrain':
        maxstrain=strain.max()
        return maxstrain
    
    
    elif application=='alipilehvar':
        apm=maxstreeess+maxstrain
# =============================================================================
#         return apm
# =============================================================================


a=np.arange(0,100).reshape(-1,1)
b=np.random.uniform(0,10,size=100).reshape(-1,1)
c=np.concatenate([a,b],axis=1)
data=pd.DataFrame(c,columns=['Sotoone 1 ','Sootone 2'])








