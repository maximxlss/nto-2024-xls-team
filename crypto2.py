from math import lcm
import time
from sage.all import EllipticCurve, Zmod, Integer, GF, crt, Integer, trial_division
from Crypto.Util.number import bytes_to_long, getPrime
from random import randrange
import json
import socket


def get():
    s = socket.socket()
    s.connect(("192.168.12.13", 1228))
    r1 = s.recv(100000).decode()
    s.sendall(b"get_task\n")
    r2 = s.recv(100000).decode().replace("'", '"')
    # print(r2)
    j = r2.splitlines()[-1]
    o = json.loads(j)

    p = o["p"]
    a = o["a"]
    b = o["b"]
    x = o["G.x"]
    E = EllipticCurve(Zmod(p), [a, b])
    G = E.lift_x(Integer(x))
    P = E(o["P.x"], o["P.y"])
    return p, E, G, P

def get_one_rem():
    p, E, G, P = get()
    print("got")
    gord = int(G.order())
    print("got order")
    factors = [] # [x for x, k in gord.factor() if x != 2]
    x = 10 ** 8
    while gord % x != 0:
        x -= 1
    factors.append(Integer(x))
    dlogs = []
    # print(factors)

    for fac in factors:
        if int(fac) > 10 ** 6:
            continue
        t = int(gord) // int(fac)
        dlog = (G * t).discrete_log(P * t)
        dlogs.append(dlog)

        print(dlog, fac)

    factors = factors[:len(dlogs)]

    x = crt(dlogs, factors)
    m = lcm(*factors)
    return Integer(x), Integer(m)

dlogs = []
factors = []

while lcm(*factors) < 2 ** 320:
    print(lcm(*factors))
    try:
        x, m = get_one_rem()
    except (TimeoutInterrupt, KeyboardInterrupt):
        print("killed")
        time.sleep(0.5)
        continue
    dlogs.append(x)
    factors.append(m)

    x = crt(dlogs, factors)

    with open("factors.txt", "w+") as f:
        f.write(f"({x}, {lcm(*factors)}),\n")

x = crt(dlogs, factors)

print(int(x).to_bytes(40, "big"))
