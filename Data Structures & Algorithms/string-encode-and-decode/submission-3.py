class Solution:

    def encode(self, strs: List[str]) -> str:
        # strs = ["Hello","Wor#ld"]
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string
        # encoded_string = "5#Hello6#Wor#ld"
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            strs.append(s[j+1:j+length+1])
            i = j + 1 + length
        return strs

        
