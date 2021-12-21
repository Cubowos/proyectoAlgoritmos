from os import PathLike
from typing import Counter

def cargarPalabras():
    archivo = open("diccionarioItaliano.txt","r")
    texto = archivo.read()
    datos = texto.split()
    archivo.close()
    return (datos)

alfabeto="abcdefghijklmnopqrstuvwxyz"
dic = cargarPalabras()


cifrado="Zdhrmxxj, bu hdcdllj rim dpmpd ymh zocxojhm dzorj bu cdeej, zd uju buj qbdxbuqbm. Qbmtej cdeej tm um dufdpd tmzyhm ou cohj rju dffjttj bu ydoj fo teopdxo, ymhroj Zdhrmxxj x'dpmpd riodzdej “Cdeej rju cxo Teopdxo O fbm mhduj rhmtrobeo dttomzm, m ox cdeej to mhd tmzyhm fozjtehdej zjxej nbhgj m nmxorm fo dobedhm Zdhrmxxj, qbdufj mhd ou fonnorjxed. Bu cojhuj ydhemroydhjuj dxxd nmted fmx ydmtm, fjpm Zdhrmxxj rjujggm Tdufhd, xd nocxod fmx horrj Tocujhjeej fmx yjtej. O fbm to ehjpdhjuj tbgoej tozydeoro, zd Tdufhd cod tdympd rim uju dphmggm yjebej nhmqbmuedhm Zdhrmxxj ymhrim tbj ydfhm uju x'dphmggm ymhzmttj. Oundeeo, ox ydfhm fo Tdufhd uju pjxmpd rim xd nocxod dpmttm dzoro ehd cxo dgoedueo fmx ydmtm, fd xbo hoemubeo fmo tmzyxorojeeo."
cifrado= cifrado.lower()

'''
D= e
M= a
P= s,t, r
T= t,p
X= b,c,f,m,s
U= s,t
F= t,h
Z= b,c,d,f,m,p,r,s,t,v
H= t
O= p,s
B= p,o,t
L= m
C= n
J= o
'''

#dpmttm
for pal in dic:
    if (len(pal)==6 and pal[0]=="e" and pal[-1] ==pal[2] and pal[-2]==pal[-3] and pal[-1]=="a"):
        print(pal)
print("------------------------")

#dxxd
for pal in dic:
    if (len(pal)==4 and pal[0]==pal[-1] and pal[0]=="e" and pal[1]==pal[-2]):
        print(pal)
print("------------------------")
#dufdpd
for pal in dic:
    if (len(pal)==6 and pal[0]==pal[-1] and pal[0]==pal[-3] and pal[0]=="e" and pal[1]!=pal[2]):
        print(pal)
print("------------------------")

#Zdhrmxxj
for pal in dic:
    if(len(pal)==8 and pal[-4]=="a" and pal[1]=="e" and pal[-2]==pal[-3] and pal[-1]!="e" and pal[-1]!="a" and pal[2]!=pal[3] and pal[2]!=pal[-2] and pal[-2]!=pal[0] and pal[-2]!=pal[3]):
        if(pal[-2]=="b" or pal[-2]=="c" or pal[-2]=="f" or pal[-2]=="m" or pal[-2]=="s"):
            print(pal)
print("------------------------")
#dobedhm
for pal in dic:
    if(len(pal)==7 and pal[0]==pal[-3] and pal[0]=="e" and pal[-1]=="a"):
        if(pal[-2]=="d" or pal[-2]=="c" or pal[-2]=="n" or pal[-2]=="t" or pal[-2]=="s" or pal[-2]=="t" or pal[-2]=="b" or pal[-2]=="p" or pal[-2]=="i"):
            print(pal)
print("------------------------")

#hdcdllj
for pal in dic:
    if(len(pal)==7 and pal[1]==pal[3] and pal[1]=="e" and pal[-2]==pal[-3] and pal[1]!=pal[-1]):
        if(pal[0]=="t" or pal[0]=="i"):
            print(pal)
print("------------------------")



'''
def traduccion(cifrado):
    nuevoTexto={}
    

    transTable=cifrado.maketrans(nuevoTexto)
    cifrado = cifrado.translate(transTable)
    print(cifrado)

traduccion(cifrado)

'''
