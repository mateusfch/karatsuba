def left_shift(bin_str:str) -> str: return bin_str + '0'

def multiply_bits(bit_a:str, bit_b:str) -> str: return '0' if bit_a=='0' or bit_b=='0' else '1'

def flip_carry(carry:str) -> str: return '1' if carry=='0' else '0'

def sum(x:str, y:str) -> str:
    if len(x)>len(y): y = '0' * (len(x) - len(y)) + y
    elif len(x)<len(y): x = '0' * (len(y) - len(x)) + x
    
    return sum_aux(x,y,'0')


def sum_aux(x:str, y:str, carry:str) -> str:
    if not x and not y: return "" if carry=='0' else '1'
    if x[-1] == y[-1]: return sum_aux(x[:-1], y[:-1], x[-1]) + carry

    return sum_aux(x[:-1], y[:-1],carry) + flip_carry(carry)



