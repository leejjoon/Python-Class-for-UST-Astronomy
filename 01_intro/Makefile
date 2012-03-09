all: 01_intro.html

01_intro.html: 01_intro.rst
	landslide -t ../aux/theme_jj -d 01_intro_orig.html 01_intro.rst
	cat 01_intro_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 01_intro.html
