import random
import time
import psutil, os

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def minDepth(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        return minDepth(root.right) + 1

    if root.right is None:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1


def maxDepth(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        return minDepth(root.right) + 1

    if root.right is None:
        return minDepth(root.left) + 1

    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def lca(root, n1, n2):
    while root:
           if root.val > n1 and root.val > n2:
               root = root.left

           elif root.val < n1 and root.val < n2:
            root = root.right

           else:
                 break

    return root


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)



def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def mem():
    process = psutil.Process(os.getpid())
    memory = process.memory_info()[0] / float(2 ** 20)
    print("Memory used:", memory)

file = open('numbers.txt', 'r')
content = file . readlines ()
arr = []
for line in content:
    arr.append(int(( line . rstrip () )))

s=Node(arr[0])
for i in range(1,len(arr)):
    s=insert(s,arr[i])
print("Inorder traversal")
inorder(s)
print("min depth",minDepth(s))
print("max depth",maxDepth(s))
print("**LCA**")
a=int(input("enter the element"))
b=int(input("enter the element"))
t = lca(s, a, b)
print(t.val)

while True:
    el = input("Enter the element you want to sort")
    array = random.sample(range(0, int(el)), int(el))
    start = time.time()
    time.sleep(1)
    heapSort(array)
    end = time.time()
    mem()
    print("time taken =",end-start)