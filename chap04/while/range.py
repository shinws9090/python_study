
#범위
a = range(10)
print(a)

print(list(a))

print(list(range(10,20)))
print(list(range(10,20,2)))

n=10
#계산
a=range(0,int(n/2))
print(list(a))
a=range(0,n//2)
print(list(a))


#반복문
for i in range(5):
    print(str(i)+"반복")
print()
for i in range(5,10):
    print(str(i)+"반복")
print()
for i in range(0,10,3):
    print(str(i)+"반복")
print()

#몇번 반복인지 알아야할경우
array = [123,125,43,23,323]
for i in range(len(array)):
    print("{}번째 반복 : {}".format(i,array[i]))

#역순출력
for i in range(4,0,-1):
    print(i)

for a in reversed(range(5)):
    print(a)