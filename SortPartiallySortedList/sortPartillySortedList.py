# You are given a list of n numbers, where every number is at most k indexes away from its properly sorted index.
# Write a sorting algorithm (that will be given the number k) for this list that can solve this in O(n log k)

# Example:
# Input: [3, 2, 6, 5, 4], k=2
# Output: [2, 3, 4, 5, 6]
# As seen above, every number is at most 2 indexes away from its proper sorted index.

# Proposed solution: O(nLogk)
# Using a min heap tree with the initial k elements
# 1 by one remove heap elemnts and put them in an array, replace the removed element with a new elments from the source array

import sys

class MinHeap:
	def __init__(self,maxsize): 
		self.maxsize = maxsize
		self.elements = [-1]*maxsize
		self.size = 0

	def insert(self, n):
		self.size += 1
		currentIndex = self.size-1 
		self.elements[currentIndex] = n
			
		while(self.elements[currentIndex] < self.elements[self.parent(currentIndex)]):
			self.swap( currentIndex, self.parent(currentIndex))
			currentIndex = self.parent(currentIndex)

	def rightChild(self,i):
		return 2*i+1

	def leftChild(self,i):
		return 2*i+2

	def hasRightChild(self, i):
		return self.size > 2*i+1

	def hasLeftChild(self, i):
		return self.size > 2*i+2

	def parent(self, pos): 
		if pos == 0: 
			return 0
		if pos % 2 == 0:
			return pos // 2 - 1
		else:
			return pos // 2

	def swap(self,i1, i2):
		self.elements[i1], self.elements[i2] =  self.elements[i2],self.elements[i1]


	def isLeaf(self, pos): 
		if pos >= (self.size//2) and pos <= self.size: 
			return True
		return False

	def heapify(self, i):
		if not self.isLeaf(i):
			if self.hasRightChild(i) and self.elements[i] > self.elements[self.rightChild(i)]:
						self.swap(i,self.rightChild(i))
						self.heapify(self.rightChild(i))

			elif self.hasLeftChild(i) and self.elements[i] > self.elements[self.leftChild(i)]:
						self.swap(i,self.leftChild(i))
						self.heapify(self.leftChild(i))
	
	def printHeap(self):
		s = "["
		for n in range(0,self.size):
			s+= str(self.elements[n]) + " "
		s+="]"
		print (s)
					

	def delete(self,i):
			cache = self.elements[i]
			self.elements[i] = self.elements[self.size - 1]
			self.size = self.size - 1
			self.heapify(i)


def sort_partially_sorted(nums, k):
	minHeap = MinHeap(k+1)
	elements =[]
	for i in range(k+1):
		minHeap.insert(nums[i])

	i = k+1
	for rem_elements in range(i, len(nums)):
		elements.append(minHeap.elements[0])
		minHeap.delete(0)
		minHeap.insert(nums[rem_elements])


	while minHeap.size > 0 :
		elements.append(minHeap.elements[0])
		minHeap.delete(0)

	return elements

def main():
	print (sort_partially_sorted([3, 2, 6, 5, 4, 8, 9 , 7, 10], 2))
	#[2, 3, 4, 5, 6 , 7, 9, 10]

if __name__ == "__main__":
	main()