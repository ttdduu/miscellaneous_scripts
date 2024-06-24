#!/usr/bin/zsh

# la idea con esto es que por defecto los tts de naver-papago sean 0.5 speed porque van a los pedos. pero en anki puedo incluir el speed original tmb si la frase es muy corta; me quedaría algo así:
# Seriez-vous prêt à m'aider [sound:fast-naver-3b953062-c4af5d2c-a17e563c-da2d23c0-ef7175d3.mp3] [sound:naver-3b953062-c4af5d2c-a17e563c-da2d23c0-ef7175d3.mp3]
# en ese caso, el sound con fast- lo incluí a mano, pero por defecto tendré solo el "normal" que en realidad corriendo este script será el 0.5

# Define the directory containing the mp3 files
#directory=~/.local/share/Anki2/addons21/1436550454/user_files/cache # este no es el modificado, pero existe y no sé para qué se usa
directory=~/.local/share/Anki2/ttdduu/collection.media

# Loop through all files in the directory
for filepath in "$directory"/*.mp3; do
    filename=$(basename "$filepath")

    # Check if the file does not already have the "fast-" prefix
    if [[ ! $filename == fast-* ]]; then
        fast_filename="fast-$filename"
        fast_filepath="$directory/$fast_filename"

        # Check if the file has already been processed
        if [[ ! -f $fast_filepath ]]; then
            # Rename the original file to "fast-rootname.mp3"
            mv "$filepath" "$fast_filepath"

            # Process the file with sox and save it with the original filename
            sox "$fast_filepath" "$filepath" tempo -s 0.5
            echo "Processed $filename -> $filename (slowed down) and $fast_filename (original)"
        else
            echo "Skipping $filename, $fast_filename already exists"
        fi
    fi
done
