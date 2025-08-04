
'''
    Implement a stack!

    Create a class called Stack with the following methods:
        pop()
            returns the element on top of the stack,
            while also removing it.
            Raises an exception if there is no element left to pop.
            
        push(x)
            add x to the top of the stack.

        peek()
            return the element on top of the stack, without removing it

        is_empty()
            return True if the stack is empty, else False

        size()
            return the size of the stack.

        data()
            return the entire state of the stack. (For testing purposes)

    Do not use any built-in methods that would make this problem trivial.

'''

# Exception Class 
class StackException(Exception):
    def __init__(self):
        self.error_code = 'Improper Stack Usage!'
    def __str__(self):
        return f'{self.error_code}'
    
# Your implementation here
class Stack:
    pass

            





    
