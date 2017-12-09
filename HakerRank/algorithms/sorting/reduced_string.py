line = input()

def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part

count = 0
while count < len(line) - 1:
    if line[count] == line[count + 1]:
        line = line[:count] + line[count + 2:]
        count = -1
    count += 1

if line is not str():
    print(line)
else:
    print("Empty String")