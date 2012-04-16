all: 06.html

06.html: 06.rst
	landslide -t ../aux/theme_jj2 -d 06_orig.html 06.rst
	cat 06_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 06.html

