def custom_fizzbuzz(n):
    for i in range(1,n):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)

custom_fizzbuzz(int(input("Enter a number: ")))