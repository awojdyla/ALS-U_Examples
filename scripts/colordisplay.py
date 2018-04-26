import Shadow
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
from matplotlib.colors import ListedColormap

# get the rays and their optical path
x = in_object_1._beam.getshonecol(1)
z = in_object_1._beam.getshonecol(3)
w = in_object_1._beam.getshonecol(19)

w_min = np.amin(w)
w_max = np.amax(w)
dw = (w_max-w_min)/5

mask1 = np.where(w<=w_min+dw)
mask2 = np.where(np.logical_and(w > w_min+1*dw, w <= w_min+2*dw))
mask3 = np.where(np.logical_and(w > w_min+2*dw, w <= w_min+3*dw))
mask4 = np.where(np.logical_and(w > w_min+3*dw, w <= w_min+4*dw))
mask5 = np.where(w >= w_max-dw)


#mask3 = np.where(w!=np.amax(w) and w!=np.amin(w))
N_bins = 101
r = [[np.amin(x), np.amax(x)],[np.amin(z), np.amax(z)]]
H,  _, _  = np.histogram2d(x,z, bins=N_bins, range=r)
H1, _, _  = np.histogram2d(x[mask1],z[mask1],bins=N_bins, range=r)
H2, _, _  = np.histogram2d(x[mask2],z[mask2],bins=N_bins, range=r)
H3, _, _  = np.histogram2d(x[mask3],z[mask3],bins=N_bins, range=r)
H4, _, _  = np.histogram2d(x[mask4],z[mask4],bins=N_bins, range=r)
H5, _, _  = np.histogram2d(x[mask5],z[mask5],bins=N_bins, range=r)

fig = plt.figure(frameon=False)

cmap1 = plt.cm.Purples
cmap2 = plt.cm.Blues
cmap3 = plt.cm.Greens
cmap4 = plt.cm.Oranges
cmap5 = plt.cm.Reds
# Get the colormap colors
my_cmap1 = cmap1(np.arange(cmap1.N))
my_cmap2 = cmap2(np.arange(cmap2.N))
my_cmap3 = cmap3(np.arange(cmap3.N))
my_cmap4 = cmap4(np.arange(cmap4.N))
my_cmap5 = cmap5(np.arange(cmap5.N))
# Set alpha
my_cmap1[:,-1] = np.linspace(0, 1, cmap1.N)
my_cmap2[:,-1] = np.linspace(0, 1, cmap2.N)
my_cmap3[:,-1] = np.linspace(0, 1, cmap3.N)
my_cmap4[:,-1] = np.linspace(0, 1, cmap4.N)
my_cmap5[:,-1] = np.linspace(0, 1, cmap5.N)
# Create new colormap
my_cmap1 = ListedColormap(my_cmap1)
my_cmap2 = ListedColormap(my_cmap2)
my_cmap3 = ListedColormap(my_cmap3)
my_cmap4 = ListedColormap(my_cmap4)
my_cmap5 = ListedColormap(my_cmap5)

extent=(X[0,0]*scalefactor,X[0,-1]*scalefactor,Z[-1,0]*scalefactor,Z[0,0]*scalefactor)

#im = plt.imshow(H)
im1 = plt.imshow(H1, cmap=my_cmap1, alpha=.9)
im2 = plt.imshow(H2, cmap=my_cmap2, alpha=.9)
im3 = plt.imshow(H3, cmap=my_cmap3, alpha=.9)
im4 = plt.imshow(H4, cmap=my_cmap4, alpha=.9)
im5 = plt.imshow(H5, cmap=my_cmap5, alpha=.9)
#im5 = plt.imshow(H5, cmap=my_cmap5, alpha=.9, interpolation='bilinear')

#np.where(w<w_min+dw)
print()
#scalefactor = 1000
#plt.imshow(H,e),cmap='bwr')
#plt.title("Wavefront, from optical path")
plt.xlabel("X position [mm]")
plt.ylabel("Z position [mm]")
plt.show()