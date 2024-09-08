import sys

def left_shift(x:str, shifts:int) -> str: return x + '0' * shifts

def flip_bit(bit: str) -> str: return '1' if bit == '0' else '0'

def divide_string(x:str) -> tuple[str, str]: return x[:len(x)//2], x[len(x)//2:]

def multiply_unitary_bits(x:str, y:str) -> str: return '0' if x=='0' or y=='0' else '1'

def adjust_zeros(x: str, y: str) -> tuple[str, str]:
    max_len = max(len(x), len(y))
    return x.zfill(max_len), y.zfill(max_len)

def addition(x: str, y: str) -> str:
    x, y = adjust_zeros(x, y)
    return addition_aux(x, y, '0')

def addition_aux(x:str, y:str, carry:str) -> str:
    if not x and not y: return '' if carry=='0' else '1'
    if x[-1] == y[-1]: return addition_aux(x[:-1], y[:-1], x[-1]) + carry

    return addition_aux(x[:-1], y[:-1],carry) + flip_bit(carry)

def subtraction(x: str, y: str) -> str:
    x, y = adjust_zeros(x, y)
    flipped_y = ''.join(flip_bit(bit) for bit in y)
    complemented_y = addition(flipped_y, '1')
    
    result = addition(x, complemented_y)
        
    return result[1:] if len(result) > len(x) else result

def karatsuba_step(x: str, y: str) -> str:
    x, y = adjust_zeros(x, y)
    return karatsuba_step_aux(x, y).lstrip('0')

def karatsuba_step_aux(x: str, y: str) -> str:
    if len(x) != len(y): x, y = adjust_zeros(x, y)
    if len(x) == 1: return multiply_unitary_bits(x, y)
    
    n = len(x)
    m = n // 2

    xl, xr = divide_string(x)
    yl, yr = divide_string(y)

    ac = karatsuba_step_aux(xl, yl)
    bd = karatsuba_step_aux(xr, yr)
    abcd = karatsuba_step_aux(addition(xl, xr), addition(yl, yr))
    ad_plus_bc = subtraction(abcd, addition(ac, bd))
    
    return addition(addition(left_shift(ac, 2 * (n-m)), left_shift(ad_plus_bc, n-m)), bd)
    
def check_result(x:str, y:str)-> bool: return karatsuba_step(x,y) == bin(int(x,2) * int(y,2))[2:]

def main(): print(karatsuba_step(sys.argv[1], sys.argv[2])) if len(sys.argv) == 3 else print("Please provide two binary numbers to multiply")

if __name__ == "__main__": main()