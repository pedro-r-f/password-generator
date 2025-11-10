"""Tree program

----------------
A coding project that creates a tree made of * based on the height

Author: Pedro R F
Date: 11/10/2025"""

def tree(height):
    'Prints a tree of * based on the specified height'
    length = height * 2 - 1
    stars = 1
    for _ in range (1, height + 1):
        print(('*'*stars).center(length))
        stars += 2

    'Prints the trunk'
    print(('*').center(length))

if __name__ == '__main__':
    print(tree(5))



