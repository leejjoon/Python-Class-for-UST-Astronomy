all: 03.html

03.html: 03.rst
	landslide -t ../aux/theme_jj -d 03_orig.html 03.rst
	cat 03_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 03.html


