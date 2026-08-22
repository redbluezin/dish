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
print(mb.stderr)fi


# =========================================================
# .dishrc
# =========================================================

DISHRC="$HOME/.dishrc"

cat > "$DISHRC" <<'EOF'
# Dish configuration

dish() {
    python "$HOME/.dish/termux_DS/dish.py" "$@"
}
EOF


# =========================================================
# .profile
# =========================================================

PROFILE="$HOME/.profile"

if [ ! -f "$PROFILE" ]; then
    touch "$PROFILE"
fi

if ! grep -qF '. "$HOME/.dishrc"' "$PROFILE"; then
    cat >> "$PROFILE" <<'EOF'

# Load Dish configuration
if [ -f "$HOME/.dishrc" ]; then
    . "$HOME/.dishrc"
fi
EOF
fi


# =========================================================
# Carregar imediatamente
# =========================================================

. "$DISHRC"


echo ""
echo "dish instalado com sucesso! 🐟"
echo ""
echo "Executável:"
echo "$HOME/.dish/termux_DS/dish.py"
echo ""
echo "O comando 'dish' já está disponível!"
