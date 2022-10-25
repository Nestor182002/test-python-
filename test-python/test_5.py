"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""

from data import get_thirds,get_companies


company=get_companies()
data = get_thirds()
result = sorted(data, key=lambda x: x['firstname'])
for res in result:
  if res["tradename"] == "":
    for comp in company:
      if res["companyid"] == comp["id"]:
        print("third: " + res["firstname"] + " with company: " + str(comp["name"]))
  else:
      for comp in company:
        if res["companyid"] == comp["id"]:
          print("third: " + res["tradename"] + " with company: " + str(comp["name"]))