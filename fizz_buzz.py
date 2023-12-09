fizz_buzz = ""
for number in range(1, 101):
    if number % 3 == 0:
        fizz_buzz = "Fizz"
    if number % 5 == 0:
        fizz_buzz += "Buzz"
    if number % 3 != 0 and number % 5 != 0:
        fizz_buzz = number

    print(fizz_buzz)
    fizz_buzz = ""