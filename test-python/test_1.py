""" 
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""
from data import get_companies,get_branches

company = get_companies()
branches = get_branches()

for comp in company:
  print("_________")
  print("company : with id " + str(comp["id"]) + " and with name= " + comp["name"])
  print("the branches:")
  for branch in branches:
    if(branch["id"] in comp["branches"]):
      print("-- " + branch["name"])
  print("_________")

