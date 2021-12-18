from typing import Counter

def cargarPalabras():
    archivo = open("wordsFrench.txt","r")
    texto = archivo.read()
    datos = texto.split()
    archivo.close()
    return (datos)

alfabeto="abcdefghijklmnopqrstuvwxyz"
dic = cargarPalabras()


cifrado="Zdhrmxxj, bu hdcdllj rim dpmpd ymh zocxojhm dzorj bu cdeej, zd uju buj qbdxbuqbm. Qbmtej cdeej tm um dufdpd tmzyhm ou cohj rju dffjttj bu ydoj fo teopdxo, ymhroj Zdhrmxxj x�dpmpd riodzdej �Cdeej rju cxo Teopdxo O fbm mhduj rhmtrobeo dttomzm, m ox cdeej to mhd tmzyhm fozjtehdej zjxej nbhgj m nmxorm fo dobedhm Zdhrmxxj, qbdufj mhd ou fonnorjxed. Bu cojhuj ydhemroydhjuj dxxd nmted fmx ydmtm, fjpm Zdhrmxxj rjujggm Tdufhd, xd nocxod fmx horrj Tocujhjeej fmx yjtej. O fbm to ehjpdhjuj tbgoej tozydeoro, zd Tdufhd cod tdympd rim uju dphmggm yjebej nhmqbmuedhm Zdhrmxxj ymhrim tbj ydfhm uju x�dphmggm ymhzmttj. Oundeeo, ox ydfhm fo Tdufhd uju pjxmpd rim xd nocxod dpmttm dzoro ehd cxo dgoedueo fmx ydmtm, fd xbo hoemubeo fmo tmzyxorojeeo."
cifrado= cifrado.lower()
#d=e m=a QUIZAS

'''#probando con dpmpd
for pal in dic:
    if  (len(pal)==5):
        if(pal[0]==pal[-1]) :
            if(pal[1]==pal[3]):
                print(pal)
#dxxd
for pal in dic:
    if (len(pal)==4):
        if (pal[0]==pal[1] and pal[1]==pal[2]):
            print(pal)'''

#dffjttj
for pal in dic:
    if (len(pal)==7):
        if(pal[1]==pal[2] and pal[3]and pal[-1] and pal[-2]==pal[-3]):
            print(pal)