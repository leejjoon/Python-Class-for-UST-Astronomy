#!/usr/bin/env python
'''
Test combinations of contouring, filled contouring, and image plotting.
For contour labelling, see contour_demo.py.

The emphasis in this demo is on showing how to make contours register
correctly on images, and on how to get both of them oriented as
desired.  In particular, note the usage of the "origin" and "extent"
keyword arguments to imshow and contour.
'''
import matplotlib.pyplot as plt
import numpy as np
from pylab import bivariate_normal

#Default delta is large because that makes it fast, and it illustrates
# the correct registration between image and contours.
delta = 0.5

extent = (-3,4,-4,3)

x = np.arange(-3.0, 4.001, delta)
y = np.arange(-4.0, 3.001, delta)
X, Y = np.meshgrid(x, y)
Z1 = bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
Z = (Z1 - Z2) * 10

levels = np.arange(-2.0, 1.601, 0.4) # Boost the upper limit to avoid truncation
                                  # errors.

plt.figure()

plt.subplot(1,2,1)

plt.imshow(Z)
plt.colorbar()

plt.subplot(1,2,2)

cset1 = plt.contourf(X, Y, Z, levels,
                     cmap=plt.cm.jet, #plt.cm.get_cmap('jet', len(levels)-1),
                     )
# It is not necessary, but for the colormap, we need only the
# number of levels minus 1.  To avoid discretization error, use
# either this number or a large number such as the default (256).

#If we want lines as well as filled regions, we need to call
# contour separately; don't try to change the edgecolor or edgewidth
# of the polygons in the collections returned by contourf.
# Use levels output from previous call to guarantee they are the same.
cset2 = plt.contour(X, Y, Z, cset1.levels,
                    colors = 'k',
                    )

# It is easier here to make a separate call to contour than
# to set up an array of colors and linewidths.
# We are making a thick green line as a zero contour.
# Specify the zero level as a tuple with only 0 in it.
cset3 = plt.contour(X, Y, Z, (0,),
                    colors = 'g',
                    linewidths = 2)

plt.title('Filled contours')
plt.colorbar(cset1)


plt.show()
