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
        return middle_element
```
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
