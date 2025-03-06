#x = {'key': 4}   # {'Key' : value}

#x['key'] = 5
#x[2] = [2,2,1,1]
#print(x)


x = {'key': 4} 

#print(list(x.keys()))

del x['key']
print(x)

for key, value in x.items():
    print(key, value)