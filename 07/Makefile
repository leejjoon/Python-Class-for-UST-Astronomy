all: 07.html 07_1.html

07.html: 07.rst
	landslide -t ../aux/theme_jj2 -d 07_orig.html 07.rst
	cat 07_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 07.html

07_1.html: 07_1.rst
	landslide -t ../aux/theme_jj2 -d 07_1_orig.html 07_1.rst
	cat 07_1_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 07_1.html
