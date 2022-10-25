"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales que se encuentre en una ciudad determinada, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""

# filter company and show branches if searched
from data import get_companies,get_branches
from os import system

company = get_companies()
branches = get_branches()

for branch in branches:
  print("-- " + branch["cityName"])


city = input("choose city of sucursal")
system("cls")

for comp in company:
  print("_________")
  print("company : with id " + str(comp["id"]) + " and with name= " + comp["name"])
  print("the branches:")
  for branch in branches:
    if(branch["id"] in comp["branches"] and city.upper() == str(branch["cityName"]).upper() ):
      print("-- " + branch["name"])
  print("_________")