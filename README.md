# Basic spreasheet tool for creating DuckyPad profiles
([DuckyPad](https://github.com/dekuNukem/duckyPad) 
is a sweet macro-pad )

1) open `profile_example.ods` in LibreOffice, Microsoft Excel, etc.

2) save_as a new sheet with a useful profile name

3) Fill in the 3 matrices in the spreadsheet with commands, display labels, and colors.  RBG colors are entered into a 
single cell as `rrr/ggg/bbb` (`rrr` etc can 1-3 digits (0-255)).

4) export the sheet as a `.csv` file such as `profileX_game.csv`

5) run `> python profbuild.py profileX_game.csv`

This will build a folder, create `config.txt` file, and all 15 `keyX.txt` files.

