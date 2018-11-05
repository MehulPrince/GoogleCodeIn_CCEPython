for i in range(1, 11):
    print("GCI is great")
name = input('What is your name ? : ')

reverse_string = ""
for i in name:
    reverse_string = i + reverse_string
print('Hello ' + name + ' please to meet you! Did you know that your name backwards is ' + reverse_string)
