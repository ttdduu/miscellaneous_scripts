#!/usr/bin/zsh

sudo apt update
sudo apt upgrade
cp ~/.zsh_history /home/ttdduu/dotfiles/historial_bkp_semanal.txt
echo 'empezando backups'

echo "######################################### nvim plugins"
nvim --headless +PlugUpdate +qall

# .vim a dotfiles
echo "######################################### .vim a dotfiles"
rsync -av "$HOME/.vim/my-snippets" "$HOME/dotfiles/home/.vim/"
rsync -av "$HOME/.vim/autoload" "$HOME/dotfiles/home/.vim/"

dropbox start

# {{{ repos=("/home/ttdduu/code/miscellaneous_scripts" "/home/ttdduu/dotfiles")


echo "######################################### repos"

# Define the commit message
commit_message="Automatic weekly commit message"

# List of repositories
repos=("/home/ttdduu/code/miscellaneous_scripts" "/home/ttdduu/dotfiles")

# Function to add, commit, and push changes if there are uncommitted changes
function commit_and_push {
  local repo=$1
  echo "######################################### Processing repository: $repo"

  # Change to the repository directory
  cd "$repo" || { echo "Failed to change directory to $repo"; return; }

  # Check if there are uncommitted changes
  if [[ -n $(git status --porcelain) ]]; then
    echo "Uncommitted changes found. Adding, committing, and pushing..."

    # Add changes
    git add -A

    # Commit changes
    git commit -m "$commit_message"

    # Push changes
    git push origin main # Adjust the branch name if necessary
  else
    echo "No uncommitted changes found."
  fi

  # Change back to the original directory
  cd - || { echo "Failed to change back to the original directory"; exit 1; }
}

# Commit and push changes for each repository
for repo in "${repos[@]}"
do
  commit_and_push "$repo"
  echo "######################################### commit $repo"
done
# }}}

# {{{ rsync a sd externo y tablet y iph y a dotfiles

dirs_para_sd=(
    "$HOME/wiki"
    "$HOME/media"
    "$HOME/pdfs"
	"$HOME/documentacion_y_burocracia"
    # Add more directories as needed
)

if [ -z "$(ls -A "$sd")" ]; then
	echo "el dir de sd está vacío"
else
	for dir in "${dirs_para_sd[@]}"; do
		echo "######################################### rsync $dir a sd"
		rsync -av --delete --inplace "$dir" "$sd/"
	done
	#rsync -av $HOME/wiki $sd/
fi

if [ -z "$(ls -A "$android")" ]; then
 echo "Directory is empty"
else
 echo "######################################### rsync wiki a tablet"
 rsync -av --delete --inplace "$HOME/wiki" "$android/SD card/ACA"
 rsync -av --delete --inplace "$HOME/french" "$android/SD card/ACA"
fi

# adicional: documentacion y burocracia a dropbox. osea doc y buroc tiene upstream a sd y a dropbox; ambos no son más que copias y edito todo desde compu
echo "######################################### documentacion y burocracia a dropbox"
rsync -av --delete "$HOME/documentacion_y_burocracia" "$HOME/Dropbox/"

if [ -z "$(ls -A "$iphone_apps")" ]; then
 echo "iphone no está en /run/user/1000/gvfs/afc:host=00008101-000C69A93683001E,port=3/"
else
 echo "######################################### rsync french a iphone_apps vlc"
 rsync -av --delete --inplace "$HOME/french" "$iphone_apps/org.videolan.vlc-ios/"
fi

# }}}

# Repository to pull updates from
# neovim_repo="/home/ttdduu/.config/neovim"
# branch="HEAD"
#
# # Pull latest updates from Neovim repository
# echo "Pulling latest updates from Neovim repository..."
# cd "$neovim_repo" || { echo "Failed to change directory to $neovim_repo"; exit 1; }
# git fetch origin $branch # Adjust the branch name if necessary
#
# LOCAL=$(git rev-parse @)
# REMOTE=$(git rev-parse @{u})
#
# if [ $LOCAL != $REMOTE ]; then
#   echo "New changes found. Pulling latest updates..."
#   git pull origin $branch # Adjust the branch name if necessary
#
#   # Compile Neovim
#   echo "Compiling Neovim..."
#   make CMAKE_BUILD_TYPE=Release
# else
#   echo "No new changes found."
# fi
#
# echo "Done."
