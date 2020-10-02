# Linked List
+ [Palindrome Linked List](#Palindrome-Linked-List)
+ [Reverse Linked List](#Reverse-Linked-List)
+ [Middle of the Linked List](#Middle-of-the-Linked-List)
+ [Merge Two Sorted Lists](#Merge-Two-Sorted-Lists)
+ [ Remove Nth Node From End of List](#Remove-Nth-Node-From-End-of-List)
+ [ Reorder List](#Reorder-List)

## Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
```python
class Solution:
    def isPalindrome(self, head):
        if not head:
            return True

        def reverseList(head):
            if not (head and head.next):
                return head
            previous_element = None
            current_element = head
            while current_element:
                next = current_element.next
                current_element.next = previous_element
                previous_element = current_element
                current_element = next
            head = previous_element
            return head
        memory_head = head
        count, midPointer = 0, 0
        newhead = head
        while (head):
            if (midPointer != count // 2):
                newhead = newhead.next
                midPointer = count // 2
            count += 1
            head = head.next
        secondHalf = reverseList(newhead.next)
        check = True
        while (memory_head and secondHalf):
            if (memory_head.val != secondHalf.val):
                check = False
            memory_head = memory_head.next
            secondHalf = secondHalf.next
        return check
```
## Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
```python
class Solution:
    def reverseList(self, head):
        if not (head and head.next):
            return head
        previous_element = None
        current_element = head
        while current_element:
            next = current_element.next
            current_element.next = previous_element
            previous_element = current_element
            current_element = next
        head = previous_element
        return head
```
## Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
```python
class Solution:
    def middleNode(self, head):
        count,newhead = 0, 0
        current_element, middle_element = head, head
        while current_element:
            current_element = current_element.next
            count += 1
        if count % 2 != 0:
            newhead = int((count + 1) / 2)
        else:
            newhead = int((count / 2) + 1)
        for i in range(newhead - 1):
            middle_element = middle_element.next
```
## Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

```
##  Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
```python
class Solution:
    def removeNthFromEnd(self, head, n):
        result = head
        length = 0
        count = 1
        while result:
            result = result.next
            length += 1
        result = head
        number_to_delete = length - n
        if number_to_delete == 0:
            head = head.next
        else:
            while count < number_to_delete:
                result = result.next
                count += 1
            result.next = result.next.next
        return head
```
##  Reorder List
https://leetcode.com/problems/reorder-list/
```python
class Solution:
    def reorderList(self, head):
        if not (head or head.next):
            return
        result = []
        MidIndex = head
        LastIndex = MidIndex.next
        while (LastIndex and LastIndex.next):
            MidIndex = MidIndex.next
            LastIndex = LastIndex.next.next
        Current_element = MidIndex.next
        MidIndex.next = None
        while (Current_element):
            result.append(Current_element)
            Current_element = Current_element.next
        Current_element = head
        while (len(result) > 0):
            result[-1].next = Current_element.next
            Current_element.next = result.pop()
            Current_element = Current_element.next.next
```
