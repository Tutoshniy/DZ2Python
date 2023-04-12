num = int(input("Введите целое число: "))
check_num = num
BASE = 16
Answer = ""

while num:
    if num % BASE == 10:
        Answer += "A"
    elif num % BASE == 11:
        Answer += "B"
    elif num % BASE == 12:
        Answer += "C"
    elif num % BASE == 13:
        Answer += "D"
    elif num % BASE == 14:
        Answer += "E"
    elif num % BASE == 15:
        Answer += "F"
    else:
        Answer = str(num % BASE) + Answer
    num = num // BASE
print(Answer, hex(check_num))
