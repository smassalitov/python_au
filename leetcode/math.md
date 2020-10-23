+ [ Palindrome Number](#Palindrome-Number)
+ [ Reverse Integer](#Reverse-Integer)
+ [ Fizz Buzz](#Fizz-Buzz)
+ [ Base 7](#Base-7)
+ [ Fibonacci Number](#Fibonacci-Number)
+ [ Largest Perimeter Triangle](#Largest-Perimeter-Triangle)
+ [ Sqrt(x)](#Sqrt(x))

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
        if int(x) < 0 :
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
        for i in range (1, n + 1):
            if(i % 5 == 0 and i% 3 == 0):
                res.append("FizzBuzz")
            elif(i % 3 == 0):
                res.append("Fizz")
            elif(i % 5 == 0):
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
```
##  Base 7
https://leetcode.com/problems/base-7/
```python
class Solution(object):
    def convertToBase7(self, num):
        result = ''
        if num == 0:
            return('0')
        not_negative_num = abs(num)
        while not_negative_num > 0:
            result = str(not_negative_num % 7) + result
            not_negative_num = not_negative_num // 7
        if num < 0:
            result = '-' + result
        return result
```
##  Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
```python
class Solution(object):
    def fib(self, N):
        def RecurseFib(N):
            if  N == 0 or N == 1:
                return N
            if N > 1:
                return RecurseFib(N-1) + RecurseFib(N-2)
        return RecurseFib(N)
```
##  Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/
```python
class Solution:
    def largestPerimeter(self, A):
        A.sort(reverse = True)
        n = len(A)
        for i in range(n-2):
            if A[i] < A[i+1] + A[i+2]:
                return  A[i] + A[i+1] + A[i+2]
        return 0
```
##  Sqrt(x)
https://leetcode.com/problems/sqrtx/
```python
class Solution(object):
    def mySqrt(self, x):
        return str(x**0.5).split(".")[0]
```