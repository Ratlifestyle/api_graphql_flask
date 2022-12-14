a = ['id', 'code', 'name']

if all(value in a for value in ['id', 'code', 'name', 'stock']):
    print("aaa")
else:
    print('bbbb')
