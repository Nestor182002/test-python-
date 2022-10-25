"""
  6) ordernar las compañias por nombre y dentro de cada compañia, crear un objecto 
  llamado thirds el cual va a terner todos los terceros que pertenezcan a esa compañia
"""
from data import get_thirds,get_companies

company=get_companies()
data = get_thirds()

for res in company:
  for thirds in data:
      if thirds["tradename"] == "":
          if thirds["companyid"] == res["id"]:
            print( " company: " + str(res["name"])+ " third: " + thirds["firstname"] )
      else:
            if thirds["companyid"] == res["id"]:
              print("company: " + str(res["name"]) + " third: " + thirds["tradename"] )


    # if thirds["companyid"] == res["id"]:
      # print("the company: "+ str(res["id"]) + " and third: " + thirds["tradename"] )