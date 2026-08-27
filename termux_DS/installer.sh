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
# Comando dish
# =========================================================

DISH="$PREFIX/bin/dish"

cat > "$DISH" <<'EOF'
#!/data/data/com.termux/files/usr/bin/sh

exec python "$HOME/.dish/termux_DS/dish.py" "$@"
EOF

chmod +x "$DISH"


# =========================================================
# .dishrc
# =========================================================

DISHRC="$HOME/.dishrc"

# Nunca sobrescrever um .dishrc existente.
# Se não existir, apenas cria um arquivo vazio.
if [ ! -f "$DISHRC" ]; then
    touch "$DISHRC"
fi


# =========================================================
# Remover função dish() antiga do .dishrc
# =========================================================

TMP="$DISHRC.tmp"

awk '
BEGIN {
    removing = 0
}

# Início da antiga função dish()
/^[[:space:]]*dish[[:space:]]*\(\)[[:space:]]*\{/ {
    removing = 1
    next
}

# Fim da antiga função
removing && /^[[:space:]]*}[[:space:]]*$/ {
    removing = 0
    next
}

# Ignora tudo que estiver dentro da função antiga
removing {
    next
}

{
    print
}
' "$DISHRC" > "$TMP"

mv "$TMP" "$DISHRC"


# =========================================================
# .profile
# =========================================================

PROFILE="$HOME/.profile"

if [ ! -f "$PROFILE" ]; then
    touch "$PROFILE"
fi

# Garante que .dishrc seja carregado pelo .profile.
if ! grep -qF '. "$HOME/.dishrc"' "$PROFILE"; then
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
# Resultado
# =========================================================

echo ""
echo "dish instalado com sucesso! 🐟"
echo ""
echo "Comando:"
echo "$DISH"
echo ""
echo "Script:"
echo "$HOME/.dish/termux_DS/dish.py"
echo ""
echo "Configuração:"
echo "$DISHRC"
echo ""

if command -v dish >/dev/null 2>&1; then
    echo "O comando 'dish' já está disponível! 🚀"
else
    echo "Aviso: 'dish' não foi encontrado no PATH."
fi

echo ""fi


# =========================================================
# Arquivo do comando
# =========================================================

DISH="$PREFIX/bin/dish"

cat > "$DISH" <<'EOF'
#!/data/data/com.termux/files/usr/bin/sh

exec python "$HOME/.dish/termux_DS/dish.py" "$@"
EOF

chmod +x "$DISH"


# =========================================================
# .dishrc
# =========================================================

DISHRC="$HOME/.dishrc"

cat > "$DISHRC" <<'EOF'
# Dish configuration

# O comando principal do Dish fica em:
# $PREFIX/bin/dish

# Este arquivo existe para futuras configurações do Dish.
EOF


# =========================================================
# Limpeza do .profile antigo
# =========================================================

PROFILE="$HOME/.profile"

if [ -f "$PROFILE" ]; then

    # Remove o bloco antigo que carregava o .dishrc.
    # Mantém o restante do .profile intacto.
    TMP="$PROFILE.dish.tmp"

    awk '
    /^# Load Dish configuration$/ {
        skip=1
        next
    }

    skip && /^fi$/ {
        skip=0
        next
    }

    !skip {
        print
    }
    ' "$PROFILE" > "$TMP"

    mv "$TMP" "$PROFILE"
fi


# =========================================================
# Remover função dish antiga do .dishrc antigo
# =========================================================

# Caso exista alguma definição antiga da função dish
# em outro arquivo, ela não será mais necessária.
# O comando real agora é $PREFIX/bin/dish.


# =========================================================
# Verificação
# =========================================================

echo ""
echo "dish instalado com sucesso! 🐟"
echo ""

echo "Comando:"
echo "$DISH"

echo ""
echo "Script:"
echo "$HOME/.dish/termux_DS/dish.py"

echo ""

if command -v dish >/dev/null 2>&1; then
    echo "O comando 'dish' já está disponível! 🚀"
else
    echo "Aviso: 'dish' não foi encontrado no PATH."
fi

echo ""fi


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
