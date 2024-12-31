a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(a is b)
c=a
print(a==c)
print(a is c)
a[2]='ok'
print(c)
print(id(a),id(b),id(c))
print(id(a) == id(b))
print(id(a) == id(c))
