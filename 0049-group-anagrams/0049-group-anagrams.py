class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagram strings are after sorting the same 
        mp ={}
        #for i, s in enumerate(strs):
        for s in strs:
            f=str(sorted(s))
            if f not in mp:
                mp[f]=[]
            mp[f].append(s)
        return list(mp.values())
        