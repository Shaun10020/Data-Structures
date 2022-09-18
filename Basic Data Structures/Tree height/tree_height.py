# python3

import sys
import threading

def find_height(index,height_array,parents):
    if height_array[parents[index]]!=None:
        height_array[index]=height_array[parents[index]]+1
        return height_array
    else:
        height_array=find_height(parents[index],height_array,parents)
        height_array[index]=height_array[parents[index]]+1
        return height_array

def compute_height(n, parents):
    # Replace this code with a faster implementation
    height_array=[None]*n
    index=0
    while parents[index]!=-1:
        index+=1
    height_array[index]=1
    current_index=0
    while current_index<n:
        if index==current_index or height_array[current_index]!=None:
            current_index+=1
            continue
        height_array=find_height(current_index,height_array,parents)
        current_index+=1
    return max(height_array)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
