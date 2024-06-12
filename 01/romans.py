def int_to_roman(num):
    int_for_roman = { 
        1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I" 
    }

    roman_num = ''
    
    for value in sorted(int_for_roman.keys(), reverse=True):
        while num >= value:
            roman_num += int_for_roman[value]
            num -=value

    return roman_num
num = 1994
variavel = int_to_roman(num)
print (variavel)


