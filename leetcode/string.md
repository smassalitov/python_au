+ [ Valid Anagram](#Valid-Anagram)
+ [ Reverse String](#Reverse-String)

##  Valid Anagram
https://leetcode.com/problems/valid-anagram/
```python
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
```
##  Reverse String
https://leetcode.com/problems/reverse-string/
```python
class Solution(object):
    def reverseString(self, s):
        s = s.reverse()
```
