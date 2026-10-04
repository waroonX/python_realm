"""
# Assembly Line Scheduling

## Problem Description

A car factory has two parallel assembly lines, **Line 1** and **Line 2**, each containing $N$ stations ordered sequentially from $0$ to $N - 1$. Station $j$ on Line 1 performs the same manufacturing task as Station $j$ on Line 2.

You are given:
* Two arrays `a1` and `a2` of size $N$, where `a1[j]` and `a2[j]` represent the processing time required at station $j$ on Line 1 and Line 2, respectively.
* Two arrays `t1` and `t2` of size $N - 1$, where `t1[j]` is the time cost to transfer from Line 1 station $j$ to Line 2 station $j+1$, and `t2[j]` is the time cost to transfer from Line 2 station $j$ to Line 1 station $j+1$.
* Entry times `e1` and `e2`, representing the time required to enter Line 1 or Line 2.
* Exit times `x1` and `x2`, representing the time required to exit from Line 1 or Line 2 after station $N - 1$.

Return the **minimum total time** required to assemble the car from start to finish.

---

## Constraints

* $1  N  10^5$
* $1  a1[i], a2[i]  10^4$
* $0  t1[i], t2[i]  10^4$
* $1  e1, e2, x1, x2  10^4$

---

## Examples

### Example 1

**Input:**
```python
a1 = [4, 5, 3, 2]
a2 = [2, 10, 1, 4]
t1 = [7, 4, 5]
t2 = [9, 2, 8]
e1 = 10
e2 = 12
x1 = 18
x2 = 7

Output: 35
"""

a1 = [4, 1, 3, 2]
a2 = [2, 10, 1, 4]
t1 = [7, 4, 5]
t2 = [9, 2, 8]
e1 = 10
e2 = 12
x1 = 18
x2 = 7

def car_assembly(a1, a2, t1, t2, e1, e2, x1, x2):

    n = len(a1)
    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = a1[0] + e1
    dp2[0] = a2[0] + e2

    for i in range(1, n):
        dp1[i] = min(dp1[i -1] + a1[i], dp2[i-1] + t2[i-1]+ a1[i])
        dp2[i] = min(dp2[i -1] + a2[i], dp1[i-1] + t1[i-1]+ a2[i])

    dp1[-1] = dp1[-1] + x1
    dp2[-1] = dp2[-1] + x2
    return min(dp1[-1], dp2[-1])

print(car_assembly(a1, a2, t1, t2, e1, e2, x1, x2))