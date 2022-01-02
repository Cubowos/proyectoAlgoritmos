from os import PathLike
from typing import Counter

def cargarPalabras():
    archivo = open("words.txt","r")
    texto = archivo.read()
    datos = texto.split()
    archivo.close()
    return (datos)

alfabeto="abcdefghijklmnopqrstuvwxyz"
dic = cargarPalabras()


cifrado="Xmzl tmhs m twat cjssewba jmzs. Qbesj xgbzjgiise cjssewba, ztsr xmb cs cjse mbe ltgub ml jsawlzsjse dsewajss dszl, m tgccr obgub ml xmz fmbxr. Fmwiqjs zg xgbzjgi zts cjssewba gf dsz xmzl cr bsqzsjwba, ml usii ml zts mcmbegbysbz gf fgjysj tgqlstgie dszl, tml jslqizse wb imjas bqycsjl gf fsjmi xmzl ugjieuwes, jspqwjwba dgdqimzwgb xgbzjgi. Wb xsjzmwb mjsml gqzlwes xmzl bmzwds jmbas, ztwl tml xgbzjwcqzse, migba uwzt tmcwzmz eslzjqxzwgb mbe gztsj fmxzgjl, zg zts snzwbxzwgb gf ymbr cwje ldsxwsl. Xmzl tmhs cssb obgub zg snzwjdmzs m cwje ldsxwsl uwztwb ldsxwfwx jsawgbl mbe ymr tmhs xgbzjwcqzse zg zts snzwbxzwgb gf wlgimzse wlimbe dgdqimzwgbl."
cifrado= cifrado.lower()

'''
S= e
M= a
J= r
L= s
E= d
A= g
W= i
Z= t
C= b
B= n
R= y
Q= u
P= q
I= l
F= f
T= h
G= o
U= w
H= v
D= p
X= c
O= k
Y= m
N= x
'''
#mjsml
for pal in dic:
    if(len(pal)==5 and pal[0]=="a" and pal[-2]=="a" and pal[2]=="e"):
        
            print(pal)
print("--------------------------")
#jsawlzsjse
for pal in dic:
    if (len(pal)==10 and pal[1]=="e" and pal[-2]=="e" and pal[-4]=="e" and pal[0]==pal[-3] and pal[0]!=pal[2] and pal[0]!=pal[-1]):
        print(pal)
print("--------------------------")

#cjse
for pal in dic:
    if (len(pal)==4 and pal[1]=="r" and pal[2]=="e" and pal[3]=="d"):
        print(pal)
print("--------------------------")
#cjssewba
for pal in dic:
    if(len(pal)==8 and pal[0]=="b" and pal[1]=="r" and pal[2]=="e" and pal[3]=="e" and pal[4]=="d"):
        print(pal)
print("--------------------------")

#cr
for pal in dic:
    if (len(pal)==2 and pal[0]=="b"):
        print(pal)
print("--------------------------")

#Qbesj
for pal in dic:
    if(len(pal)==5 and pal[1]=="n" and pal[2]=="d" and pal[3]=="e" and pal[-1]=="r"):
        print(pal)
print("--------------------------")

#jspqwjwba
for pal in dic:
    if(len(pal)==9 and pal[0]=="r" and pal[1]=="e" and pal[3]=="u" and pal[4]=="i" and pal[5]=="r" and pal[6]=="i" and pal[7]=="n" and pal[8]=="g"):
        print(pal)
print("--------------------------")

#wlimbe
for pal in dic:
    if(len(pal)==6 and pal[0]=="i" and pal[-1]=="d" and pal[-2]=="n" and pal[-3]=="a"):
        print(pal)
print("--------------------------")
#fsjmi
for pal in dic:
    if(len(pal)==5 and pal[-1]=="l" and pal[-2]=="a" and pal[-3]=="r" and pal[-4]=="e"):
        print(pal)
print("--------------------------")

#tml
for pal in dic:
    if(len(pal)==3 and pal[1]=="a" and pal[2]=="s"):
        print(pal)
print("--------------------------")

#gf
for pal in dic:
    if (len(pal)==2 and pal[1]=="f"):
        print(pal)
print("--------------------------")

#tmcwzmz
for pal in dic:
    if(len(pal)==7 and pal[1]=="a" and pal[-2]=="a" and pal[2]=="b" and pal[3]=="i" and pal[4]==pal[6]):
        print(pal)
print("--------------------------")

#uwztwb
for pal in dic:
    if(len(pal)==6 and pal[1]=="i" and pal[2]=="t" and pal[3]=="h" and pal[4]=="i" and pal[5]=="n"):
        print(pal)
print("--------------------------")
#tmhs
for pal in dic:
    if( len(pal)==4 and pal[1]=="a" and pal[0]=="h" and pal[-1]=="e"):
        print(pal)
print("--------------------------")

#bmzwhs
for pal in dic:
    if(len(pal)==6 and pal[0]=="n" and pal[1]=="a" and pal[2]=="t" and pal[3]=="i" and pal[5]=="e"):
        print(pal)
print("--------------------------")        
#dszl
for pal in dic:
    if(len(pal)==4 and pal[1]=="e" and pal[2]=="t" and pal[3]=="s"):
        print(pal)
print("--------------------------")


#xgbzjgi
for pal in dic:
    if(len(pal)==7 and pal[1]=="o" and pal[3]=="t" and pal[4]=="r" and pal[5]=="o" and pal[6]=="l"):
        print(pal)
print("--------------------------")

#obgub
for pal in dic:
    if(len(pal)==5 and pal[1]=="n" and pal[2]=="o" and pal[3]=="w" and pal[4]=="n"):
        print(pal)
print("---------------------------")

#fgjysj
for pal in dic:
    if len(pal)==6 and pal[0]=="f" and pal[1]=="o" and pal[2]=="r" and pal[4]=="e" and pal[5]=="r":
        print(pal)
print("--------------------------")
#bqycsjl
for pal in dic:
    if len(pal)==7 and pal[0]=="n" and pal[1]=="u" and pal[3]=="b" and pal[4]=="e" and pal[5]=="r" and pal[6]=="s":
        print(pal)
print("--------------------------")

#snzwjdmzs
for pal in dic:
    if len(pal)==9 and pal[0]=="e" and pal[2]=="t" and pal[3]=="i" and pal[4]=="r" and pal[5]=="p":
        print(pal)
print("--------------------------")
def traduccion(cifrado):
    nuevoTexto={'a':'g','b':'n','c':'b','d':'p','e':'d','f':'f','g':'o','h':'v','i':'l','j':'r','l':'s','m':'a','n':'x','o':'k','p':'q','q':'u','u':'w','r':'y','s':'e','t':'h','w':'i','x':'c','y':'m','z':'t'}
    

    transTable=cifrado.maketrans(nuevoTexto)
    cifrado = cifrado.translate(transTable)
    print(cifrado)

traduccion(cifrado)


