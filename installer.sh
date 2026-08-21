#!/data/data/com.termux/files/usr/bin/bash

pkg install python git -y

if [ -d "$HOME/.dish/.git" ]; then
    echo "Atualizando dish..."
    git -C "$HOME/.dish" pull

elif [ -d "$HOME/dish/.git" ]; then
    echo "Migrando dish para .dish..."
    mv "$HOME/dish" "$HOME/.dish"

else
    echo "Baixando dish..."
    git clone https://github.com/redbluezin/dish/dish.py "$HOME/.dish"
fi

grep -q '^dish() {' "$HOME/.bashrc" || \
echo 'dish() { exec python "$HOME/.dish/dish.py" "$@"; }' >> "$HOME/.bashrc"

source "$HOME/.bashrc"

echo "dish instalado com sucesso! 🐟"
