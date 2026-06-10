class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grams = {}

        for s in strs:
            freq = [0] *26
            for i in s:
                freq[ord(i)-97] +=1
            key = tuple(freq)
            if grams.get(key) is None:
                grams[key] = []
                grams[key].append(s)
            else:
                grams[key].append(s)
                
        return list(grams.values())

