#! /bin/sh
# https://medium.com/@shalandy/deploy-git-subdirectory-to-heroku-ea05e95fce1f
# must run from root

git subtree push --prefix server heroku main
