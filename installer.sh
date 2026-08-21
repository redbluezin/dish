#!/data/data/com.termux/files/usr/bin/sh

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

grep -q '^dish() {' "$HOME/.bashrc" || \
echo 'dish() { python "$HOME/.dish/dish.py" "$@"; }' >> "$HOME/.bashrc"

echo "dish instalado com sucesso! 🐟"
echo "Reinicie o Termux para usar o comando 'dish'."
