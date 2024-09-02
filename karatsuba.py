def left_shift(bin_str:str) -> str: return bin_str + '0'

def multiply_unitary_bits(bit_a:str, bit_b:str) -> str: return '0' if bit_a=='0' or bit_b=='0' else '1'

def flip_bit(bit:str) -> str: return '1' if bit=='0' else '0'

def adjust_zeros(x:str, y:str) -> list[str]:
    max_bin = max(len(x),len(y))
    return [x.zfill(max_bin), y.zfill(max_bin)]

def addition(x:str, y:str) -> str:
    x, y = adjust_zeros(x,y)
    return addition_aux(x,y,'0')


def addition_aux(x:str, y:str, carry:str) -> str:
    if not x and not y: return "" if carry=='0' else '1'
    if x[-1] == y[-1]: return addition_aux(x[:-1], y[:-1], x[-1]) + carry

    return addition_aux(x[:-1], y[:-1],carry) + flip_bit(carry)

def subtraction(x:str,y:str) -> str:
    x, y = adjust_zeros(x,y)
    flipped_y = ''.join(flip_bit(bit) for bit in y)
    complemented_y = addition(flipped_y,'1')
    
    result = addition(x, complemented_y)
    
    return result[1:]


print(subtraction('1010','0011'))
#print(print(subtraction('1100','0101')))
