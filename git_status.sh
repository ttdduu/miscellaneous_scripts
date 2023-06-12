#!/bin/bash

branch=$(git rev-parse --abbrev-ref HEAD)
status=$(git status --porcelain)

if [ -n "$status" ]; then
  echo "$branch*"
else
  echo "$branch"
fi

