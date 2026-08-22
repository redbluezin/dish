import subprocess as sp
import os, sys

if len(sys.argv) >= 2 :
    with open(f"{os.getcwd()}/{sys.argv[1]}","r") as rl :
        mx = rl.read()
else :
    raise ValueError("dish: erro, formatação Invalida")

mx = mx.split("\n")
hh = sys.argv[1:]

for vn, ps in enumerate(mx) :
    if ps.startswith("import") :
        vf = ps.split()[1]
        if "/" in vf:
            with open(vf, "r") as r :
                vm = r.read()
        else :
            with open(f"/storage/emulated/0/testes/tu2/{vf}", "r") as r :
                vm = r.read()
        mx[vn] = f"{vm}\n"
    else :
        mx[vn] = ps+"\n"

p = "".join(mx)
mb = sp.run(["sh","-c", p, *hh], capture_output=True, text=True)

print(mb.stdout)
print(mb.stderr)
