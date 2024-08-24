#!/bin/bash

# Check if the current directory is already a Git repository
if [ -d .git ]; then
    echo "This directory is already a Git repository."
    exit 1
fi

# Initialize a new Git repository
git init

# Create .gitignore if it doesn't exist and add git.sh to it
if [ ! -f .gitignore ]; then
    echo ".gitignore does not exist. Creating .gitignore."
    touch .gitignore
fi

# Add git.sh to .gitignore
echo "git.sh" >> .gitignore

# Add all files to the staging area
git add .

# Commit the changes with the message "first commit"
git commit -m "first commit"

# Get the current folder name
REPO_NAME=${PWD##*/}

# Create a new public repository on GitHub using the GitHub CLI
gh repo create "$REPO_NAME" --public --source=. --remote=origin --push

# Push the changes to the new GitHub repository
git push -u origin main

echo "Repository '$REPO_NAME' has been created and pushed to GitHub."