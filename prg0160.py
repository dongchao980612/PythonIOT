cities=["Beijing","Chengdu","Wuhan","Tianjing"]
for city in cities:
    if city[0]=='W':
        break
    print(city,end=",")
else:
    print("No break")
print("Done!")

for letter in "Taobao":
    if letter=='o':
        continue
    print(letter,end="")