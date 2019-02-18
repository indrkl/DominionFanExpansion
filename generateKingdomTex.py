from pathlib import Path

pathlist = Path(".").glob('**/*.png')
list = []
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    list.append(path_in_str)


cardsTex = open("cards.tex", 'w')
list.sort()
for item in list:
    cardsTex.write("\includegraphics[width=\cardwidth]{%s}\n"%(item))