import random

def random_gen():
    random_number = random.randint(1,2**32)
    random_binary_str = format(random_number,'b')
    if len(random_binary_str) < 32:
        random_binary_str = (32-len(random_binary_str))*'0' + random_binary_str

    return random_binary_str

def extract_lsb(binary_str):
    lsb = binary_str[-1]

    return lsb

def lsb_loop(times):
    numbers = []
    bits = []
    for i in range(times):
        random_binary = random_gen()
        lsb = extract_lsb(random_binary)
        numbers.append(random_binary)
        bits.append(lsb)
    return zip(numbers, bits)

def print_nums(times):
    digits = []
    nums_list = lsb_loop(times)
    for i,j in nums_list:
        temp_str = 'b_%s|%s|%s'%(str(len(nums_list)-nums_list.index((i,j))), i, j)
        digits.append(temp_str)
    return nums_list, digits

def final_number(times):
    temp_list = print_nums(times)
    nums_list = temp_list[0]
    digits = temp_list[1]
    bits_list = []
    for i in range(len(nums_list)-1,-1,-1):
        bits_list.append(nums_list[i][1])
    number = 25*'0'+'1'
    for i in range(len(bits_list)-1,-1,-1):
        number = number + str(bits_list[i])
    number = number + '1'
    dec_final_number = int(number,2)
    return number, dec_final_number, digits
