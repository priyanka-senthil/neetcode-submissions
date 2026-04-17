class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
                # print(count)

            # After building count for this word
            print(f"Word: {s}, Count: {count}")   # 👈 debug print
            res[tuple(count)].append(s)
            print(f"res so far: {dict(res)}\n")   # 👈 debug print
            
        return list(res.values())