from pathlib import Path

pathlist = Path(".").glob('**/*.png')
cardsTex = open("cards.tex", 'w')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)
    cardsTex.write("\includegraphics[width=\cardwidth]{%s}"%(path_in_str))