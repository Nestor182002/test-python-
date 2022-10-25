"""
9) realice una consulta al archivo data.py, muestre todos los items, 
  ordenelos por nombre y dentro de cada item agregue el color correspondiente,
  en caso de que esté lo tenga. 
  
  El resultado del ordenando debe ser así, en la parte inicial los items 
  que no tienen color y en la parte final los que si tienen color, todo dentro de
  un mismo objeto
"""
from data import get_colors,get_items

item_data=[]
element=[]
colors= get_colors()
items=get_items()

for item in items:
  if item["color"] == None:
    item_data.append({"name_item":item["name"],"color":item["color"]})

for item in items:
    if item["color"] != None:
      element.append({"name_item":item["name"],"color":item["color"]})
ordering = sorted(element, key=lambda x: x['name_item'])

item_data.append(ordering)
print(item_data)