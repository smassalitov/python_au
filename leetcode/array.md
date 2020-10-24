+ [ Max Consecutive Ones](#Max-Consecutive-Ones)
+ [ Flipping an Image](#Flipping-an-Image)
+ [ Transpose Matrix](#Transpose-Matrix)
+ [ Move Zeroes](#Move-Zeroes)
+ [ Squares of a Sorted Array](#Squares-of-a-Sorted-Array)

##  Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        currentMax,resultMax = 0,0
        for num in nums:
            if num == 1 :
                currentMax += 1
                if currentMax > resultMax:
                    resultMax = currentMax
            else:
                currentMax = 0
        return resultMax
```
##  Flipping an Image
https://leetcode.com/problems/flipping-an-image/
```python
class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            row.reverse()
            for element in range(0 , len(A)):
                if row[element] == 1:
                    row[element] = 0
                else:
                    row[element] = 1
        return A
```
##  Transpose Matrix
https://leetcode.com/problems/transpose-matrix/
```python
class Solution(object):
    def transpose(self, A):
        rows, collums = len(A[0]), len(A)
        Onerow, result = [], []
        for i in range(rows):
            for j in range(collums):
                Onerow.append(A[j][i])
            result.append(Onerow)
            Onerow = []
        return result
```
##  Move Zeroes
https://leetcode.com/problems/move-zeroes/
```python
class Solution(object):
    def moveZeroes(self, nums):
        for num in nums:
            if  num == 0:
                nums.remove(num)
                nums.append(num)
        return nums
```
##  Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
```python
class Solution(object):
    def sortedSquares(self, A):
         return(sorted([x*x for x in A]))
```