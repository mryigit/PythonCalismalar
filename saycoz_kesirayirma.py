# -*- coding: utf-8 -*-
#####PROBLEM:
##  kendisine verilen a / b kesirini aşağıdaki gibi ayirma işini yapan
##a / b = 1 / X₁ + 1 / X₂ + … + 1 / Xn
##örnek :
##2/7 = 1/4 + 1/28
##Kısıtlar:
##· program maksimum üç saniye içinde sonuç üretmeli
##· 1 ≤ a < b ≤ 1000 ,
##· X'ler birbirine esit olmamalı
##Kullanılan Yöntem:
##Adim 1-) Kesire en yakın 1/X bulunur. Buda “(PAYDA / PAY)+1”
##yontemiyle bulunur. Örneğin 2/7 icin “(7/2)+1” buda 4 e eşittir. Burda
##dikkat edildiyse bölme işleminde virgülden sonraki rakamlar işleme
##katılmamıştır yani integer bölmesi yapılmıştır.
##Adim 2-) Bulduğumuz değeri muhafaza ederek bize verilen kesirden bu
##değeri çıkarırız “2/7 – 1/4” eğer çıkarma işlemi sonucunda pay=1 olursa
##işlem bitmiş demektir
##Yukaridaki adimlar pay=1 olana kadar devam eder. Program her kendini
##çağırdığında pay ve payda güncellenir. Yani yeni pay ve yeni payda değeri
##çıkarma işlemi sonucundaki kesrin payı ve paydası olur bu işlemler pay = 1
##olana kadar devam eder pay = 1 oldugunda program bize kesrin parçalanmış
##halini sunar

#######################################################################
########################## ANA PROGRAM ################################
#######################################################################
def ayir(pay,payda,liste): # 2 kesir farkinin payi 1 olana kadar devam edecek olan ana fonksiyon

    kok = (payda / pay) + 1   #kesirimize den kucuk ama ona en yakin koku buluyoruz
    
    liste.append(kok)
    py,pd=cikarma(pay,payda,1,kok)  #listemize ekledigimiz koku kesrimizde cikardimiz ye
   
    
    if py==1:     #cikarma islemi sonucu yeni pay 1 ise kalan kesiride listeye
        liste.append(pd) # ekliyoruz ve progmin calismasi bitiyor
        return liste
    
    else:               #yukardaki kosul saglanana kadar ayni islemleri guncelledigimiz
        return ayir(py,pd,liste) #degerler ile tekrar ediyorzu taki py 1 olana kadar
    
    
def cikarma(pay1,payda1,pay2,payda2): # iki kesir arasinda cikarma islemi yapan fonksiyon
    yenipayda = payda1 * payda2
    yenipay = pay1*payda2 - pay2*payda1
    
    return yenipay/ebob(yenipay,yenipayda),yenipayda/ebob(yenipay,yenipayda) # sonucu sadelestirerek donduruyoruz


def ebob(n, d):        #iki sayinin enbuyuk ortak bolenini bulan program

    if d!=0:
        return ebob(d,n%d)
    else:
        return n



#######################################################################
########################## TEST KISMI #################################
#######################################################################
def dizitop(dizi):
    dizipay=0
    carpim=1                #2 ve 2den fazla kesrin pay kismini bulan fonksiyon
    i=0
    while len(dizi) > i:
        x = dizi.pop()
        i=i+1
        for j in dizi:
            carpim = carpim*j
                
        dizi.insert(0,x)
        
        dizipay=dizipay+carpim
        carpim = 1
    
    return dizipay

def pyd(dizi):
    dizipayda=1       #2 ve 2den fazla kesrin payda kismini bulan fonksiyon
    for r in dizi:
        dizipayda=dizipayda*r
    return dizipayda

def saglama(pay,payda,dizi):                # yukardaki fonksiyonlari kullanarak buldumuz sonucu ile verdimizi sonucu
    bol = ebob(dizitop(dizi),pyd(dizi))         #karsilastiran fonksiyon
    if 1.0*(dizitop(dizi)/bol)/(pyd(dizi)/bol) == (pay*1.0)/payda :
        return "saglama sonucu olumlu"
    else:
        return "saglama sonucu olumsuz"

def test_baslat():          # burasi deneme yapmamizi kolaylastirmak amaciyla kullanicidan girdi alan kisim
    durum = True
    while durum:
        l=""
        formlist=[]
        durum1 = raw_input("baslamak icin hehangi bir tusa cikmak icin Q ya basiniz!!!")

        if durum1 == "Q" or durum1 == "q":
            print "\ncikis yaptiniz"
            return 0
        else:
            durum = True
            
        x=input("pay :")                        
        y=input("payda :")
        if x >= y or y>1000 or x > 999:
            print "bu program bilesik kesirler icin uygun degildir ayrica pay maksimum 999 payda da maksimum 1000 olabilir"
            print "programdan cikildi"
            return 0
        k=ayir(x,y,[])
            
        t=saglama(x,y,k)
        if t=="saglama sonucu olumsuz":
            break
        k.sort()                                    ##########################
        formlist.append("%d/%d ="%(x,y))            #                        #
                                                    #                        #
        for i in k:                                 #                        #
            formlist.append("1/"+str(i)+" +")       #BURASI SONUCU FORMATLI  #
        x=formlist.pop()                            #                        #
                                                    #OLARAK YAZDIRMAK ICIN   #
        for i in range(len(x)-1):                   #                        #
            l=l+x[i]                                #TASARLADIGIMIZ KOD      #
        formlist.append(l)                          #                        #
                                                    #PARCACIGI               #
        for i in formlist:                          #                        #
            print "%s"%i,                           #                        #
        print "\n"+t+"\n"                           ##########################

test_baslat()
        
        
