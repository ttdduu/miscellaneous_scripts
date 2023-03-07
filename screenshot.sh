#!/bin/zsh
# copiar a clipboard:
st -e maim -s | xclip -selection clipboard -t image/png

# savear:
cd ~/media/screenshots    # Change to the directory where you want to save the screenshots
filename="myscreenshot1.png"    # Set the default filename
if [[ -e "$filename" ]]; then   # If the file already exists
    i=2
    while [[ -e "myscreenshot$i.png" ]]; do    # Increment the number until a unique filename is found
        let i++
    done
    filename="myscreenshot$i.png"    # Set the new filename
fi
maim -s "$filename"    # Capture the screenshot and save it with the new filename
