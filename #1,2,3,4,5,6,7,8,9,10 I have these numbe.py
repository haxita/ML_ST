#1,2,3,4,5,6,7,8,9,10 I have these numbers, do something to impress my 4 years old son
#I will show him the numbers and he will tell me the result
#good idead

#I will show him the numbers and he will tell me the result
#good idead
import random
import time

def main():
    print("I will show you some numbers and you will tell me the result")
    print("Let's start")
    time.sleep(2)
    numbers = [1,2,3,4,5,6,7,8,9,10]
    random.shuffle(numbers)
    print("The numbers are:")
    for number in numbers:
        print(number)
        time.sleep(1)
    result = sum(numbers)
    print("The result is: ", result)
    print("Good job!")

if __name__ == "__main__":
    main()  

    