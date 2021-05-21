
#딕셔너리 변수저장
dict_a={
    "name":"엔드게임",
    "type":"히어로무비",
    "ingredient":["망고","성탕","으잉?","황색소"],
    "origin" : "필리핀"
}
#출력
print("name : ",dict_a["name"])
print("type : ",dict_a["type"])
print("origin : ",dict_a["origin"])
#반복문
for ingredient in dict_a["ingredient"]:
    print("ingredient:",ingredient)

#바꾸기
dict_a["name"]="냐아아아아아"
print("name : ", dict_a["name"])

#딕셔너리 안에 리스트출력
print(dict_a["ingredient"][1])

#딕셔너리 값 추가
dict_a["price"] = 500000
print(dict_a)

#값 제거
del dict_a["price"]
print(dict_a)

#키 존제 유무 확인 in
if 'key' in dict_a:
    print(dict_a["key"])
else: print("없단다 아가야")

#get()
value = dict_a.get("adfasdf")
print("값 : ", value)

if value==None:
    print("없다고")

#반복문
for k in dict_a:
    print(k , ":" ,dict_a[k])



#문제
dict_b ={
    "name" : "구름"
}
print(dict_b)
del dict_b["name"]
print(dict_b)

#문제2
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number]+1
    else:
        counter[number] = 1

print(counter)

#문제3
type("문자열") is str
print(str)
type([]) is list
print(list)
type({}) is dict
print(dict)

character = {
    "name" : "기사",
    "level" : 12,
    "item" : {
        "sword" : "불꽃의검",
        "armor" : "풀플레이트"
    },
    "skill":["배기","ㅇ","ㅇ"]
}

for key in character:
    if type(character[key]) is dict:
        for i in character[key]:
            print(i,":",character[key][i])
    elif type(character[key]) is list:
        for i in character[key]:
            print(key, ":", i)
    else:
        print(key, ":", character[key])