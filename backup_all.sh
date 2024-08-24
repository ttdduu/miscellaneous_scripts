#!/usr/bin/zsh

history > /home/ttdduu/dotfiles/historial_bkp_semanal.txt

nvim --headless +PlugUpdate +qall

dropbox start

# {{{ repos=("/home/ttdduu/code/miscellaneous_scripts" "/home/ttdduu/dotfiles")


# Define the commit message
commit_message="Automatic weekly commit message"

# List of repositories
repos=("/home/ttdduu/code/miscellaneous_scripts" "/home/ttdduu/dotfiles")

# Function to add, commit, and push changes if there are uncommitted changes
function commit_and_push {
  local repo=$1
  echo "Processing repository: $repo"

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
done
# }}}

# {{{ rsync a sd externo

dirs_para_sd=(
    "$HOME/wiki"
    #"/path/to/yet/another/directory"
    # Add more directories as needed
)

if [ -z "$(ls -A "$sd")" ]; then
	echo "Directory is empty"
else
	for dir in "${dirs_para_sd[@]}"; do
		rsync -av "$dir" "$sd/"
	done
	#rsync -av $HOME/wiki $sd/
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
