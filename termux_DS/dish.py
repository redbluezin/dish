#!/data/data/com.termux/files/usr/bin/sh

# =========================================================
# Dependências
# =========================================================

if ! command -v python >/dev/null 2>&1; then
    echo "Python não encontrado."
    echo "Instalando Python..."
    pkg install python -y
fi

if ! command -v git >/dev/null 2>&1; then
    echo "Git não encontrado."
    echo "Instalando Git..."
    pkg install git -y
fi


# =========================================================
# Instalação / atualização do Dish
# =========================================================

if [ -d "$HOME/.dish/.git" ]; then

    echo "Atualizando dish..."
    git -C "$HOME/.dish" pull

elif [ -d "$HOME/dish/termux_DS" ]; then

    echo "Migrando dish para .dish..."

    if [ ! -d "$HOME/.dish" ]; then
        mv "$HOME/dish" "$HOME/.dish"
    else
        mv "$HOME/dish/termux_DS" "$HOME/.dish/termux_DS"
        rmdir "$HOME/dish" 2>/dev/null
    fi

else

    echo "Baixando dish..."

    git clone https://github.com/redbluezin/dish "$HOME/.dish"

fi


# =========================================================
# Procurar termux_DS
# =========================================================

DISH=""

if [ -f "$HOME/.dish/termux_DS/dish.py" ]; then

    DISH="$HOME/.dish/termux_DS/dish.py"

else

    echo "Procurando termux_DS..."

    DISH=$(find "$HOME/.dish" -type f -path '*/termux_DS/dish.py' 2>/dev/null | head -n 1)

fi


# =========================================================
# Verificar se encontrou
# =========================================================

if [ -z "$DISH" ] || [ ! -f "$DISH" ]; then

    echo ""
    echo "ERRO: não foi possível encontrar termux_DS/dish.py!"
    echo ""
    echo "Estrutura encontrada em:"
    echo "$HOME/.dish"
    echo ""

    exit 1

fi


echo "Dish encontrado em:"
echo "$DISH"


# =========================================================
# .dishrc
# =========================================================

DISHRC="$HOME/.dishrc"

echo "Configurando .dishrc..."


# Cria .dishrc se não existir
if [ ! -f "$DISHRC" ]; then
    touch "$DISHRC"
fi


# Remove uma função dish antiga.
# Isso também remove a versão que apontava
# para ~/.dish/dish.py.
TMP="$DISHRC.tmp"

awk '
BEGIN {
    skip = 0
}

# Início da função dish
/^dish[[:space:]]*\(\)[[:space:]]*\{/ {
    skip = 1
    next
}

# Final da função dish
skip && /^[[:space:]]*\}/ {
    skip = 0
    next
}

!skip {
    print
}
' "$DISHRC" > "$TMP"

mv "$TMP" "$DISHRC"


# Adiciona a função correta
cat >> "$DISHRC" <<EOF

dish() {
    python "$DISH" "\$@"
}
EOF


# =========================================================
# .profile
# =========================================================

PROFILE="$HOME/.profile"

if [ ! -f "$PROFILE" ]; then
    touch "$PROFILE"
fi


if ! grep -q 'HOME/.dishrc' "$PROFILE"; then

    cat >> "$PROFILE" <<'EOF'

# Load Dish configuration
if [ -f "$HOME/.dishrc" ]; then
    . "$HOME/.dishrc"
fi
EOF

fi


# =========================================================
# Carregar .dishrc imediatamente
# =========================================================

. "$DISHRC"


# =========================================================
# Final
# =========================================================

echo ""
echo "================================"
echo " dish instalado com sucesso! 🐟"
echo "================================"
echo ""
echo "Executável:"
echo "$DISH"
echo ""
echo ".dishrc:"
echo "$DISHRC"
echo ""
echo "Comando 'dish' disponível!"    echo "Baixando dish..."

    git clone https://github.com/redbluezin/dish "$HOME/.dish"

fi


# =========================================================
# Verificar Dish
# =========================================================

DISH="$HOME/.dish/termux_DS/dish.py"

if [ ! -f "$DISH" ]; then
    echo ""
    echo "ERRO: dish.py não encontrado!"
    echo "Esperado em:"
    echo "$DISH"
    exit 1
fi


# =========================================================
# .dishrc
# =========================================================

DISHRC="$HOME/.dishrc"

if [ ! -f "$DISHRC" ]; then

    echo "Criando .dishrc..."

    cat > "$DISHRC" <<'EOF'
# Dish configuration

dish() {
    python "$HOME/.dish/termux_DS/dish.py" "$@"
}
EOF

elif ! grep -q '^dish() {' "$DISHRC"; then

    cat >> "$DISHRC" <<'EOF'

dish() {
    python "$HOME/.dish/termux_DS/dish.py" "$@"
}
EOF

fi


# =========================================================
# .profile
# =========================================================

PROFILE="$HOME/.profile"

if [ ! -f "$PROFILE" ]; then
    touch "$PROFILE"
fi

if ! grep -q 'HOME/.dishrc' "$PROFILE"; then

    cat >> "$PROFILE" <<'EOF'

# Load Dish configuration
if [ -f "$HOME/.dishrc" ]; then
    . "$HOME/.dishrc"
fi
EOF

fi


# =========================================================
# Carregar .dishrc agora
# =========================================================

. "$DISHRC"


echo ""
echo "dish instalado com sucesso! 🐟"
echo ""
echo "Dish: $HOME/.dish/termux_DS"
echo ".dishrc: $DISHRC"
echo ""
echo "O comando 'dish' já está disponível!"
