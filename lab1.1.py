def reverse_string(input_str):
    if len(input_str) == 0:
        return
    else:
        print(input_str[-1], end="")  # Друкуємо останній символ без переводу рядка
        reverse_string(input_str[:-1])  # Рекурсивно викликаємо функцію для решти рядка

# Приклад використання:
input_str = "tiger"
reverse_string(input_str)
