figuritas = ['hulk','hulk', 'lebron james','hulk', 'lebron james','hulk', 'la mujer maravilla',
 'la mujer bionica', 'el hombre araña', 'lebron james', 'hulk']


for item in reversed(range(7)):
     print(item,end=' ')
print()

data = [0,1,2,3,4,5,6]
data.reverse()
for item in data:
    print(item, end=' ')
print()


data = [0,1,2,3,4,5,6]
for item in reversed(data):
    print(item, end=' ')
print()







# weekdays = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday",
#                 #0          1           2          3          4      
#   "Saturday", "Sunday"]
#    # 5           6



# stock = ['fideo', 'arroz', 'polenta', 'atun', 'atun', 'atun', 'caballa', 'caballa',
#       'harina', 'harina', 'langostino', 'langostino', 'langostino']


# stock = {'atun': 3, 'langostino': 3, 'caballa': 2, 'harina': 2, 'fideo': 1, 'arroz': 1, 'polenta': 1}

# for key, value in stock.items():
#     print(key, value)





# for item in repeticiones:
#     print(f'{item[0]}: {item[1]}')










##CONTROL STOCK PARA EL TURCO FARA



# #ALTERNATIVA 1
# stock = ['fideo', 'arroz', 'polenta', 'atun', 'atun', 'atun', 'caballa', 'caballa',
#      'harina', 'harina', 'langostino', 'langostino', 'langostino']

# reponer = [item for item in stock if stock.count(item) <= 2]
# print(reponer)


# #ALTERNATIVA 2
# stock = ['fideo', 'arroz', 'polenta', 'atun', 'atun', 'atun', 'caballa', 'caballa',
#      'harina', 'harina', 'langostino', 'langostino', 'langostino']

# reponer = []

# for item in stock:
#     if stock.count(item) <= 2:
#         reponer.append(item)

# print(reponer)
