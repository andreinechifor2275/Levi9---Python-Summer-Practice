from functools import reduce
import numpy


def exercise_1():
    """
    Write a function that prints numbers from 1 to 10.
    """
    for i in range(1,11):
        print(i)
    pass

def exercise_2(n):
    """
    Write a function that returns the sum of all numbers from 1 to n.
    Example: exercise_2(5) should return 15 (1+2+3+4+5)
    """
    return sum([num for num in range(1,n+1)])
    pass

def exercise_3(numbers):
    """
    Write a function that takes a list of numbers and returns only the even numbers.
    Example: exercise_3([1, 2, 3, 4, 5, 6]) should return [2, 4, 6]
    """
    return [num for num in numbers if num%2==0]
    pass

def exercise_4(text):
    """
    Write a function that reverses a string and returns a list with each letter.
    Example: exercise_4("hello") should return ["o", "l", "l", "e", "h"]
    """
    list = [letter [::-1] for letter in text]
    list.reverse()
    return list

    pass

def exercise_5(text):
    """
    Write a function that counts the number of vowels in a string.
    Example: exercise_5("hello world") should return 3
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

    pass

def exercise_6(numbers):
    """
    Write a function that finds the maximum number in a list.
    Example: exercise_6([3, 7, 2, 9, 1]) should return 9
    """
    return max(numbers)
    pass

def exercise_7(sorted_list, target):
    """
    Implement a search to find the index of a target value in a sorted list.
    Return -1 if not found.
    Example: exercise_7([1, 3, 5, 7, 9, 11], 7) should return 3
    """
    for index,value in enumerate(sorted_list):
        if value == target:
            return index
    return -1

    pass

def exercise_8(n):
    """
    Write a function that prints the multiplication table for a given number n.
    Example: exercise_8(3) should print:
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    ... up to 3 x 10 = 30
    """
    for i in range(1,11):
        print(str(n) + 'x' + str(i) + '=' + str(n*i))
    pass

def exercise_9(n):
    """
    Write a function that calculates the factorial of a number.
    Example: exercise_9(5) should return 120 (5*4*3*2*1)
    """
    x=1
    for i in range(1,n+1):
       x = x*i
    return x
    pass

def exercise_10(n):
    """
    Write a function that checks if a number is prime.
    Example: exercise_10(17) should return True, is_prime(15) should return False
    """

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

    pass

def exercise_11(list1, list2):
    """
    Write a function that finds common elements between two lists.
    Example: exercise_11([1, 2, 3, 4], [3, 4, 5, 6]) should return [3, 4]
    """
    return list(set(list1).intersection(list2))
    pass

def exercise_12(lst):
    """
    Write a function that removes duplicates from a list while preserving order.
    Example: exercise_12([1, 2, 2, 3, 4, 4, 5]) should return [1, 2, 3, 4, 5]
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

    pass

def exercise_13(text, shift):
    """
    Write a function that implements a Caesar cipher (shifts each letter by n positions).
    You can search for ord and chr functions to help with character shifting.
    ord - converts a Unicode character to its corresponding integer Unicode code point value.
    chr - converts an integer Unicode code point value back to its corresponding character.
    Example: exercise_13("abc", 2) should return "cde"
    """

    pass

def exercise_14(n):
    """
    Write a function that generates the first n numbers in the Fibonacci sequence.
    Example: exercise_14(7) should return [0, 1, 1, 2, 3, 5, 8]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

    pass

def exercise_15(text):
    """
    Write a function that checks if a string is a palindrome (ignoring spaces and case).
    Example: exercise_15("A man a plan a canal Panama") should return True
    """

    newtext = ''.join(text.lower().split())
    return newtext == newtext[::-1]

    pass


def exercise_16():
        matrix = np.random.randint(101, size=(15, 15))
        sortedelements = sorted(matrix.flatten())

        top, bottom, left, right = 0, 14, 0, 14
        index = 0
        result = [[0 for in range(15)] for _ in range(15)]
        while index < len(sorted_elements):
            for j in range(top, right + 1):
                result[top][j] = sorted_elements[index]
                index += 1
            top += 1

            for i in range(top, bottom + 1):
                result[i][right] = sorted_elements[index]
                index += 1
            right -= 1

            for j in range(right, left - 1, -1):
                result[bottom][j] = sorted_elements[index]
                index += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                result[i][left] = sorted_elements[index]
                index += 1
            left += 1

        for row in result:
            print([int(x) for x in row])



if __name__ == "__main__":
    print("Python Week 3 Exercises")
    print("Complete each function above to solve the exercises.")
    # exercise_1()
    # print(exercise_2(5))
    # print(exercise_3([1, 2, 3, 4, 5, 6]))
    # print(exercise_4('hello'))
    # print(exercise_5('hello world'))
    # print(exercise_6([3, 7, 2, 9, 1]))
    # print(exercise_7([1, 3, 5, 7, 9, 11], 7))
    # exercise_8(3)
    # print(exercise_9(5))
    # print(exercise_10(17))
    # print(exercise_11([1, 2, 3, 4], [3, 4, 5, 6]))
    # print(exercise_12([1, 2, 2, 3, 4, 4, 5]))
    # print(exercise_14(7))
    # print(exercise_15("A man a plan a canal Panama"))
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

    res = exercise_16(mat)

    print(" ".join(map(str, res)))