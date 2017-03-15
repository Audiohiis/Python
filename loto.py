from random import randint

check = randint(0, 9)

def loto():
    number = input("Sisesta täisarv 0-9: ")
    if number.isdigit():
        number = int(number)
        print(check)
        if number < check:
            print("Number on väiksem")
            loto()
        elif number > check:
            print("Number on suurem")
            loto()
        else:
            print("Palju õnne, arvasite ära!")
loto()