#!/usr/bin/zsh

# abrir el mks del calendario con el brain dump
#st -e bspc desktop -f 9 && st -e nvim -S $todo/calendario_con_brain_dump.mks

# solo el calendario como haría un neurotípico
st -e bspc desktop -f 9 && st -e nvim $cal/calendario.wiki
