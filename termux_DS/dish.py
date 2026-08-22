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
# Instalação / atualização
# =========================================================

if [ -d "$HOME/.dish/.git" ]; then

    echo "Atualizando dish..."
    git -C "$HOME/.dish" pull

elif [ -d "$HOME/dish/termux_DS/.git" ]; then

    echo "Migrando dish para .dish..."

    mv "$HOME/dish" "$HOME/.dish"

else

    echo "Baixando dish..."

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
