

import requests
import hashlib, sys

let = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
list_lower = let.split(",")
list_upper = let.upper().split(",")
num = "0,1,2,3,4,5,6,7,8,9".split(",")

list_final = num + list_lower + list_upper

longitud = len(list_final) - 1

API_REST_URL = "https://tecreesmuylisto.com/"
# API_REST_URL = "https://httpbin.org/post"

req = requests.post(API_REST_URL, data={"s": "a"})

hashref = hashlib.sha256(req.content).digest()

def incrementar(list):

    i = 0
    ok = False
    
    while i < len(list):
        elt = list[i]
        if elt == longitud:
            list[i] = 0
            i += 1
        else:
            list[i] = elt + 1
            ok = True
            break
        pass
    pass

    if ok:
        return list
    else:
        return None
    pass
pass




ini = 1
fin = 3

i = ini

while i <= fin:
    
    list_aux = []
    j = 0
    while j < i:
        list_aux.append(0)
        j += 1
    pass

    

    while not list_aux:

        s = ''

        j = 0

        while j < len(list_aux):
            s = s + list_final[list_aux[j]]
            j += 1
        pass

        req = requests.post(API_REST_URL, data={"s": s})

        hashiter = hashlib.sha256(req.content).digest()
        print(s)
        if not hashref == hashiter:
            print("respuesta correcta: " + s)
            sys.exit()
        pass

        list_aux = incrementar(list_aux)

    pass


pass



print(req.content)
print()