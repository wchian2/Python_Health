def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

response = int(input("Enter an integer!"))
print(response)

currentNumber = response

while currentNumber != 1:
    currentNumber = collatz(currentNumber)