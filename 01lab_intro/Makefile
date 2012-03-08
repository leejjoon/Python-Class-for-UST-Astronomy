all: 01_intro.html

01_intro.html: 01_intro.rst
	landslide -d 01_intro_orig.html -c 01_intro.rst
	cat 01_intro_orig.html | sed "s#file://`pwd`#.#g" > 01_intro.html
