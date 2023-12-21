# 0x06. Python - Classes and Objects - ALX SOFTWARE ENGINEERING

# My first square
Write an empty class `Square` that defines a square


# Square with size
Write a class `Square` that defines a square by: (based on 0-square.py)

- Private instance attribute: `size`
- Instantiation with size (no type/value verification)
- You are not allowed to import any module

**Why?**
Why size is private attribute?
The size of a square is crucial for a square; many things depend on it (area computation, etc.). As a class builder, you must control the type and value of this attribute. One way to have the control is to keep it private. You will see in the next tasks how to get, update, and validate the size value.


# Size validation
Write a class `Square` that defines a square by: (based on 1-square.py)

- Private instance attribute: `size`
- Instantiation with optional size: `def __init__(self, size=0):`
    - `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer"
    - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0"
- You are not allowed to import any module


# Area of a square
Write a class `Square` that defines a square by: (based on 2-square.py)

- Private instance attribute: `size`
- Instantiation with optional size: `def __init__(self, size=0):`
    - `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer"
    - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0"
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module


# Access and update private attribute
Write a class `Square` that defines a square by: (based on 3-square.py)

- Private instance attribute: `size`
    - Property `def size(self):` to retrieve it
    - Property setter `def size(self, value):` to set it:
        - `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer"
        - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0"
- Instantiation with optional size: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module


# Printing a square
Write a class `Square` that defines a square by: (based on 4-square.py)

- Private instance attribute: `size`
    - Property `def size(self):` to retrieve it
    - Property setter `def size(self, value):` to set it:
        - `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer"
        - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0"
- Instantiation with optional size: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - If size is equal to 0, print an empty line
- You are not allowed to import any module


# Coordinates of a square
Write a class `Square` that defines a square by: (based on 5-square.py)

- Private instance attribute: `size`
    - Property `def size(self):` to retrieve it
    - Property setter `def size(self, value):` to set it:
        - `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer"
        - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0"
- Private instance attribute: `position`
    - Property `def position(self):` to retrieve it
    - Property setter `def position(self, value):` to set it:
        - `position` must be a tuple of 2 positive integers; otherwise, raise a `TypeError` exception with the message "position must be a tuple of 2 positive integers"
- Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - If size is equal to 0, print an empty line
    - Position should be used by using space - Don’t fill lines by spaces when `position[1] > 0`
- You are not allowed to import any module


# Singly linked list
Write a class `Node` that defines a node of a singly linked list by:

- Private instance attribute: `data`:
    - Property `def data(self):` to retrieve it
    - Property setter `def data(self, value):` to set it:
        - `data` must be an integer; otherwise, raise a `TypeError` exception with the message "data must be an integer"
- Private instance attribute: `next_node`:
    - Property `def next_node(self):` to retrieve it
    - Property setter `def next_node(self, value):` to set it:
        - `next_node` can be `None` or must be a `Node`; otherwise, raise a `TypeError` exception with the message "next_node must be a Node object"
- Instantiation with data and next_node: `def __init__(self, data, next_node=None):`

And, write a class `SinglyLinkedList` that defines a singly linked list by:

- Private instance attribute: `head` (no setter or getter)
- Simple instantiation: `def __init__(self):`
- Should be printable:
    - Print the entire list in stdout
    - One node number per line
- Public instance method: `def sorted_insert(self, value):` that inserts a new Node into the correct sorted position in the list (increasing order)


# Print Square instance
Write a class `Square` that defines a square by: (based on 6-square.py)

- Private instance attribute: `size`
    - Property `def size(self):` to retrieve it
    - Property setter `def size(self, value):` to set it:
        - `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer"
        - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0"
- Private instance attribute: `position`
    - Property `def position(self):` to retrieve it
    - Property setter `def position(self, value):` to set it:
        - `position` must be a tuple of 2 positive integers; otherwise, raise a `TypeError` exception with the message "position must be a tuple of 2 positive integers"
- Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - If size is equal to 0, print an empty line
    - Position should be used by using space
    - Printing a Square instance should have the same behavior as `my_print()`


# Compare 2 squares
Write a class `Square` that defines a square by: (based on 4-square.py)

- Private instance attribute: `size`
    - Property `def size(self):` to retrieve it
    - Property setter `def size(self, value):` to set it:
        - `size` must be a number (float or integer); otherwise, raise a `TypeError` exception with the message "size must be a number"
        - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0"
- Instantiation with size: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Square instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<`, and `<=` based on the square area


# ByteCode -> Python #5
Write the Python class `MagicClass` that does exactly the same as the following Python bytecode:
