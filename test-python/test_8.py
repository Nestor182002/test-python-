"""
  8) realice una consulta al archivo data.py, muestre los items donde su codigo sea par,
  ordenelos por el precio de manera descendente y dentro de cada item agregue el color correspondiente.
"""
from data import get_colors,get_items

item_data=[]
colors= get_colors()
items=get_items()

for item in items:
  if item["code"][-1] != 0:
    if int(item["code"][-1])  % 2 == 0:
      item_data.append(item)
  else:
    item_data.append(item[-1])

print(sorted(item_data, key=lambda x: x['code'],reverse=True))