import math as ma
import numpy as np

tahta = np.zeros([3,3])
global doluKutu
global bosKutu
global turn
global xOlanKutular
global oOlanKutular

xOlanKutular = {}
oOlanKutular = {}

turn = False
doluKutu = 0
bosKutu = 0
x = 0
y = 0

def sira():
    global bosKutular
    global doluKutu
    global bosKutu
    global turn
    bosKutular = {}
    for index in np.ndindex(tahta.shape):
        if(tahta[index] != 0):
            bosKutular[index] = tahta[index]        
    for index in np.ndindex(tahta.shape):
        if (tahta[index] == 1):
            doluKutu += 1
        else:
            bosKutu += 1

def kutuBosMu(x,y):
    if (tahta[x,y] == 0):
        return True
    else:
        return False
    
def oyunBittiMi():
    global doluKutu
    global bosKutu
    global turn
    sira()
    if (tahta[0,0] == tahta[0,1] == tahta[0,2] == 1):
        print("X oyuncusu kazandı")
        return True
    elif (tahta[1,0] == tahta[1,1] == tahta[1,2] == 1):
        print("X oyuncusu kazandı")
        return True
    elif (tahta[2,0] == tahta[2,1] == tahta[2,2] == 1):
        print("X oyuncusu kazandı")
        return True
    else:
        return False
    
print (tahta)

while True:
    if (turn == False):
        print("Sıra X oyuncusunda")
        x = int(input("x : "))
        y = int(input("y : "))
        kutuBosMu(x,y)
        if (kutuBosMu(x,y) == True):
            tahta[x,y] = 1
            xOlanKutular[x,y] = 1
            print(tahta)
            if (oyunBittiMi() == True):
                break
            turn = True
        else:
            print("Kutu dolu")
    elif (turn == True):
        print("Sıra O oyuncusunda")
        x = int(input("x : "))
        y = int(input("y : "))
        kutuBosMu(x,y)
        if (kutuBosMu(x,y) == True):
            tahta[x,y] = 2
            oOlanKutular[x,y] = 2
            print (tahta)
            if (oyunBittiMi() == True):
                break
            turn = False
        else:
            print("Kutu dolu")

