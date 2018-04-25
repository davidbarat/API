import pandas

data = [{"nom": "Little Pub", "type" : "Bar", "ambiance": 9, "note": 7},
     {"nom": "Le Corse", "type" : "Sandwicherie", "ambiance": 2, "note": 8},
     {"nom": "Café Caumartin", "type" : "Bar", "ambiance": 1}]

df = pandas.DataFrame(data)

print(data)
df