
'''
    Implement FizzBuzz!

    Write a function that iterates from 1 to n and:
        Print 'fizz' for multiples of 3
        Print 'buzz' for multiples of 5
        Print 'fizzbuzz' for multiples of 3 AND 5.
        
    Return a list containing all numbers that fizzed, buzzed, and fizzbuzzed.
'''
# Your implementation here
def fizzbuzz(n: int) -> list[int]:
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            print('fizz')
            res.append(i)
        elif i % 5 == 0:
            print('buzz')
            res.append(i)
        elif i % 3 == i % 5 == 0:
            print('fizzbuzz')
            res.append(i)

    return res
        
            



'''
    Vowels in a String

    Write a function that returns the number of vowels in a given string.
        Ex. 'python' -> 2
'''
# Your implementation here
def vowels(s: str) -> int:
    num_vowels = 0
    for char in s.lower():
        num_vowels += 1
    return num_vowels
        


'''
    Custom Reverse

    Write a function that reverses a given list.
        You may not use the built-in reverse() function.
        Hint: You may use O(n) space
'''
# Your implementation here

def reversal(l: list) -> list:
    rev = []
    for i in range(len(l) - 1, -1, -1):
        rev.append(l[i])

    return rev

    # return l[::-1]
    
        


'''
    Palindrome

    Write a function that checks if a string is a palindrome
        Return True if the string is the same forwards and backwards
        Return False otherwise
'''
# Your implementation here

def is_palindrome(string: str) -> bool:

    left = right = 0

    while (left < right):
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


'''
    Frequency Counter

    Write a function that takes a list and returns a dictionary of counts.
    The result should be a dictionary where
        Each key is a unique element of the list.
        Each value refers to how many times that key appears in the list.
'''
# Your implementation here




'''
    Cipher

    Write a function that shifts each character in a string by n letters.
    Ex. cipher('abc', 1) -> 'bcd'

'''
# Your implementation here


if __name__ == '__main__':
    result = fizzbuzz(100)
    print(result)
    
