"""A module for breadth-first traversal of trees."""

from collections import deque
from typing import Iterable
from tree import T


def bf_order(t: T | None) -> Iterable[int]:
    """Breadth-first traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(bf_order(tree))
    [2, 1, 4, 3, 5]
    """

    result = []
    #edge-case
    if t == None:
        return result
    
    s = deque([t])
    #alternative
    #rekursiv_in_order(t, result)
    while s != deque([]):
        first_tree = s.pop()
        result.append(first_tree.val)

        if (first_tree.left != None):
            s.appendleft(first_tree.left)
        
        if (first_tree.right != None):
            s.appendleft(first_tree.right)  


    return result
'''
def main():
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None))) 
    print(list(bf_order(tree)))

if __name__ == '__main__':
    main()
'''