
with open("shellcode_inner", "rb") as f:
    text = f.read()


# chunks = []

# for i in range(0, len(text) + 1, 8):
#     chunks.append(text[i:i + 8])

# chunks.reverse()

print("""BITS 64
push rax
nop
""")

i = 0
for c in text:
    print(f"mov bl, 0x{c:02x}")
    print("mov byte [rax], bl")
    new_i = i + 1
    delta = i ^ new_i
    print(f"xor al, 0x{delta:02x}")
    i = new_i

print("""ret
nop
""")

