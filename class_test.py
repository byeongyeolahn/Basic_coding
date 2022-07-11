# 
class Object:
    def __init__(self): # 생성자 
        self.v =1

    def add(self):
        self.v += 1
        
a = Object() # 오브젝트 생성
print(a.v)
a.add()
print(a.v)