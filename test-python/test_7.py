"""
  7) realice una consulta al archivo data.py, muestre los items que tienen colores 
  y ordenelos por precio de manera ascendente
"""
from data import get_colors,get_items

item_data=[]
colors= get_colors()
items=get_items()
index=1
for item in items:
  print(index,item)
  if item["color"] != None:
    item_data.append(item)

print(item_data)