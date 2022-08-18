num1 = int(input("숫자 입력: "))

num2 = int(input("숫자 입력: "))


result = 0
while num1 >= 1:
    if num1 % 2 != 0:
        result += num2
    num1 //= 2
    num2 *= 2

print(result)
