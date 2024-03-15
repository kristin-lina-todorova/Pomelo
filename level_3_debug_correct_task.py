def shift_digits(number):
    shift_value = 3
    shifted_number = ""
    for digit in str(number):
        shifted_digit = (int(digit) + shift_value) % 10
        shifted_number += str(shifted_digit)
        shift_value += 2
        
    return int(shifted_number)

original_number = 4387
shifted_number = shift_digits(original_number)
print(f"Original number: {original_number}")
print(f"Shifted number: {shifted_number}")
