'''
为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。给你一个赎金信 (ransomNote) 字符串和一个杂志(magazine)字符串，判断 ransomNote 能不能由 magazines 里面的字符构成。
如果可以构成，返回 true ；否则返回 false 。magazine 中的每个字符只能在 ransomNote 中使用一次。

示例 1：
输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：
输入：ransomNote = "aa", magazine = "ab"
输出：false
示例 3：
输入：ransomNote = "aa", magazine = "aab"
输出：true
提示：
1 <= ransomNote.length, magazine.length <= 105
ransomNote 和 magazine 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ransom-note
'''

class Solution:
    def getDirt(self, cstring: str) -> dict: # 类方法，实现 input <string>, output <dict> = <字符:该字符在串中的重复次数>  
        str_dir = {key: cstring.count(key) for key in set(cstring)}
        return str_dir

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rN_dir, maga_dir = self.getDirt(ransomNote), self.getDirt(magazine)
        if (rN_dir.keys() - maga_dir.keys()): # 如果 ransomNote 中有字符不在 magazine 中，直接返回False
            return False
        else:
            matching_keys = rN_dir.keys() & maga_dir.keys() # 获取所有重复字符
            res_dir = {key: rN_dir[key] <= maga_dir[key] for key in matching_keys} # 获取 ransomNote 中重复字符的重复次数小于或等于 magazine 中的字符，类似真子集，
            if not res_dir.values() or False in res_dir.values(): # 如果真子集为空或者出现 False 即可判断不能由 magazines 里面的字符构成；反之可以
                return False
            else:
                return True

'''
执行结果：通过

执行用时：36 ms, 在所有 Python3 提交中击败了97.78%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了13.28%的用户
通过测试用例：126 / 126

官方解法：
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
'''