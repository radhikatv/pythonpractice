"""
Fetches factors of a given number
"""
num = int(input("Enter a Number"))
div = 1
print("Divisors of "+ str(num) + " are")
while div <= num:
    if num % div == 0:
        print (div)
    div += 1
