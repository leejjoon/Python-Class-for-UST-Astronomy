all: index.html install.html

index.html: index.rst
	rst2html index.rst  > index.html

install.html: install.rst
	rst2html install.rst  > install.html
