from stack import Stack


def reverse_string(my_string: str) -> str:
    rev_stack = Stack()
    rev_str = ""

    # TODO: your code goes here
    for char in my_string:
        rev_stack.push(char)
    
    for _ in range(rev_stack.size()):
        rev_str += rev_stack.pop()
    
    return rev_str

if __name__ == "__main__":
    print(reverse_string("hello"))  # olleh
