class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        output = ''

        if ((numerator > 0) and (denominator > 0)) or ((numerator < 0) and (denominator < 0)):
            output += ''
        else:
            output += '-'

        numerator, denominator = abs(numerator), abs(denominator)
        
        integer = numerator // denominator
        remainder = numerator % denominator
        if remainder == 0:
            output += str(integer)
            return output
        else:
            output += str(integer) + '.'
            remainder_pos = {remainder: len(output)}
        while True:
            div = (remainder * 10) // denominator
            remainder = (remainder * 10) % denominator
            output += str(div)
            if remainder == 0:
                return output
            if remainder not in remainder_pos:
                remainder_pos[remainder] = len(output)
            else:
                pos = remainder_pos[remainder]
                output = output[:pos] + '(' + output[pos:] + ')'
                return output