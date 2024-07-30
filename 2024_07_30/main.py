#自訂的function
def underage(a,n):
    if a < 18:
        print(f'{n}:未成年')
    else:
        print(f'{n}:成年')


name = input("請輸入姓名:")
age = int(input("your age:"))
underage(age,name)
