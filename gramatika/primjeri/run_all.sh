#!/bin/sh
for file in $(ls *.tex); do
  echo -n "Doing $file... "
  xelatex -synctex=1 -interaction=nonstopmode $file > /dev/null
  convert -density 300 ${file%.*}.pdf ${file%.*}.png > /dev/null
  echo "done!"
done
