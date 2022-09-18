# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    self.index=[]
    self.inorder_recursion(0,self.index)
    for x in self.index:
      self.result.append(self.key[x])
    return self.result

  def preOrder(self):
    self.result = []
    self.index=[]
    self.preorder_recursion(0,self.index)
    for x in self.index:
      self.result.append(self.key[x])
    return self.result

  def postOrder(self):
    self.result = []
    self.index=[]
    self.postorder_recursion(0,self.index)
    for x in self.index:
      self.result.append(self.key[x])
    return self.result

  def inorder_recursion(self,N,array):
    if self.left[N]!=-1:
      self.inorder_recursion(self.left[N],array)
    array.append(N)
    if self.right[N]!=-1:
      self.inorder_recursion(self.right[N],array)

  def preorder_recursion(self,N,array):
    array.append(N)
    if self.left[N]!=-1:
      self.preorder_recursion(self.left[N],array)
    if self.right[N]!=-1:
      self.preorder_recursion(self.right[N],array)

  def postorder_recursion(self,N,array):
    if self.left[N]!=-1:
      self.postorder_recursion(self.left[N],array)
    if self.right[N]!=-1:
      self.postorder_recursion(self.right[N],array)
    array.append(N)

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
