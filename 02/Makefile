all: 02.html

02.html: 02.rst
	landslide -t ../aux/theme_jj -d 02_orig.html 02.rst
	cat 02_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 02.html
