from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    stack = []
    for element in arr:
        stack.append(element)
    newlist = []
    for i in range(len(stack)):
        newlist.append(stack.pop())
    return newlist

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
