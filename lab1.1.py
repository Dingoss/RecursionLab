def reverse_string(input_str):
    if len(input_str) == 0:
        return
    else:
        print(input_str[-1], end="")  
        reverse_string(input_str[:-1])  

input_str = "tiger"
reverse_string(input_str)
