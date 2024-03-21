bits 64

cld
mov rcx, 128
mov rdi, rax
lea rsi, [rbp + 0x9c]
rep movsd
jmp rax

