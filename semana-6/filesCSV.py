#Formatos de Archivos
# Texto, binarios, planos (csv), XML, JSON
'''
code,name,surName 
23424,Angela Maria,Fuentes Pinto 
75643,Pedro Jose,Morales Diaz 
'''

path = './semana-6/resources/files/'
name_file = 'songs.csv'

songs = dict()

sw = False
with open( path + name_file, 'r') as file_csv:
    data = file_csv.readlines()
    for row in data:
        if sw:
            record = row.split(";")
            songs[record[0]] = {"title":record[1],"duration":record[2],"album":record[3],"interpreter":record[4]}
        else:
            sw = True

print(songs['65456'])
print('='*50)
#A partir de importar la libreria csv
#Leer datos
import csv
header = []
records = []
with open( path + name_file, 'r') as file_csv:
    data = csv.reader(file_csv,delimiter=";")
    header = next(data) #Descartar el Primer Registro
    for row in data:
        print('\t '.join(row))
        records.append(row)

    print(f'Se procesaron {data.line_num} Registros')
    print(f'Filas={len(records)} Columnas={len(records[0])}')

#Escribir datos en un archivo
header = ['id','name','is_vegetarian','calories','value']
data = [
    ['4354','Taco al Pastor','N','430','15000'],
    ['6465','Pasta','S','80','20000'],
    ['8737','Mojarra','N','560','34000']
]

with open('./dishs.csv','w') as dishs:
    save = csv.writer(dishs)

    #Guardar un Registro (cabecera)
    save.writerow(header)

    #Guardar varios Registros (datos)
    save.writerows(data)

with open('dishs.csv','r') as dishs:
    data = csv.reader(dishs)
    next(data)
    dic_dishs = dict()

    for row in data:
       code = row[0]
       name = row[1]
       is_vegetarian = True if row[2] == 'S' else False
       calories = int(row[3])
       value = int(row[4])
       dic_dishs[code] = {"name":name,"vegetarian":is_vegetarian,"calories":calories,"value":value}

print(dic_dishs)
print(dic_dishs['6465'])



print('Fin Programa')