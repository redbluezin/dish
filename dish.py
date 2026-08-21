import subprocess as sp
import os, sys

if len(sys.argv) == 2 :
    with open(sys.argv[1],"r") as rl :
        mx = rl.read()
else :
    raise ValueError("dish: erro, formatação Invalida")

mx = mx.split("\n")
hh = sys.argv[1:]
print(hh)

for vn, ps in enumerate(mx) :
    if ps.startswith("import") :
        vf = ps.split()[1]
        with open(f"/storage/emulated/0/testes/tu2/{vf}", "r") as r :
            vm = r.read()
        mx[vn] = f"{vm}\n"
    else :
        mx[vn] = ps+"\n"

p = "".join(mx)
print(p)
mb = sp.run(["sh","-c", p, *hh], capture_output=True)

print(mb.stdout)
print(mb.stderr)
