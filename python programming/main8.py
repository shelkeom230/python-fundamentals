# while loops 
print("enter a number")
num=int(input())

while num>4:
    print("number is greater than 4")
    num=int(input())

    if num==50:
        break
    if num==8:
        continue
    print("loop ended")