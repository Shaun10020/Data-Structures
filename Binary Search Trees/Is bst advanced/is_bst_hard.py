#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  keys=[]
  lefts=[]
  rights=[]
  for node in tree:
    keys.append(node[0])
    lefts.append(node[1])
    rights.append(node[2])
  if len(keys)==0:
    return True
  if not theholyjudging(keys,lefts,rights,0,-1,-1):
    return False
  return True

def theholyjudging(keys,lefts,rights,i,lower_bond,upper_bond):
  if upper_bond!=-1:
    if keys[i]>=upper_bond:
      return False
  if lower_bond!=-1:
    if keys[i]<lower_bond:
      return False
  if rights[i]!=-1:
    if not theholyjudging(keys,lefts,rights,rights[i],keys[i],upper_bond):
      return False
  if lefts[i]!=-1:
    if not theholyjudging(keys,lefts,rights,lefts[i],lower_bond,keys[i]):
      return False
  return True

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
