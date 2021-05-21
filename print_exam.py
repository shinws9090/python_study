print("#하나만 출력1--------")
print()

print("#하나만 출력2--------","dkdkdk",sep="\n",end="\n\n")
print("결과",end="\n\n")

print("#여러 개를 출력합니다.-----------")
print(10,20,30,40,50,end="\n\n")

print(type(True),type("True"),type(12),type(12.5),sep="\n",end="\n\n")

print("이름\t나이\t지역")
print("오오오\t19\t강남")
print("""
    양
    오
    무아아아앙
    러러아인
""")

# print("하이"+1) 문자열이상 숫자는 안됨니당
print("하이,"*10)

print("#문자열 배열-------------------")
print("안녕하세열"[0])
print("안녕하세열"[1])
print("안녕하세열"[2])
print("안녕하세열"[3])
print("안녕하세열"[4])

print("#문자열 배열 거꾸러-------------------")
print("안녕하세열"[-1])
print("안녕하세열"[-2])
print("안녕하세열"[-3])
print("안녕하세열"[-4])
print("안녕하세열"[-5])

print("#문자열 범위선택-------------------")
print("안녕하세열"[1:4])
print("안녕하세열"[1:])
print("안녕하세열"[:4])
print("#문자열 범위선택(변수)-------------------")
hello = "안녕하세여"
print(hello[0:2])
print("#문자열 길이")
print(len(hello))

res = input("인사말을 입력하세요")
print("입력한것은",res)


a= "10 11 a b 14".split(" ")
print(type(a), a, sep='\n')