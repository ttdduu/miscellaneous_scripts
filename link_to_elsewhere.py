#!/home/ttdduu/miniconda3/envs/pytom/bin/python3

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


def to_pdf():  # para los linkeados [[$papers/bla.pdf params|así]]
    if "|" in link_entero:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("|")]

        if " " in file:  # si metí params en el [[$papers/... x y z]]
            # Regex pattern splits on substrings "; " and ", "
            splits = re.split(" |\|", file)

            name = splits[0]
            page = splits[1]
            search = " ".join(splits[2:])
            print(search)
            os.system(f"sioyex {name} {page} {search}")

        else:
            os.system(f"st -e sw sioy {file} {1}")
    else:
        file = link_entero[link_entero.find("[") + 2 : link_entero.find("]")]

        if " " in file:  # si metí params en el [[$papers/... x y z]]
            # Regex pattern splits on substrings "; " and ", "
            splits = re.split(" |\|", file)

            name = splits[0]
            page = splits[1]
            search = splits[2]
            os.system(f"sioyex {name} {page} {search}")

        else:
            os.system(f"st -e sw sioy {file} {1}")


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


def session():
    file = link_entero[link_entero.find("[") + 2 : link_entero.find("]")]
    os.system(f"st -e nvim -S {file}")


def to_nvim():
    file = link_entero[link_entero.find("[") + 2 : link_entero.find("]")]
    os.system(f"st -e nvim {file}")


def to_sioyek(page=True):
    if page:
        """
        para líneas de texto tipo _quote del texto_ pagenumber

        """
        print(link_entero)
        search = str(link_entero[1 : link_entero.find("_", 1)])
        # params = link_entero[link_entero.find("_", 1) + 2 :].split(".")[0]
        # los últimos 5 caracteres son el ".wiki" que se agrega a la quote + pagenumber
        # en vim
        params = link_entero[link_entero.find("_", 1) + 2 : -5]
        # después de pagenumber quizá metí más texto para explicar o whatever; no me
        # interesa para esto.
        """
        osea puedo tener una estructura como esta:

        blabla _quote del df_ 134 por ende blablabla

        y que ande bien! xq al final de eso le appendeo el filename y lo único que
        quiero es el 1er elemento de params (el nro) y el último (el filename).
        lo imp es parar el cursor dentro de la quote que quiero, menos mal.
        En particular porque ahora puedo tener más de una quote en misma línea.
        """
        page, name = params.split(" ")[0], params.split(" ")[-1]
        print(params)
        page = int(page) + 1
        name = name + ".pdf"
        print(page)
        print(name)
        print(search)
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
    os.system(f'sioyex {name} {page} "{search}"')


# if "#" in link_entero:
# to_wiki()

# to_sioyek es para ir desde un _quote_ que está dentro del .wiki del .pdf en cuestión
"con N en vim tengo _search_ page name; name es el .wiki en el que estoy"
if ".md" in link_entero[-3:] and link_entero[0] == "_":
    index_post_search = link_entero.find("_", 1) + 3
    if link_entero[index_post_search - 1].isdigit():
        # if link_entero[0] != "_":
        to_sioyek()
    else:
        to_sioyek(page=False)

# para ir desde un [[*.pdf]] al pdf
if ".pdf" in link_entero:
    to_pdf()

if ".mks" in link_entero:
    session()

if "." not in link_entero[link_entero.rfind("/") + 1 :]:
    to_vifm()

if ".md" in link_entero and link_entero[0] != "_":
    to_nvim()

# TODO problemas cuando en _quote_ pagenumber [[link]] hay un [[link]] en la línea
if "https:" in link_entero and "[[" in link_entero[:2]:
    to_chrome()

if ".com" in link_entero and "[[" in link_entero[:2]:
    to_chrome()

if "www." in link_entero and "[[" in link_entero[:2]:
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

if ".doc" in link_entero:
    to_libre()

if ".odt" in link_entero:
    to_libre()

if ".png" in link_entero:
    to_sxiv()
