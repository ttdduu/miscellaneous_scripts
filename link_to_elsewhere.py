#!/home/ttdduu/miniconda3/envs/pytom-sioyek/bin/python3

import pyperclip
import os
import re
import subprocess

link_entero = pyperclip.paste()


def to_wiki():
    archivo, seccion = link_entero.split("#", 1)

    seccion = f"#{seccion}".replace(" ", "\ ")

    # todos los wiki files tienen que tener un TOC arriba para que esto funcione.

    os.system(f"st -e nvim +/{seccion} {archivo}")


def to_vifm():
    if "|" in link_entero:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]
    elif "[" in link_entero:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("]")]
    else:
        file = link_entero

    os.system(f"st -e vifm --select {file}")


def to_pdf():
    if "|" in link_entero:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]
    else:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("]")]

    if " " in file:  # si metí params en el [[$papers/... x y z]]
        # Regex pattern splits on substrings "; " and ", "
        splits = re.split(" |\|", file)

        name = splits[0]
        page = splits[1]
        search = splits[2]
        print(name)
        print(page)
        print(search)
        os.system(f"siokex {name} {page} {search}")

    else:
        os.system(f"st -e sw siok {file}")


def to_libre():
    if "|" in link_entero:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]
    else:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("]")]

    os.system(f"st -e libreof {file}")


def to_chrome():
    if "|" in link_entero:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]
    else:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("]")]

    os.system(f'st -e sw google-chrome "{file}"')


def to_vlc():
    if "|" in link_entero:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]
    else:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("]")]

    os.system(f"st -e sw vlc {file}")


def to_sxiv():
    if "|" in link_entero:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]
    else:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("]")]

    os.system(f"st -e sw sxiv {file}")


def to_praat():
    file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]
    if " " in file:
        os.system(f"st -e sw praat --send $lsd/tesislab/praat_vim.praat {file}")
    else:
        os.system(f"st -e sw praat --open {file}")


def to_sioyek(page=True):
    if page:
        """
        para líneas de texto tipo '_quote del texto_ pagenumber'

        """
        search = str(link_entero[1 : link_entero.find("_", 1)])
        params = link_entero[link_entero.find("_", 1) + 2 :].split(".")[0]
        page, name = params.split(" ")
        page = int(page[:-1]) + 1
        name = name + ".pdf"
    if page == False:
        """
        para líneas de texto 'Full Title: _cortical connections blabla_ filename.wiki'
        """
        start_search = link_entero.find("_", 0)
        end_search = link_entero.find("_", start_search + 1)  # arranca a buscar desde 1
        search = str(link_entero[start_search + 1 : end_search])
        page = 1
        name = (
            link_entero[end_search + 2 : link_entero.find(".", end_search + 2)] + ".pdf"
        )
        print(name)
        print(page)
        print(search)

    os.system(f'siokex {name} {page} "{search}"')


# if "#" in link_entero:
# to_wiki()

"con N en vim tengo _search_ page name; name es el .wiki en el que estoy"
if ".wiki" in link_entero:
    if "#" not in link_entero:
        if link_entero[0] != "_":
            to_sioyek(page=False)
        else:
            to_sioyek()

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
