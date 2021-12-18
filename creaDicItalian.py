
arch = open("texto.txt", "r")
texto = arch.read()
texto2 = ""
texto = texto.lower()
alfabeto = "abcdefghijklmnopkrstuvwxyz "
for c in texto:
    if c in "àèìòù":
        if c == "à":
            texto2+="a"
        elif c == "è" :
            texto2+="e"
        elif c == "ì" :
            texto2+="i"
        elif c == "ò" :
            texto2+="o"
        elif c == "ù" :
            texto2+="u"
    elif(c in alfabeto):
        texto2+=c
datos = texto2.split()
dic = []
for d in datos:
    if not(d in dic):
        dic.append(d)
dic.sort()      
print(dic)
arch.close()
with open("diccionarioIntaliano.txt",'w') as output:
    for row in dic:
        output.write(str(row)+" ")