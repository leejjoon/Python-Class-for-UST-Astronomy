all: 04.html

04.html: 04.rst
	landslide -t ../aux/theme_jj -d 04_orig.html 04.rst
	cat 04_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 04.html


