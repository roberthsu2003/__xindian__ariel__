class Tools():
    @classmethod
    def underage(cls,a,n):
        if a < 18:
            print(f'{n}:未成年')
        else:
            print(f'{n}:成年')

class Bicycle():
    def __init__(self,c:str,w:int):
        self.color = c
        self.wheels = w

    #instance method
    def description(self):
        print("我是一台腳踏車")
        print(f"我的顏色是{self.color}")
        print(f"我有{self.wheels}輪子")