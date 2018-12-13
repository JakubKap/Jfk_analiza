
all: Wymierne.g4
	antlr4 -Dlanguage=Python3 -o './gen' Wymierne.g4

clean: gen/Wymierne.interp gen/WymierneLexer.interp gen/WymierneLexer.py gen/WymierneLexer.tokens gen/WymierneListener.py gen/WymierneParser.py gen/Wymierne.tokens

	rm gen/Wymierne.interp
	rm gen/WymierneLexer.interp
	rm gen/WymierneLexer.py
	rm gen/WymierneLexer.tokens
	rm gen/WymierneListener.py
	rm gen/WymierneParser.py
	rm gen/Wymierne.tokens
	
	
