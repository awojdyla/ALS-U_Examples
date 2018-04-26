import Shadow
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate

def display_wavefront(beam, Nx=101, Nz=101):
	# get the rays and their optical path
	x1 = beam.getshonecol(1)
	z1 = beam.getshonecol(3)
	path1 = beam.getshonecol(13)

	# resampling the OPD on a constant grid
	x_lin = np.linspace(np.min(x1), np.max(x1), Nx)
	z_lin = np.linspace(np.min(z1), np.max(z1), Nx)
	X, Z = np.meshgrid(x_lin,z_lin)
	wfe1 = interpolate.griddata((x1,z1),path1,(X,Z),method='linear')

	#removal pf piston
	wfe_um = (wfe1-np.nanmean(wfe1))*1e6

	# scale factor for plotting display
	scalefactor = 1E3
	plt.imshow(wfe_um,extent=(X[0,0]*scalefactor,X[0,-1]*scalefactor,Z[-1,0]*scalefactor,Z[0,0]*scalefactor))
	plt.title("Wavefront, from optical path [um]")
	plt.xlabel("X position [mm]")
	plt.ylabel("Z position [mm]")
	plt.colorbar()
	plt.set_cmap('plasma')
	plt.show()

	# send the object, for later
	return wfe_um

display_wavefront(in_object_1._beam)