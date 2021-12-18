from typing import Counter

def cargarPalabras():
    archivo = open("wordsitalian.txt","r")
    texto = archivo.read()
    datos = texto.split()
    archivo.close()
    return (datos)

alfabeto="abcdefghijklmnopqrstuvwxyz"
dic = cargarPalabras()

cifrado="Zdhrmxxj, bu hdcdllj rim dpmpd ymh zocxojhm dzorj bu cdeej, zd uju buj qbdxbuqbm. Qbmtej cdeej tm um dufdpd tmzyhm ou cohj rju dffjttj bu ydoj fo teopdxo, ymhroj Zdhrmxxj x�dpmpd riodzdej �Cdeej rju cxo Teopdxo O fbm mhduj rhmtrobeo dttomzm, m ox cdeej to mhd tmzyhm fozjtehdej zjxej nbhgj m nmxorm fo dobedhm Zdhrmxxj, qbdufj mhd ou fonnorjxed. Bu cojhuj ydhemroydhjuj dxxd nmted fmx ydmtm, fjpm Zdhrmxxj rjujggm Tdufhd, xd nocxod fmx horrj Tocujhjeej fmx yjtej. O fbm to ehjpdhjuj tbgoej tozydeoro, zd Tdufhd cod tdympd rim uju dphmggm yjebej nhmqbmuedhm Zdhrmxxj ymhrim tbj ydfhm uju x�dphmggm ymhzmttj. Oundeeo, ox ydfhm fo Tdufhd uju pjxmpd rim xd nocxod dpmttm dzoro ehd cxo dgoedueo fmx ydmtm, fd xbo hoemubeo fmo tmzyxorojeeo."
cifrado= cifrado.lower()
print(cifrado)

'''
def traduccion(cifrado): #funcion de traduccion
    nuevoTexto={'a':'m','b':'','c':'','d':'e','e':'','f':'','g':'','i':'','j':'o','k':'','l':'','m':'','n':'','o':'i','p':'','q':'','s':'','t':'','u':'','v':'','w':'','y':'','z':''}
    print(nuevoTexto,"\nEste es el diccionario que usaremos para descifrarlo ")
'''