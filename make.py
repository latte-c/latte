import os

print('> Generaing antlr4 parser')
os.system('antlr4 -Dlanguage=Python3 -visitor -no-listener latte/front/parser/Latte.g4 -o latte/front/parser')