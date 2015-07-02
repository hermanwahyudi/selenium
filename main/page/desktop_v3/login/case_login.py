import string, random

chara = string.ascii_lowercase+string.digits

def validate_1(size=8):
    string_val1_1 = ''.join(random.choice(chara) for i in range(size))
    joined_alpha_val1 = string_val1_1
    return joined_alpha_val1

print (validate_1())

def validate_2(size=8):
    string_val2_1 = ''.join(random.choice(chara) for i in range (size))
    string_val2_2 = ''.join(random.choice(chara) for i in range(6))
    joined_alpha_val2 = string_val2_1 + '@' +string_val2_2
    return joined_alpha_val2

print (validate_2())

def validate_3(size=8):
    string_val3_1 = ''.join(random.choice(chara) for i in range(size))
    string_val3_2 = ''.join(random.choice(chara) for i in range(6))
    joined_alpha_val3 = '@' + string_val3_1 + '.com'
    return joined_alpha_val3

print (validate_3())