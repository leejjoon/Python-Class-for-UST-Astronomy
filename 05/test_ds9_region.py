from ds9_region import ds9_region

assert ds9_region("circle", 2.5, 8.12, r=1.4) == \
       'circle(2.5, 8.12, 1.4)'

assert ds9_region("ellipse", 3.9, 3.3, r_maj=2.4, r_min=1.5, angle=20) == \
       'ellipse(3.9, 3.3, 2.4, 1.5, 20)'

assert ds9_region("box", 8.6, 7.6, width=2.4, height=1.4, angle=330) == \
       'box(8.6, 7.6, 2.4, 1.4, 330)'

assert ds9_region("circle", 2.5, 8.12, r=1.4) == \
       ds9_region("circle", 2.5, 8.12, 1.4)

assert ds9_region("ellipse", 3.9, 3.3, r_maj=2.4, r_min=1.5, angle=20) == \
       ds9_region("ellipse", 3.9, 3.3, 2.4, 1.5, angle=20)

assert ds9_region("box", 8.6, 7.6, width=2.4, height=1.4, angle=330) == \
       ds9_region("box", 8.6, 7.6, 2.4, 1.4, angle=330)
