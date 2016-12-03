import random

def random_gen():
    random_number = random.randint(2**31,2**32)
    random_binary_str = format(random_number,'b')

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
    nums_list = lsb_loop(times)
    for i,j in nums_list:
        print 'b_'+str(len(nums_list)-nums_list.index((i,j)))+'|', i,'|', j
    return nums_list

def final_number(times):
    nums_list = print_nums(times)
    bits_list = []
    for i in range(len(nums_list)-1,-1,-1):
        bits_list.append(nums_list[i][1])
    number = 25*'0'+'1'
    for i in range(len(bits_list)-1,-1,-1):
        number = number + str(bits_list[i])
    number = number + '1'
    dec_final_number = int(number,2)
    return number, dec_final_number
# def main():
#     random_number = random_gen()
#     print random_number
#     lsb = extract_lsb(random_number)
#     print lsb
def main():
    pair_final_number = final_number(5)
    print 'Number' + '|', pair_final_number[1], '|' ,pair_final_number[0]


main()
