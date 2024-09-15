key = 'value'
#Dictionary
dict = {'key1': "value1",'key2': 10, 'key3': True, 'key4': '25', 'key4':['red', 'bule'], 'key5':('mango','banana')}
print(dict['key2'])

key12val = dict.get('key12')
print(key12val)
print(dict)
dict['key6'] = "new_value"
print(dict)
del dict['key4']
print(dict)
print(dict.items())
for key,value in dict.items():
    print(key)
print("=================================")
for i in dict:
    print(i, dict[i])

print("==================================")
for i in dict.values():
    print(i)

print("=================================")
for i in dict.keys():
    print(i)
