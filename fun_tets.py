#지역변수 = 해당 함수 내, 특정 지역에서만 사용 가능한 변수
# 전역변수 = 어디서든 사용 가능
v0 = 1000
def add(v1, v2):
    #global v0, 사용 시 전역 변수로 간주
    print(v0)
    return v1+v2

print(v0)
a = int(input("v1"))
b = int(input("v2"))
print("v1, v2 =" +str(add(a,b)))