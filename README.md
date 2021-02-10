# Basic spreasheet tool for creating DuckPad profiles

1) open profile_example.ods in LibreOffice or Excell

2) save_as a new sheet with a usef profile name

3) Fill in the 3 matrices in the spreadsheet with commands, display labels, and colors.  RBG colors are entered into a 
single cell as rrr/ggg/bbb.

4) export the sheet as a .scv file

5) run > python profbuild.py   filename.csv

This will build a folder, create config.txt, and all 15 keyX.txt files.

