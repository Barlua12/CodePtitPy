def convert_base(N,b):
    if N==0:
        return '0'
    digits=     "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # digits =    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=''
    while N>0:
        convert_b=N%b
        result=digits[convert_b]+result
        N//=b
    return result

