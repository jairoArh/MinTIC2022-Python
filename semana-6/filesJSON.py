'''
JSON (Javascript Object Notation),es un formato de texto sencillo para el 
intercambio de datos. 
Se trata de un subconjunto de la notación literal de objetos de JavaScript, 
aunque, debido a su amplia adopción como alternativa a XML, se considera un 
formato independiente del lenguaje.

Equivalencias de datos Python-JSON
    dict        - object
    list, tuple - collección
    str         - String
    int, float  - number
    True;False  - true, false
    None        - null
'''

import json

path = './semana-6/resources/files/'
name = 'clients.json'

with open(path + name,'r') as clients:
    data = json.load(clients)
    print('='*70)
    print(data[0]['accounts'][0]['residue'])
    for row in data:
        print(row)

name = 'marvel.json'
with open( path + name,'r') as marvel:
    avengers = json.load(marvel)
    print('-'*70)
    #for av in avengers["Marvel Cinematic Universe"]:
    #    print(type(av))

    for k,value in avengers.items():
        for k, val in value.items():
            print(val['title'])
        
print('&'*70)
with open('./semana-6/clients.json','r') as cl:
    data_cl = json.load(cl)
    for k,v in data_cl.items():
        for k1,v1 in v.items():
            print(f"{v1['lastname']}\n{v1['accounts']}")

#Exportar a archivos en formato JSON
with open('./semana-6/out.json','w') as out:
    d = dict({1:{"name":"Pollo","value":23453},
    2:{"name":" Bisteck","value":18500},
    3:{"name":"Taco al Pastor","value":15000},
    4:{"name":"Viudo de Pescado","value":38900}})

    json.dump(d,out)

print('*'*10,'Fin del Programa','*'*10)