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

'''
#dgoedueo
for pal in dic:
    if(len(pal)==8 and pal[0]=="e" and pal[4]=="e" and pal[2]==pal[-1] and pal[3]==pal[-2]):
        print(pal)


'''
def traduccion(cifrado):
    nuevoTexto={}
    

    transTable=cifrado.maketrans(nuevoTexto)
    cifrado = cifrado.translate(transTable)
    print(cifrado)

traduccion(cifrado)

'''
