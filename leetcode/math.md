+ [ Palindrome Number](#Palindrome-Number)
+ [ Reverse Integer](#Reverse-Integer)
+ [ Fizz Buzz](#Fizz-Buzz)

##  Palindrome Number
https://leetcode.com/problems/palindrome-number/
```python
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        string_x = str(x)
        return string_x == string_x[::-1]
```
##  Reverse Integer
https://leetcode.com/problems/reverse-integer/
```python
class Solution:
    def reverse(self, x):
        x = str(x)
        if (int(x)<0) :
            x = int(x[0]+x[1:][::-1])
        else:
            x = int(x[::-1])
        if -2**31 <= x <= 2**31-1:
            return x
        else:
            return 0
```
##  Fizz Buzz
https://leetcode.com/problems/fizz-buzz/
```python
class Solution:
    def fizzBuzz(self, n):
        res = []
        for i in range (1,n+1):
            if(i % 5 ==0 and i% 3 == 0):
                res.append("FizzBuzz")
            elif(i % 3 == 0):
                res.append("Fizz")
            elif(i % 5 == 0):
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
```
