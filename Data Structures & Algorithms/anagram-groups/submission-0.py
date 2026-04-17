class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            print(f"sorted_word = {sorted_word}")
            anagrams[sorted_word].append(word)
            print(f"anagrams[sorted_word] = {anagrams[sorted_word]}")
            print(f"anagrams.keys() = {anagrams.keys()}")
            print(f"anagrams.values() = {anagrams.values()}")
            print(f"anagrams {anagrams} \n -----------------------\n")

        return list(anagrams.values())