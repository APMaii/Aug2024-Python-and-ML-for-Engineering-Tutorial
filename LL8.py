#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In The Name of GOD

L8-----

Created on Wed Aug 28 18:02:11 2024

@author: Ali Pilehvar Meibody


    
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
        
        list --> mitoni koli (touple,set,dictionary)
        list.function()  a1.append()  -->apply
        
    Structure barname: quiz, man :psudocode (shebhe code)
    1-voorodi 
        assign (a=2,b=3) , input() , open() 
    2-mohasebat --> + - , ....if , for , while , ... AI
    3-khoroji --> save too variable (c) ,save to desktop,uploade website, print() ,khoroji
    


Yek karo hey tekrar konim ---> mitonim shabihe boxi
vorodi -->box-->khoroji


DEF --->FUNCTION (TABE)

1- voroodi dari
2-body (calculation)
3-khorojii

****khOOROJI != PRINT



2 step
1-step -->besdazi -->define
2-call ---> estefade sedash bzni


aval call kon , vorodi, khoroji , .....
**ag bkhay zakhgrie koni -->retrurn -->khoroji dare -->too ye zarf
fagaht bekham namayesh -->print --> return , zarf



Structure def

def name(vorodi1,...,):
    body(1 line)
    many lines
    
    [optional] return
    
Call
name(vorodi1)



run konid tab ero hatman --> sakhtar miad dasre python
python mifhme yek tabe dre bename welcome
badan mitoni sedash koni


call bad az define
"""

#bedoone vorodi va khoroji
def welcome():
    print('khosh oomadid')


welcome()
#vorodi nmigrft, khoroji hma nmidad (fght print mikrd)


#---vorodi bgire , khrooji dnre

def welcome(esm):
    print('khosh oomadid ', esm)

welcome('ali')
#vorodi migire, khoroji nmide (fght print)


#_---ham vorodi ham khoorji 
def welcome(esm):
    new=esm.upper()
    return new

b=welcome('ali')

#+yehcizi print
def welcome(esm):
    new=esm.upper()
    print('salam salam')
    return new

b=welcome('ali')



def welcome(esm):
    new=esm.upper()
    return new
    print('salam salam')

b=welcome('ali')


#---- vorodi nadahste , khrooji dahste

def pi():
    return 3.14

a=pi()

#local

def jam(a,b):
    c=a+b
    return c

d=jam(10,20)
#a o 10 , b 0 20 mzire c=30 


#a,b,c
print(a)
print(b)
print(c)
#zarfe movaghat -->tabe -->local variable

#birone tabe ham -->global
def jam(a,b):
    global c
    c=a+b
    return c

d=jam(10,20)
print(c)



#=====================================
'''
def name(arg):
    body
    return *
'''

def jam(a,b):
    c=a+b
    return c

jam(10) #TypeError: jam() missing 1 required positional argument: 'b'
jam(10,20,30) #TypeError: jam() takes 2 positional arguments but 3 were given


def jam(*a):
    c=a[0]*a[1]
    return c

jam(10,20,30)


jam(10,20,30,40,50,60,70,)


#-----
def jam(a,b):
    c=a+b
    return c


jam(10,20)
jam(a=10,b=20)

#gahi vaghta mihay bgi fght adad bnvis
#na arg_name poshtesh bzari

def force(a,b,/,*,c,d):
    formula=a+b+c+d
    return formula

#poshte / --> fght bayad adad bnvise
#bade * fght arg_name

force(10,20,c=20,d=40)




#===============PROJECT=============
#trick miznan tooye arg 
#trabe ro functionalize

def newton(mass,a):
    force=mass*a
    return force


#begam agah madamam barash tarif konm
#chon to jahan 2 ta made darim 
#quantumi --> nerwton law (tamim yafte)
#normal-->newton


#-=ACl276 yek made quantumi --> 2 g a=10
newton(2,10)
#yek tabeye jadid bsazi

def newton_quantum(mass,a):
    force=mass*a*1.45
    return force


#narim samte dota tabe 
#Mitonim bgim atbeye khodemon joda az mass o a
#ye vroodi bgire made


newton(10,2,)

def newton_quantum(mass,a,yes_or_not):
    if yes_or_not=='yes':
        force=mass*a
    if yes_or_not=='no':
        force=mass*a*1.45
        
    return force

newton_quantum(2,10,'no')




def newton_quantum(mass,a,yes_or_not):
    if yes_or_not=='normal':
        force=mass*a
    if yes_or_not=='quantum':
        force=mass*a*1.45
        
    return force

#error yes
newton_quantum(2,10,'yes')

#error N = n
newton_quantum(2,10,'Normal')


newton_quantum(2,10,'normal')
newton_quantum(2,10,'quantum')



def newton_quantum(mass,a,yes_or_not):
    if yes_or_not.upper()=='NORMAL':
        force=mass*a
    if yes_or_not.upper()=='QUANTUM':
        force=mass*a*1.45
        
    return force


newton_quantum(2,10,'normal')

newton_quantum(2,10,'Normal')

newton_quantum(2,10,'NorMal')





def welcome(esm,jensiat):
    if jensiat=='m':
        print('khosh amadid aghaye',esm)
        
    if jensiat=='w':
        print('khosh amadid khanoome',esm)
        

welcome('ali','m')    
welcome('bahar','w')  

  
welcome('ali','agha')    #ejra nmikone


#tabe
#calcualtion - equation
#shabih sazi ha -->equation ... ax 
#--------------------
#moadele hal koni
#--------------------
'''
2*x**2 + 3*x + 4 =0

delta=b**2 - 4*a*c






voorodi --> box --> khoroji (r)



'''


root(2**x*23)

root('2*x**2 + 3*x + 4 =0')


#a*x**2 + b*x + c =0

root(a,b,c)

'''
ma miomdim delta hesab mikrdim
agar kochiktr az 0 ->javab nadasht
ag =0 ye javab -b/2*a
ag >0 -_.do javaboo



'''
import math
def root_degree2(a,b,c):
    delta=b**2 - 4*a*c
    if delta<0:
        print('javabi nadaremoadele')
        
    if delta==0:
        r=-b/(2*a)
        print('moadele yek javab darad : ', r)
        
    if delta>0:
        r1=(-b+math.sqrt(delta))/(2*a)
        r2=(-b-math.sqrt(delta))/(2*a)
        print('moadedle 2 ta javab darad ',r1,'and',r2)
    
#2*x**2 + 3*x + 4 =0

root_degree2(2, 3, 4) 
root_degree2(2, 8, 4)
#tabe e hast k 3 vorodi migirad ,print fght mikne


#hkkhrooji dart
def root_degree2(a,b,c):
    delta=b**2 - 4*a*c
    if delta<0:
        return None
        
    if delta==0:
        r=-b/(2*a)
        return r
        
    if delta>0:
        r1=(-b+math.sqrt(delta))/(2*a)
        r2=(-b-math.sqrt(delta))/(2*a)
        return r1,r2

zarf=root_degree2(2, 8, 4)


zarf=root_degree2(2, 3, 4) 

#----Bache haye riazi , hooshe masnooe

root_degree2('3*x**2 + 2*x + 3 =0')

def root_degree2(eq):
    ind_a=eq.find('x')
    print(eq[ind_a-2])
    
#==================
#moadele diffrential

#newton- roghson.,...


#=====Tabe=====

#----a=0

#---4*x + 2
def Root_Degree2(a,b,c):
    '''
    This function calculate the roots based on calculation of delta in emprical equations
    Parameters
    ----------
    a : int
        first coeff
    b : int
        second coeff
    c : int
        third coeff

    Returns
    -------
    float
        roots

    '''
    if a ==0:
        print('lotfan daraje 2 bashe equation')
        return
    
    delta=b**2 - 4*a*c
    if delta<0:
        return None
        
    if delta==0:
        r=-b/(2*a)
        return r
        
    if delta>0:
        r1=(-b+math.sqrt(delta))/(2*a)
        r2=(-b-math.sqrt(delta))/(2*a)
        return r1,r2

Root_Degree2(0,10,5)




def Root_Degree2(a,b,c):
    '''
    This function calculate the roots based on calculation of delta in emprical equations
    Parameters
    ----------
    a : int
        first coeff
    b : int
        second coeff
    c : int
        third coeff

    Returns
    -------
    float
        roots

    '''
    if a ==0:
        raise TypeError('Please insert the secvondary equation')
    
    delta=b**2 - 4*a*c
    if delta<0:
        return None
        
    if delta==0:
        r=-b/(2*a)
        return r
        
    if delta>0:
        r1=(-b+math.sqrt(delta))/(2*a)
        r2=(-b-math.sqrt(delta))/(2*a)
        return r1,r2

Root_Degree2(0,10,5)


#========================
#========================
#========================


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




#===========================================
#===========================================

#az yek jaee , yek tabe ee bekjesham biron
#madule
import class_sep_2024

#ModuleNotFoundError: No module named 'class_sep_2024'



import class_sep_2024


#m an alan dastressi daram b in madule






rishe=class_sep_2024.Root_Degree2(5,10,2)




ekhtelaf(10,2) #NameError: name 'ekhtelaf' is not defined


mashin_hesab.ekhtelaf(10,2) #NameError: name 'mashin_hesab' is not defined



#be besmella
#====================
#bayad spyder k dri kar mikoni , file ha 
import mashin_hesab



d=mashin_hesab.ekhtelaf(10,20)

print(d)



#===============
#khodemon sakhtimmmm
#aya khode python chizhaee --> riaziato too dleesh dare??
import math #yek bar

#koli tabee


zarf=math.sin(0)

print(zarf)

#sin
#cos
#

a=2*3+4*math.cos()

math.pow(2,3) #Out[79]: 8.0
#radikal
math.sqrt(4) #Out[81]: 2.0


def poww(x,y):
    result=x**y
    return result

poww(2,3)


def sin(a):
    c= a**23 + a**22 + a**21 + ....
    return c



#=================================
#KETABKHOOONE HAAAA ---. madule , function , classss......
#aval import ....
#az delesh function bekeshi birooon


#200 000 
#hamasho laptob dare ?--->NA
#yeseriash -->math, random , statistic

import statistics


statistics.mean([10,20,30,40]) #Out[85]: 25



    
def miangin(list1):
    summ=0
    for i in list1:
        summ=summ+i
        
    lenn=len(list1)
        
    m=summ/lenn
    return m
  

miangin([10,20,30,40] )  #Out[83]: 25.0
    
#miane ,.....



#======================
#ooon ketabkhone haee beshim k nadarimeshooon


#200 000 ketabkhoone 


#--------
#search va peyda konim ketabkhone

#git hub
#https://github.com/
#google.com
#python library,. python package, python madule ,


#https://pypi.org



#taze mitoni peyda koni oon ketabkhone ee k bdrdetmikhore


#AI_BASED_chat_model 
import getpass

password = getpass.getpass("Enter your password: ")
print("You entered:", password)



#=================================
#miri vase download
#esme 

#+
#math.time,random,statistic,scipy , seaborn , getpass,....



#1-Numpy -->mOHASEBAT
#2-Pandas --> KAR BA DADE (DATA)
#3-matplotlib ---> Rasm
#4-sklearn ---> Machine learning
#5-tensorflow --> Deelearning


#+200 000 ketyabkhone vojod dare




#-----------------
#AI beporsi
#Github
#PYpi

#peydashon koni




#===================
#numpy
#tarighere install 
#baraye hame 
#har ketabkhone
#math, time , statistics
#numpy , pandas, matplotlib
#sk learn




#-------------------------------------
#numpy
#-->google -->search PIP numpy
#pip sme_ketabkhoone
#miri dakhele site va oon samte rast bala copy
#pip install numpy
#koja vared konm?


#----------
#miri anaconda
#base-->mizani environment (class)
#cmd.exe       powershell 
#install launch
#ejrash kon ---> yuek safeye siah

#----PIP install ro dar safgeye siah benevis copy paste
#enter bzn
#Montazewre vaysa
import numpy



#@jalase ayande numpy ro nasb dahste bashan

#agar nashdo?
#ai.2024.pilehvar@gmail.com


#========
#ravshed vom

#windows#
#win + r -->wt.exe



#wt


#conda activate (esme)
'''
conda activate class2024

'''

'''
pip install numpy
'''

#numpy
#matplotlib


#.......
'''

conda deactivate class2024

'''

#======================
















































































