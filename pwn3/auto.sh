nasm shellcode_inner.asm   
python main.py > shellcode.asm
nasm shellcode.asm
python print_shellcode.py
cat shellcode.txt