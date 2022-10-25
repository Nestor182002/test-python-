"""
  3) ordenar los terceros que se tienen en el archivo data.py 
  por nombre, para obtener el nombre correcto se debe tener en 
  cuenta la siguiente validación:
  
  si el tercero tiene un (tradename != '') entonces se muestra este valor, 
  en caso contrario se debe obtener concatenando los siguientes 
  campos: (firstname, lastname, maidenname) en el orden dado
"""
from data import get_thirds

lists= []

data = get_thirds()
for thirds in data:
  if thirds["tradename"] != "":
    lists.append(thirds["tradename"])
  else:
    trade=thirds["firstname"] + thirds["lastname"] + thirds["maidenname"]
    lists.append(str(trade).upper())
print(sorted(lists))