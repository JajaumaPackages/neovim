#!/bin/bash

set -e
tempDir=$(mktemp -d)
checkoutDir="$tempDir/neovim"
git clone --quiet https://github.com/neovim/neovim "$checkoutDir"
tar -C "$tempDir" -cjf neovim.tar.bz2 neovim

lastTag=$(cd "$checkoutDir"; git describe --abbrev=0 | sed 's/^v//')
headCommit=$(cd "$checkoutDir"; git rev-list HEAD -n 1 | cut -c 1-7)

echo "%global gitdate $(date +%Y%m%d)"
echo "%global gitversion ${lastTag}"
echo "%global gitcommit ${headCommit}"

rm -rf "$tempDir"
