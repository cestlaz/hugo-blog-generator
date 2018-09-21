#!/bin/bash
hugo
cd public
git add .
git commit -a -m "added newcontent"
git push
cd ..
