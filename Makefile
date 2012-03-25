all: index.html install.html

index.html: index.rst style.css
	rst2html index.rst  --stylesheet-path=style.css  > index.html

install.html: install.rst style.css
	rst2html install.rst  --stylesheet-path=style.css > install.html
