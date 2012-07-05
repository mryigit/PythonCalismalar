# -*- coding: cp1254 -*-
##### 4 farklı sekilde yaklasık hata ile kok hesaplayan program###

import math
import time
##############newtonrapson yontemi##############
def newtrap(x0 , A_s , U_s , E , adim):
    
    if fonk(A_s) * fonk(U_s) > 0:
        print "uygun olmayan aralik"
        
    else:
        x1 = x0 - (fonk(x0) / turfonk(x0)) #newtrap formul
        print "X%d = " %adim , x1
        
        if turfonk(x0) == 0:
            print "sifira bolme hatasi"
        
        elif abs(x1-x0) < E:
            return x1 , adim
        
        else:
            return newtrap(x1 , A_s , U_s , E , adim + 1)


##############secant yontemi##############
def secant(x0 , x1 , E , adim):
    egim = ( fonk(x1) - fonk(x0) ) / (x1 - x0)
    
    if egim == 0: # 0 a bolunme hatasini denetleyen kisim
        print "0 a bolunme hatasi"
        exit()
        
    elif abs(x1 - x0) <= E: # duyarliligin kontrol edildigi yer
        return x1 , adim-1
    
    else:
        x2 = x1 - ( (fonk(x1) * (x1 - x0)) / (fonk(x1) - fonk(x0)) ) # secant formul
        x0,x1 = x1,x2                          #yeni degerler atama
        #print "X%d = " %adim , x1
        return secant(x0 , x1 , E , adim + 1)


##############bisection yontemi##############
def yarilama(A_s , U_s , E , adim):
   
    if fonk(A_s) * fonk(U_s) > 0:
        print "uygunsuz aralik"
        exit()

    else:
        ort = (A_s + U_s) / 2.0
        #print "X%d = " %adim , ort
        
        if abs(A_s - U_s) < E:
            return ort , adim

        else:
            if fonk(A_s) * fonk(ort) < 0:
                U_s = ort

            else:
                A_s = ort
                
        return yarilama(A_s , U_s , E , adim + 1)

    
##############bisection yontemi##############
def regfalsi(A_s , U_s , E , adim):
    
    if fonk(A_s) * fonk(U_s) > 0:
        print "uygunsuz aralik"
        exit()
        
    else:
        x0 = ( (fonk(A_s) * U_s) - (fonk(U_s) * A_s) ) / (fonk(A_s) - fonk(U_s))
        x1 = ( (fonk(x0) * U_s) - (fonk(U_s) * x0) ) / (fonk(x0) - fonk(U_s))
        #print "X%d = " %adim , x0
        
        if abs(x1 - x0) < E:
            return x0 , adim

        else:
            if fonk(A_s) * fonk(x0) < 0:
                U_s = x0

            else:
                A_s = x0
                
        return regfalsi(A_s , U_s , E , adim + 1)
       



##############fonksiyon ve turevininin tanimlandigi kisim##############
def fonk(x):
    return math.log(x) - math.exp(-x)

def turfonk(x):
    return (1/x)+math.exp(-x)
########################################################################




#################newton test ###################
print "newthonrapson yontemi"
print "--------------------------------------"


n = newtrap(0.5 , 1 , 2 , 0.001 , 1)


print "adim sayisi = ",n[1]
print "kok = ",n[0]
print "gecen zaman = %f" % ((b-a)/1000.0)
print "--------------------------------------"
################################################


#################secant test ###################
print "\nsecant yontemi"
print "--------------------------------------"

c=time.clock()
for i in range(0,1000):
    s = secant(0.5 , 0.05 , 0.001 , 1 )
d=time.clock()

print "adim sayisi = ",s[1]
print "kok = ",s[0]
print "gecen zaman = %f"%((d - c) / 1000.0)
print "--------------------------------------"
#################################################


#################regfalsi test ###################
print "\nregulafalsi yontemi"
print "--------------------------------------"

g=time.clock()
for i in range(0,1000):
    r = regfalsi(1.0 , 2.0 , 0.001 , 1)
h=time.clock()

print "adim sayisi = ",r[1]
print "kok = ",r[0]
print "gecen zaman = %f"%((h-g)/1000.0)
print "--------------------------------------"
#################################################


#################bisect test ###################
print "\nbisection yontemi"
print "--------------------------------------"

e=time.clock()
for i in range(0,1000):
    b = yarilama(1.0 , 2.0 ,0.001 , 1)
f=time.clock()

print "adim sayisi = ",b[1]
print "kok = ",b[0]
print "gecen zaman =%f"%((f-e)/1000.0)
print "--------------------------------------"
#################################################
