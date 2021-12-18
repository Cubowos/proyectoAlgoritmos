from typing import Counter

def cargarPalabras():
    archivo = open("diccionarioIntaliano.txt","r")
    texto = archivo.read()
    datos = texto.split()
    archivo.close()
    return (datos)

alfabeto="abcdefghijklmnopqrstuvwxyz"
dic = cargarPalabras()


cifrado="Zdhrmxxj, bu hdcdllj rim dpmpd ymh zocxojhm dzorj bu cdeej, zd uju buj qbdxbuqbm. Qbmtej cdeej tm um dufdpd tmzyhm ou cohj rju dffjttj bu ydoj fo teopdxo, ymhroj Zdhrmxxj x�dpmpd riodzdej �Cdeej rju cxo Teopdxo O fbm mhduj rhmtrobeo dttomzm, m ox cdeej to mhd tmzyhm fozjtehdej zjxej nbhgj m nmxorm fo dobedhm Zdhrmxxj, qbdufj mhd ou fonnorjxed. Bu cojhuj ydhemroydhjuj dxxd nmted fmx ydmtm, fjpm Zdhrmxxj rjujggm Tdufhd, xd nocxod fmx horrj Tocujhjeej fmx yjtej. O fbm to ehjpdhjuj tbgoej tozydeoro, zd Tdufhd cod tdympd rim uju dphmggm yjebej nhmqbmuedhm Zdhrmxxj ymhrim tbj ydfhm uju x�dphmggm ymhzmttj. Oundeeo, ox ydfhm fo Tdufhd uju pjxmpd rim xd nocxod dpmttm dzoro ehd cxo dgoedueo fmx ydmtm, fd xbo hoemubeo fmo tmzyxorojeeo."
cifrado= cifrado.lower()
#d=e m=a 
#dpmpd
for pal in dic:
    if (len(pal)==5 and pal[0]==pal[-1]and pal[1]==pal[-2] and pal[2]=="a"):
        print(pal)#etate
print('-----------------------------------------')        
#ydmtm
for pal in dic:
    if(len(pal)==5 and pal[-1]==pal[-3]=="a" and pal[1]=="e"):
        print(pal)#deaua
print('-----------------------------------------')
#ydfhm
for pal in dic:
    if(len(pal)==6 and pal[-1]=="a" and pal[0]=="d" and pal[1]=="e" and pal[-3]!="a" and pal[-3]!="e") :
        print(pal)
print('-----------------------------------------')

#dffjttj
for pal in dic:
    if(len(pal)==7 and pal[0]=="e" and pal[-1]==pal[-4]):
        print(pal)


'''
D=e
M=a
P=t 
Y=d
T=u
F=b,m,s,v
h=r,s
'''
