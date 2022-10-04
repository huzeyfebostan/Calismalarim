
def collatz(number):
    if number % 2 == 0:
        number = number / 2
        return number
    else:
        number = number * 3 + 1
        return number

while True:
    try:
        num = int(input("Enter number:"))
        break
    except :
        print("Sayı girin")

print("Enter number:\n",num)
new_num = num

while True:
    new_num = int(collatz(new_num))
    print(new_num)
    if new_num == 1:
        break
