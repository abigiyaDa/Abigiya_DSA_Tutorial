class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]  
        temp = ""    

        for i in range(len(a)):
            current_char = a[i]  
            match = True
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != current_char:
                    match = False
                    break

            if match:
                temp += current_char
            else:
                break  

        return temp
