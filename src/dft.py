"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T

# alternative solution
def rekursiv_in_order(t: T | None, result: list[int]):
    if t != None:
        rekursiv_in_order(t.left, result)
        result.append(t.val)
        rekursiv_in_order(t.right, result)
#solution
def in_order(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    result = []
    #edge-case
    if t == None:
        return result
    
    s = [t]
    #alternative
    #rekursiv_in_order(t, result)
    while s != []:
        first_tree = s.pop()
        if (first_tree.left != None):
            s.append(T(first_tree.val, None, first_tree.right))
            s.append((first_tree.left))
        else:
            result.append(first_tree.val)
            if first_tree.right != None:
                s.append((first_tree.right))


    return result

#test
def main():
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None))) 
    print(list(in_order(tree)))

if __name__ == '__main__':
    main()