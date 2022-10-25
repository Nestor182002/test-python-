"""
  4) Mostrar de los terceros que se tienen en el archivo data.py los cualees no poseen cellPhone y email.
"""
from data import get_thirds

data = get_thirds()

for thirds in data:
  if thirds["cellPhone"] == None and thirds["email"] == "" :
    print("the company id: " + str(thirds["companyid"])+ " with identification: " + thirds["identificationNumber"] )
