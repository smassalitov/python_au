+ [ Valid Anagram](#Valid-Anagram)
+ [ Reverse String](#Reverse-String)
+ [ Reverse String](#Reverse-String)
+ [ Reverse Vowels of a String](#Reverse-Vowels-of-a-String)
+ [ Reverse Words in a String III](#Reverse-Words-in-a-String-III)
+ [ To Lower Case](#To-Lower-Case)

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
##  Reverse String
https://leetcode.com/problems/reverse-string/
```python
class Solution(object):
    def reverseString(self, s):
        s = s.reverse()
```
##  Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
```python
class Solution(object):
    def reverseVowels(self, s):
        stack = []
        word = ""
        vowels = "aeiouAEIOU"
        for element in s:
            if element in vowels :
                stack.append(element)
        for element in s:
            if element in vowels:
                word+=stack.pop()
            else:
                word+=element
        return word
        
```
##  Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
```python
class Solution:
    def reverseWords(self, s):
        s=s.split()
        for word in range(len(s)):
            s[word]=s[word][::-1]
        return " ".join(s)
        
```
##  To Lower Case
https://leetcode.com/problems/to-lower-case/
```python
class Solution:
    def toLowerCase(self, str):
        result = ""
        for element in range (len(str)):
            if(ord(str[element]) >= 65 and ord(str[element]) <= 90):
                result += chr(ord(str[element])+32)
            else:
                result += str[element]
        return result
```
