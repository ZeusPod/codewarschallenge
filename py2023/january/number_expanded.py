#write a number in expanded form 

def expanded_form(number):
    num_str = str(number)
    num_len = len(num_str)
    expanded_nums = []
    for i in range(num_len):
        if num_str[i] != '0':
            expanded_nums.append(num_str[i] + '0'*(num_len-i-1))
    return ' + '.join(expanded_nums)

print(expanded_form(32030))
    
