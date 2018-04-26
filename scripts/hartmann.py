
import Shadow
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate

def display_hartmann(beam, Nx = 101, Nz = 101):
	# extract data (position and angles)
	x1 = beam.getshonecol(1)
	z1 = beam.getshonecol(3)
	xp = beam.getshonecol(4)
	zp = beam.getshonecol(6)

	# from the angles, extract magnitude and direction
	slo = np.sqrt(xp**2+zp**2)
	ang = np.arctan2(zp,xp)

	# interpolare on a linear grid to allow easier processing
	scalefactor = 1E6

	x_lin = np.linspace(np.min(x1), np.max(x1), Nx)
	z_lin = np.linspace(np.min(z1), np.max(z1), Nx)
	X, Z = np.meshgrid(x_lin,z_lin)
	slopes = interpolate.griddata((x1,z1),slo,(X,Z),method='linear')
	angles = interpolate.griddata((x1,z1),ang,(X,Z),method='linear')

	# compute the gradients
	grad_x = slopes*np.cos(angles)
	grad_z = slopes*np.sin(angles)

	# integrate the gradients (from the center) to get the wavefront
	xr = np.cumsum(-grad_x[:,51: 0:-1],axis=1)
	xl = np.cumsum( grad_x[:,50:-1: 1],axis=1)
	xx = np.concatenate((np.flip(xr,axis=1),xl),axis=1)

	zr = np.cumsum(-grad_z[51: 0:-1,:],axis=0)
	zl = np.cumsum( grad_z[50:-1: 1,:],axis=0)
	zz = np.concatenate((np.flip(zr,axis=0),zl),axis=0)

	# here's the wavefront (the units depend of the backprogation distance)
	wfe_au = (xx+zz)

	# show the results
	plt.imshow(wfe_au,extent=(X[0,0]*scalefactor,X[0,-1]*scalefactor,Z[-1,0]*scalefactor,Z[0,0]*scalefactor))
	plt.title("wavefront, from slopes")
	plt.xlabel('position [um]')
	plt.ylabel('position [um]')
	plt.show()

	return wfe_au

def defocus_removal(wfe_au):
	import numpy as np
	import matplotlib.pyplot as plt
	# removal of the focus term, from fit

	# grab the wavefront from the previous script
	x_lin = np.linspace(-1, 1, 101)
	X, Z = np.meshgrid(x_lin,x_lin)

	# fitting the best parabola for removal
	import scipy.linalg
	# remove spurrious points
	mask = np.where(np.isfinite(wfe_au))

	# wavefront fit for fitting
	wfe_fit = wfe_au[mask]

	# Create simple terms, for fit and removal
	P0 = 1+0*X[mask]
	P1 = X[mask]
	P2 = X[mask]**2 + Z[mask]**2

	# perform the fitting of the wavefront
	B = np.concatenate(
	(P0.reshape(P0.size,1),P1.reshape(P0.size,1),P2.reshape(P0.size,1)),
	axis=1)
	C,_,_,_ = scipy.linalg.lstsq(B, wfe_fit)

	# removal of the quadratic term
	corr = -C[2]*(X**2+Z**2)
	wfe = (wfe_au-np.nanmean(wfe_au)+corr)*1e6
	wfe[np.where(wfe>3000)]=0

	# scale factor for plotting display
	scalefactor = 1E3

	fig = plt.figure()
	plt.imshow(wfe,extent=(X[0,0]*scalefactor,X[0,-1]*scalefactor,Z[-1,0]*scalefactor,Z[0,0]*scalefactor))
	plt.title("Wavefront, from slopes, with defocus removed")
	plt.xlabel("X position [mm]")
	plt.ylabel("Z position [mm]")
	plt.colorbar()
	plt.set_cmap('plasma')
	plt.show()

	return wfe1


wfe_au = display_hartmann(in_object_1._beam)
defocus_removal(wfe_au)