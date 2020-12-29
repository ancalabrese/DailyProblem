# Given a singly-linked list, reverse the list. This can be done iteratively or recursively. 
# Can you get both solutions?

# Example:
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL

#Proposed solution: O(n)
# Iterative method: 
  # 1. Set node, previous and next node equals to head
  # 2. While we get to last node (Node.next = None) 
  #   a. set Next to node.next
  #   b. Set next to prev
  #   c. Set prev to current node
  #   d. Set current node to next
  # 3. When done adjust head.next (which is now the tail) to None and Node .next (which is the last node we were on) to previous

# Recursive: 
  # 1. Return current node if it's equal to None or his next == None (this way we first get to the end of the list)
  # 2. Once at the end get the Node returned (which is the previous in respect to the current) and
    # a. set current.next.next to current 
    # b set current.next to None 
  # 3. Return the node returned from Function 
  
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    node = prev = next = head
    next = head.next
    node = next
    while node.next != None: 
      next = node.next        
      node.next = prev
      prev = node      
      node = next

    head.next = None
    node.next = prev


  # Recursive Solution      
  def reverseRecursively(self, head):
    if head == None:
      return head
    if head.next == None :
      return head 

    node = self.reverseRecursively(head.next)
    head.next.next = head
    head.next = None

    return node
    

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4