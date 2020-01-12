#!/bin/bash

cd Maverick
git pull --rebase
cd ..

git add .
git commit -m "update submodule Maverick"