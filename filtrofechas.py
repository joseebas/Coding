# Aquí estan todas las librerias que voy a usar
import os
import time
import shutil
import datetime
import glob
  
  
# Aqui es donde los archivos van a ser guardados
os.chdir(r"/home/joseebas/Escritorio/Python/Archivos")
  
all_files = list(os.listdir())
outputs = os.getcwd()
  
# Hacemos un bucle para que se detecten todos los archivos del directorio actual
for files in all_files:
    try:
        
        inputs = glob.glob(files+"\\*")
          
        for ele in inputs:
            shutil.move(ele, outputs)
       
        shutil.rmtree(files)
    except:
        pass
  
# Volvemos a hacer un bucle, con este bucle detectamos la fecha de creación y creamos tanto la carpeta donde se almacenaran los archivos, dejando los archivos en cada carpeta según su fecha
for files in os.listdir('.'):
      
    
    time_format = time.gmtime(os.path.getmtime(files))
    datetime_object = datetime.datetime.strptime(str(time_format.tm_mon), "%m")
    full_month_name = datetime_object.strftime("%b")
    dir_name = full_month_name + '-' + \
        str(time_format.tm_mday) + "-" + \
        str(time_format.tm_year)
  
    if not os.path.isdir(dir_name):  
        os.mkdir(dir_name)
    dest = dir_name
    shutil.move(files, dest)
      
print("Ejecutando script...")
