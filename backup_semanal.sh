#!/usr/bin/zsh

# Define the commit message
commit_message="Automatic weekly commit message"

# List of repositories
repos=("/home/ttdduu/code/miscellaneous_scripts" "/home/ttdduu/dotfiles")

# Repository to pull updates from
neovim_repo="/home/ttdduu/.config/neovim"

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

# Pull latest updates from Neovim repository
echo "Pulling latest updates from Neovim repository..."
cd "$neovim_repo" || { echo "Failed to change directory to $neovim_repo"; exit 1; }
git pull origin main # Adjust the branch name if necessary

# Compile Neovim
echo "Compiling Neovim..."
make CMAKE_BUILD_TYPE=Release

echo "Done."

dropbox start