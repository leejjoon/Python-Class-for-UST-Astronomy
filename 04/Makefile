all: 04.html 04_1.html

04.html: 04.rst
	landslide -t ../aux/theme_jj -d 04_orig.html 04.rst
	cat 04_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 04.html


04_1.html: 04_1.rst
	landslide -t ../aux/theme_jj -d 04_1_orig.html 04_1.rst
	cat 04_1_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 04_1.html


