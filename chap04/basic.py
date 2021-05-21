example_list = ["요소A","요소B","요소C"]

print(enumerate(example_list))
print(list(enumerate(example_list)))

for i ,value in enumerate(example_list):
    print(i,value)

example_dict = {
    "1":"123",
    "2":"234",
    "3":"345"
}

for key,value in example_dict.items():
    print(key,value)

array = []

for i in range(0,20,2):
    array.append(i*i)
print(array)

#리스트내포***********************
array = [i*i for i in range(0,20,2)]
print(array)

array=["사과","자두","초콜릿","바나나","체리"]
output=[f for f in array if f !="초콜릿"]
print(output)

output = [i for i in range(1,100+1) if "{:b}".format(i).count("0")==1]
print(output)
for i in output:
    print(i,":","{:b}".format(i))