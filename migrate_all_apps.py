#coding:utf-8
import os
from datetime import datetime
data_inicio = datetime.now()

lista = [
    'controle_de_acesso',
    'eventos',
    'mensageiro',
    's1000',
    's1005',
    's1010',
    's1020',
    's1030',
    's1035',
    's1040',
    's1050',
    's1060',
    's1070',
    's1080',
    's1200',
    's1202',
    's1207',
    's1210',
    's1250',
    's1260',
    's1270',
    's1280',
    's1295',
    's1298',
    's1299',
    's1300',
    's2190',
    's2200',
    's2205',
    's2206',
    's2210',
    's2220',
    's2230',
    's2240',
    's2241',
    's2250',
    's2260',
    's2298',
    's2299',
    's2300',
    's2306',
    's2399',
    's2400',
    's3000',
    's5001',
    's5002',
    's5011',
    's5012',
]


os.system('python manage.py migrate auth')
os.system('python manage.py migrate contenttypes')
os.system('python manage.py migrate sessions')


for a in lista:
    print ''
    comando = 'python manage.py makemigrations '+a
    print "Executando: "+comando
    os.system(comando)
    print ''
    comando = 'python manage.py migrate '+a
    print "Executando: "+comando
    os.system(comando)


data_fim = datetime.now()
print 'Inicio:', data_inicio
print 'Termino:', data_fim
print 'Tempo decorrido:', data_fim - data_inicio


