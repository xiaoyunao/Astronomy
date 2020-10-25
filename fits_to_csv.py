import astropy.io.fits
import numpy
data = astropy.io.fits.open('path')
t = data[1].data
print(t)
numpy.savetxt("new.csv", t, delimiter=',', fmt='%s')
