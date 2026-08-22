#!/data/data/com.termux/files/usr/bin/sh

# =========================================================
# Dependências
# =========================================================

if ! command -v python >/dev/null 2>&1; then
    echo "Python não encontrado."
    pkg install python -y
fi

if ! command -v git >/dev/null 2>&1; then
    echo "Git não encontrado."
    pkg install git -y
fi


# =========================================================
# Instalação / atualização
# =========================================================

if [ -d "$HOME/.dish/.git" ]; then

    echo "Atualizando dish..."
    git -C "$HOME/.dish" pull

elif [ -d "$HOME/dish/termux_DS" ]; then

    echo "Migrando dish para .dish..."
    mv "$HOME/dish" "$HOME/.dish"

else

    echo "Baixando dish..."
    git clone https://github.com/redbluezin/dish "$HOME/.dish"

fi


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
