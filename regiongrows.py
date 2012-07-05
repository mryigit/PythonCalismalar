### python ile goruntu isleme bolge buyutme(regiongrowing) yapan kod
#### test icin ####
## i=Image.open("coins.jpg")
## epsilon=23
## basnokt=(130,15)
## regiongrow(i,epsilon,basnokt)

class Kuyruk:
    def __init__(self):
        self.items = []

    def kbosmu(self):
        return self.items==[]

    def kekle(self,item):
        self.items.insert(0,item)

    def kcikar(self):
        return self.items.pop()

    def kboy(self):
        return len(self.items)
    
    def kvarmi(self, item):
        return (item in self.items)
        

import Image
import os
def regiongrow(im,eps,bas):
    Q=Kuyruk()
    s=[]
    x=bas[0]
    y=bas[1]
    im =im.convert("L")
    
    Q.kekle((x,y))
    while not Q.kbosmu():
        t = Q.kcikar()
        x = t[0]
        y = t[1]
        
        if x < im.size[0]-1 and \
           abs((im.getpixel((x+1,y)) - im.getpixel((x,y)))) <= eps :
            if not Q.kvarmi((x+1, y)) and not (x+1, y) in s:
                Q.kekle((x+1,y))
                
        if x > 0 and \
           abs((im.getpixel((x-1,y)) - im.getpixel((x,y)))) <= eps:
            if not Q.kvarmi((x-1, y)) and not (x-1, y) in s:
                Q.kekle((x-1,y))
                     
        if y < im.size[1]-1 and \
           abs((im.getpixel((x,y+1)) - im.getpixel((x,y)))) <= eps:
            if not Q.kvarmi((x, y+1)) and not (x, y+1) in s:
                Q.kekle((x,y+1))
                    
        if y > 0 and \
           abs((im.getpixel((x,y-1)) - im.getpixel((x,y)))) <= eps:
            if not Q.kvarmi((x, y-1)) and not (x, y-1) in s:
                Q.kekle((x,y-1))

        if t not in s:
            s.append(t)
            
    im.load()
    putpixel = im.im.putpixel
    
    for i in range (im.size[0]):
        for j in range (im.size[1]):
            putpixel((i, j), 0)

    for i in s:
        putpixel(i, 150)
        
    output=raw_input("kaydedilecek dosya adini giriniz: ")
    im.thumbnail((im.size[0],im.size[1]), Image.ANTIALIAS)
    im.save(output + ".JPEG", "JPEG")
