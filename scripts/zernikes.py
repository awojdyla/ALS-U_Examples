import Shadow
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate

def zernike_projection(beam, Nx=101, Nz=101, N_zern= 8):
	x = beam.getshonecol(1)
	z = beam.getshonecol(3)
	path = beam.getshonecol(13)

	x_lin = np.linspace(np.min(x), np.max(x), Nx)
	z_lin = np.linspace(np.min(z), np.max(z), Nx)
	X, Z = np.meshgrid(x_lin,z_lin)
	wfe = interpolate.griddata((x,z),path,(X,Z),method='linear')

	import sys
	import numpy
	sys.path.insert(0,"/Users/awojdyla/python/poppy/")

	from poppy import zernike
	# commented import astropy and import poppy_core in poppy repo

	#4 defocus
	mask2 = np.where(numpy.isnan(wfe))
	wfe_proj = wfe.copy()
	wfe_proj[mask2] = 0

	N_Zern = 8
	#define an aperture for the Zernike basis (non-nans)
	aperture = wfe.copy()*0+1
	aperture[mask2] = 0
	ZZ = zernike.arbitrary_basis(aperture, nterms=N_Zern, rho=None, theta=None, outside=0)

	proj = np.zeros(N_Zern)
	for i in np.arange(N_Zern):
	    Zerni = ZZ[i,:,:]/np.sqrt(np.sum(ZZ[i,:,:]*ZZ[i,:,:]))
	    proj[i] = np.sum(wfe_proj*Zerni)

	proj[0]=0;

	fig = plt.stem(np.arange(N_Zern), proj*1e3)
	plt.title("Zernike projections")
	plt.xlabel("Noll index")
	plt.ylabel("coefficient [a.u.]")
	plt.show()

	return proj

zernike_projection(in_object_1._beam)

