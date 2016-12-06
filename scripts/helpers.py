def fast_exp(base, exp, modulus):
    y = 1
    binary_exp_str = "{0:b}".format(exp)

    for i in range(len(binary_exp_str)):
        y = y*y % modulus
        if binary_exp_str[i] == '1':
            y = (base*y) % modulus
    return y

def str_to_bin(string):
    binary_b = ''.join([bin(ord(letter)) for letter in string])
    binary = binary_b.translate(None, 'b')
    return binary

def int_to_str_length(number, length):
    number_str = format(number,'b')
    if len(number_str) < length:
        number_str = (length-len(number_str))*'0' + number_str
    return number_str

def fast_exp_trace(base, exp, modulus):
    y = 1
    binary_exp_str = "{0:b}".format(exp)
    matrix = "i |xi\t|y\t|y"
    for i in range(len(binary_exp_str)):
        y = y*y % modulus
        y_temp = y*y % modulus
        if binary_exp_str[i] == '1':
            y = (base*y) % modulus
            matrix = matrix + "\n%d |%s\t|%d\t|%d" %(len(binary_exp_str)-i-1, binary_exp_str[i], y_temp, y)
        else:
            matrix = matrix + "\n%d |%s\t|%d\t|%d" %(len(binary_exp_str)-i-1, binary_exp_str[i], y_temp, y)
    print matrix
    return y
