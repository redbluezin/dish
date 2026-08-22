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

elif [ -d "$HOME/dish/termux_DS/.git" ]; then

    echo "Migrando dish para .dish..."
    mv "$HOME/dish/termux_DS" "$HOME/.dish"

elif [ -d "$HOME/dish/termux_DS" ]; then

    echo "Encontrada instalação antiga do dish."
    echo "Migrando para .dish..."

    mv "$HOME/dish/termux_DS" "$HOME/.dish"

else

    echo "Baixando dish..."

    git clone https://github.com/redbluezin/dish "$HOME/.dish"

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
    python "$HOME/.dish/dish.py" "$@"
}
EOF

else

    if ! grep -q '^dish() {' "$DISHRC"; then

        cat >> "$DISHRC" <<'EOF'

dish() {
    python "$HOME/.dish/dish.py" "$@"
}
EOF

    fi

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
# Carregar imediatamente
# =========================================================

. "$DISHRC"


echo ""
echo "dish instalado com sucesso! 🐟"
echo ""
echo "O .dishrc está em:"
echo "$DISHRC"
echo ""
echo "O comando 'dish' já está disponível!"
