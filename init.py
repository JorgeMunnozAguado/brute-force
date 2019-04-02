import requests
import hashlib, sys

let = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
list_lower = let.split(",")
list_upper = let.upper().split(",")
num = "0,1,2,3,4,5,6,7,8,9".split(",")

list_final = num + list_lower + list_upper

API_REST_URL = "https://tecreesmuylisto.com/"

req = requests.post(API_REST_URL, data={"s": "a"})

hashref = hashlib.sha256(req.content).digest()

fijado = []

while True:

    for s in list_final:

        cadena = ""

        for i in fijado:
            cadena = cadena + i

        cadena = cadena + s

        req = requests.post(API_REST_URL, data={"s": cadena})

        hashiter = hashlib.sha256(req.content).digest()
        print(cadena)
        if not hashref == hashiter:
            print("respuesta correcta: " + cadena)
            sys.exit()

    if len(fijado) == 0:
        fijado.append(list_final[0])

    elif fijado[-1] == list_final[-1]:
        fijado.append(list_final[0])

    else:
        fijado[-1] = list_final[list_final.index(fijado[-1]) + 1]