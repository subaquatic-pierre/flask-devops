#! /bin/bash

echo "Devops Build service ..."
# SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Project directory $PROJECT_DIR"
echo "cd $PROJECT_DIR"
# cd $PROJECT_DIR

echo "git checkout main"
# git checkout main

echo "git pull origin main"
# git pull origin main

echo "Running build script ..."
echo "NODE_VERSION=18 ~/.nvm/nvm-exec npm install"
# NODE_VERSION=18 ~/.nvm/nvm-exec npm install

echo "NODE_VERSION=18 ~/.nvm/nvm-exec npm run build"
# NODE_VERSION=18 ~/.nvm/nvm-exec npm run build

echo "Restarting service ..."
echo "echo $ROOT_PASSWORD | sudo -S systemctl restart example-frontend.service"
# echo $ROOT_PASSWORD | sudo -S systemctl restart example-frontend.service
