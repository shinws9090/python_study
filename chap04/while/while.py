

Key_list = ["name","hp","mp","level"]
value_list = ["기사",200,30,5]
character = {}

for i in range(len(Key_list)):
    character[Key_list[i]]=value_list[i]

print(character)


limit = 10000
i=1
sum_value=0
while sum_value < limit:
    sum_value+=i
    i+=1
print("{}를 더할때{}을 넘고 그때값은{}이다".format(i,limit,sum_value))

max_value = 0
a=0
b=0

for i in range(1,100//2+1):
    j = 100 - i
    current = i * j
    if max_value < current:
        a = i
    b = j
    max_value = current

print(a, b, max_value)