class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashMap = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        output = []
        for digit in digits:
            tmp = list()
            if len(output) == 0:
                tmp = hashMap[digit]
            else:
                for e in output:
                    for ch in hashMap[digit]:
                        tmp.append(e+ch)
            output = tmp
        return output