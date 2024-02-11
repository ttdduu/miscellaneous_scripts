#!/home/ttdduu/miniconda3/envs/pytom/bin/python3

import pyperclip
import os

link_entero = pyperclip.paste()


def to_wiki():
    archivo, seccion = link_entero.split("#", 1)

    seccion = f"#{seccion}".replace(" ", "\ ")

    # todos los wiki files tienen que tener un TOC arriba para que esto funcione.

    os.system(f"st -e nvim +/{seccion} {archivo}")


def to_vifm():
    file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]

    os.system(f"st -e vifm --select {file}")


def to_pdf():
    file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]

    os.system(f"st -e sw okular {file}")


def to_libre():
    file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]

    os.system(f"st -e libreof {file}")


def to_chrome():
    file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]

    os.system(f'st -e sw google-chrome "{file}"')


def to_vlc():
    file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]

    os.system(f"st -e sw vlc {file}")


def to_sxiv():
    file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]

    os.system(f"st -e sw sxiv {file}")


def to_praat():
    file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]
    if " " in file:
        os.system(f"st -e sw praat --send $lsd/tesis/praat_vim.praat {file}")
    else:
        os.system(f"st -e sw praat --open {file}")


if "#" in link_entero:
    to_wiki()

if ".pdf" in link_entero:
    to_pdf()

if "https:" in link_entero:
    to_chrome()

if ".com" in link_entero:
    to_chrome()

if "www." in link_entero:
    to_chrome()

if ".mp3" in link_entero:
    to_vlc()

if ".mp4" in link_entero:
    to_vlc()

if ".mkv" in link_entero:
    to_vlc()

if ".wav" in link_entero:
    to_praat()

if ".docx" in link_entero:
    to_libre()

if ".doc|" in link_entero:
    to_libre()

if ".odt" in link_entero:
    to_libre()

if ".png" in link_entero:
    to_sxiv()

if "." not in link_entero[link_entero.rfind("/") + 1 :]:
    to_vifm()
