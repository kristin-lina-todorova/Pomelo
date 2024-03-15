def shift_digits(number):
    shift_value = 3
    shifted_number = ""
    for digit in str(number):
        #correct -> shifted_digit = (int(digit) + shift_value) % 10
        #wrong -> shifted_digit = digit + shift_value % 10
        shifted_digit = digit + shift_value % 10
        #correct -> shifted_number += str(shifted_digit)
        #wrong -> shifted_digit += str(shifted_digit)
        shifted_digit += str(shifted_digit)
        #correct -> shift_value += 2
        #wrong -> shift_value += 4
        shift_value += 4
        
    return int(shifted_number)

original_number = 4387
#correct -> shifted_number = shift_digits(original)
#correct -> shifted_number = shift_number(original)
shifted_number = shift_number(original_number)
print(f"Original number: {original_number}")
print(f"Shifted number: {shifted_number}")
