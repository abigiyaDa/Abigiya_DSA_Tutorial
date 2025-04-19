class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = defaultdict(int)

        for word in words:
            key = "".join(sorted(set(word)))  
            freq[key] += 1

        count = 0
        for val in freq.values():
            if val > 1:
                count += (val * (val - 1)) // 2  

        return count