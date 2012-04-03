all: 05.html 05_hw.html

05.html: 05.rst
	landslide -t ../aux/theme_jj2 -d 05_orig.html 05.rst
	cat 05_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 05.html

05_hw.html: 05_hw.rst
	landslide -t ../aux/theme_jj2 -d 05_orig.html 05_hw.rst
	cat 05_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 05_hw.html

# 052.html: 05.rst
# 	landslide -t ../aux/theme_jj -d 05_orig.html 05.rst
# 	cat 05_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 052.html


