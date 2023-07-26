import collections

class Solution(object):

    def encode_strings_SS(self, encode_str:str)-> str:

        answer = ""

        for word in encode_str:

            if word == ":":
                answer += word
                answer += "::;"

            else:
                answer += word
                answer += ":;"

        return answer[:-2]


    def decode_strings_SS(self, decode_str:str)-> str:

        answer = decode_str.split(":;")

        for i in range(len(answer)):
            if answer[i] == "::":
                answer[i] = ":"

        return answer



    def encode_strings_neat(self, encode_str:str)-> str:
        
        res = ""
        for s in encode_str:
            res += str(len(s)) + "#" + s
        return res

    def decode_strings_neat(self, decode_str:str)-> str:
        
        res, i = [], 0

        while i < len(decode_str):
            j = i
            while decode_str[j] != "#":
                j += 1
            length = int(decode_str[i:j])
            res.append(decode_str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


# Guide for solution:

# Htime complexity O(n).

### Golden rule: Split str with .split(). Using delimiter to separate.