from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Xiaomi", "Note12", "+79815006548"))
catalog.append(Smartphone("Samsung", "S21", "+79540685236"))
catalog.append(Smartphone("Apple", "12s", "+79510152396"))
catalog.append(Smartphone("Honor", "90 Pro", "+79624586345"))
catalog.append(Smartphone("OPPO", "A78", "+75842369541"))

for obj in catalog:
    print (obj._brand, '-', obj._model,'.', obj._number)