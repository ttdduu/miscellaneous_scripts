#!/bin/bash
target_directory=${1:-.}

if [[ ! -d "$target_directory/.git" ]]; then
    echo ""
    exit 1
fi

branch=$(git rev-parse --abbrev-ref HEAD)
status=$(git status --porcelain)
commit_hash=$(git rev-parse --short HEAD)
if [ -n "$status" ]; then
  echo "$branch* "
else
  echo "$branch "
fi

echo "$commit_hash"
