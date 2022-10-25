"""
  10) realice una consulta al archivo data.py, muestre todos los terceros, reduzca la 
  información y solo muestre el nombre, la ciudad y identificacion, 
  ordenelos por identificación
"""
from data import get_thirds

order=[]
data = get_thirds()

for thirds in data:
  if thirds["tradename"] != "":
    order.append({"name":thirds["tradename"],"city":thirds["cityName"],"identificationNumber":thirds["identificationNumber"]})
  else:
    order.append({"name":thirds["firstname"],"city":thirds["cityName"],"identificationNumber":thirds["identificationNumber"]})

ordering = sorted(order, key=lambda x: x['identificationNumber'])

print(ordering)