'''
372. 超级次方
你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1：
输入：a = 2, b = [3]
输出：8
示例 2：
输入：a = 2, b = [1,0]
输出：1024
示例 3：
输入：a = 1, b = [4,3,3,8,5,2]
输出：1
示例 4：
输入：a = 2147483647, b = [2,0,0]
输出：1198
 
提示：
1 <= a <= 231 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b 不含前导 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-pow/
'''

from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int: # (a ^ p) % target
        target = 1337
        p = sum([i * 10 ** index for index, i in enumerate(b[::-1])])
        res = 1
        while p != 0:
            if (p & 1) == 1:
                res = (res * a) % target
            p >>= 1 # val1 >>= val2 , 相当于把 val1 除以 2^val2 并向下取整
            a = (a * a) % target
        return res

'''
执行结果：通过

执行用时：120 ms, 在所有 Python3 提交中击败了39.21%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了61.87%的用户
通过测试用例：55 / 55
'''