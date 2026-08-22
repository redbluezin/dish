#!/data/data/com.termux/files/usr/bin/sh

echo "Instalando dependências..."
pkg install python git -y

if [ -d "$HOME/.dish/.git" ]; then
    echo "Atualizando dish..."
    git -C "$HOME/.dish" pull

elif [ -d "$HOME/dish/.git" ]; then
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

if [ ! -f "$DISHRC" ]; then
    echo "Criando .dishrc..."

    cat > "$DISHRC" <<'EOF'
# Dish configuration

dish() {
    python "$HOME/.dish/dish.py" "$@"
}
EOF

else
    # Garante que o comando dish exista no .dishrc
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

# Carrega o .dishrc automaticamente
if ! grep -q 'HOME/.dishrc' "$PROFILE"; then
    cat >> "$PROFILE" <<'EOF'

# Load Dish configuration
if [ -f "$HOME/.dishrc" ]; then
    . "$HOME/.dishrc"
fi
EOF
fi


# =========================================================
# Carregar imediatamente nesta sessão
# =========================================================

. "$DISHRC"


echo ""
echo "dish instalado com sucesso! 🐟"
echo ""
echo "O .dishrc foi criado em:"
echo "$DISHRC"
echo ""
echo "O comando 'dish' já está disponível nesta sessão."
echo "Nas próximas sessões, o .dishrc será carregado automaticamente."
