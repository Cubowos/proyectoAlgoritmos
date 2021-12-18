alfabeto = "abcdefghijklmnopkrstuvwxyz"
arch = open("prueba.txt", "r")
texto = arch.read()
arch.close()
texto = texto.lower()
h = {}
for c in alfabeto:
    h[c]=0

for c in texto:
    if (c in alfabeto):
        h[c]+=1
print(h)
salida = open("salida.csv", "w")
for e in h.keys():
    cad = e +","+ str(h[e])+"\n"
    salida.write(cad)
salida.close()
    

