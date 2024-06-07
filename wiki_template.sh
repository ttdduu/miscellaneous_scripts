#!/usr/bin/zsh

if [ ! -s "$1.wiki" ]; then
	echo "Full title: __" >> "$1".wiki
	echo "Authors: " >> "$1".wiki
	echo "Extra: " >> "$1".wiki
else:
	true
fi

nvim "$1".wiki
