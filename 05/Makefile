all: 05.html 05_hw.html 05_hw_single.html 05_hw.tgz

05.html: 05.rst
	landslide -t ../aux/theme_jj2 -d 05_orig.html 05.rst
	cat 05_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 05.html

05_hw.html: 05_hw.rst
	landslide -t ../aux/theme_jj2 -d 05_orig.html 05_hw.rst
	cat 05_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 05_hw.html

# 052.html: 05.rst
# 	landslide -t ../aux/theme_jj -d 05_orig.html 05.rst
# 	cat 05_orig.html | sed "s#file://`(cd ..;pwd)`#..#g" > 052.html

05_hw_single.html: 05_hw.rst
	../rst2html.py --stylesheet-path=../style.css 05_hw.rst > 05_hw_single.html

05_hw.tgz: test_mergesort.py test_mergesort_generator.py test_ds9_region.py Gvaramadze2010.tex
	tar czvf 05_hw.tgz test_mergesort.py test_mergesort_generator.py test_ds9_region.py Gvaramadze2010.tex

