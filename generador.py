import os
import time

def Generar():
    
    f = open ('/home/usuario/Escritorio/Python/Archivos/prueba.txt', 'w')
    f.write('hola mundo')
    f.close()
    time.sleep(5)
    f = open ('/home/usuario/Escritorio/Python/Archivos/prueba1.txt', 'w')
    f.write('hola mundo')
    f.close()
    time.sleep(5)
    f = open ('/home/usuario/Escritorio/Python/Archivos/prueba2.txt', 'w')
    f.write('hola mundo')
    f.close()
    time.sleep(5)
    f = open ('/home/usuario/Escritorio/Python/Archivos/prueba3.txt', 'w')
    f.write('hola mundo')
    f.close()
    
while True:
    Generar()
        
