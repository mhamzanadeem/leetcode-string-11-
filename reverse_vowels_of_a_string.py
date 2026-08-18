class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = 'aeiouAEIOU'
        choosen_letters= []
        for char in s:
            if char in vowels: 
                choosen_letters.append(char)

        choosen_letters.reverse()

        result = []

        for char in s:
            if char in vowels: 
                result.append(choosen_letters.pop(0))
            else:
                result.append(char)

        return "".join(result)


