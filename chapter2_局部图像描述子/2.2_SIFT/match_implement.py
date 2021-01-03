from sift import *
from scipy.ndimage import filters
from numpy import *
from PIL import Image
from pylab import *
from IPython import embed


im1f = 'jimei_grey.jpg'
im2f = 'jimei2.jpg'

im1 = array(Image.open(im1f).convert('L'))
im2 = array(Image.open(im2f).convert('L'))

process_image(im1f, 'jimei.sift')
l1, d1 = read_features_from_file('jimei.sift')

figure()
gray()
plot_features(im1,l1,circle=True)
show()


process_image(im2f, 'jimei2.sift')
l2, d2 = read_features_from_file('jimei2.sift')
matches = match_twosided(d1, d2)
print('{} matches'.format(len(matches.nonzero()[0])))
 	

figure()
gray()
plot_matches(im1, im2, l1, l2, matches)
show()
