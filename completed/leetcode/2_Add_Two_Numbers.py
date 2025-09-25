"""
2. Add Two Numbers
작성일: 2025년 9월 26일

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""




# Definition for singly-linked list.class ListNode:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        output_l = ListNode(0)
        curr = output_l
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            n_sum = l1_val + l2_val + carry
            carry = n_sum // 10
            # allocate new ListNode
            curr.next = ListNode(n_sum % 10)
            curr = curr.next
            # update List
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return output_l.next



# Test Cases
if __name__ == "__main__":
    # Example 1
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = Solution().addTwoNumbers(l1, l2)
    # Expected Output: [7,0,8]
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

    # Example 2
    l1 = ListNode(0)
    l2 = ListNode(0)
    result = Solution().addTwoNumbers(l1, l2)
    # Expected Output: [0]
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

    # Example 3
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    result = Solution().addTwoNumbers(l1, l2)
    # Expected Output: [8,9,9,9,0,0,0,1]
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
