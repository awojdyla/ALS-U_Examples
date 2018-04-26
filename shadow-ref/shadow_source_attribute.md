# Source attributes
- fdistr	= 2

	Defines source angle distribution types. 
	Available options are: 
	1. flat (1)
	2. uniform (2)
	3. gaussian (3)
	4. synchrotron (4)
	5. conical (5)
	6. exact synchrotron(6).

-  fgrid	= 0  

	Defines source modelling type -- spatial/momentum space.  
	Options are: 
	0. random/random (0), 
	1. grid/grid (1), 
	2. grid/random (2), 
	3. random/grid (3), 
	4. ellipse in phase/random on the ellipse (4),
	5. ellipse in phase/gid on the ellipse (5). 
	
- fsour	= 0 
	
	spatial source type/shape in X-Z plane.  Options are: 
	0. point (0), 
	1. rectangle (1), 
	2. ellipse (2), 
	3. gaussian(3).

- fsource_depth	= 1
	
	Defines the source depth (Y).  
	Options are:  
	1. no depth (1), 
	2. flat depth (2),
	3. gaussian (3), 
	4. synchrotron depth (4).

- f_coher	= 0 
	
	if generating the A vectors, defines whether the light is incoherent (0), or coherent (1).

- f_color	= 1 
	
	Photon energy distribution type.  Options are: 
	1. single energy (1), 
	2. multiple discrete energies, up to 10 energies
	3. uniform energy distribution (3).

- f_phot	= 0 
	defines whether the photon energy will be specified in eV (0) or Angstroms (1).

-  f_pol	= 0 
	For synchrotron and wiggler sources defines the polarization component of interest: 
	1. parallel (1), 
	2. perpendicular (2), 
	3. total (3).

- f_polar = 1 
	flag defining whether or not to generate the A vectors:  yes (1), no (0).
	
- f_opd	=  0 
	Flag defining whether or not to save the optical  paths (OPD):  yes (1), no (0).

- f_wiggler	= 0 - source type.  
	Options:  
	0. regular/bending magnet/synchrotron (0), 
	1. wiggler (1),
	2.  undulator (2).

- f\_bound\_sour	=  0 
	Flag defining whether or not to optimize the source:  yes (1), no (0).
	
- f\_sr\_type	=   0 - 
	
	For synchrotron sources, distribution in terms of: photons (0), or power distribution (1).
	
- istar1	= 478291 

	Seed for random number generator, odd.
	
- npoint	= 5000 
	
	 Number of random rays (0-5000).

- ncol	=  0 

	Source generation routines will fill in the number of columns in your source.

- n_circle	= 0 

	For fgrid=1,3 and fdistr=5; number of grid points along each circle.
	
- n_color	=  0

	For f_color=2, number of discrete lines in energy, maximum = 10.
	
- n_cone	= 0 

	For fgrid=1,3 and fdistr=5; number of grid
 			  points along the radius(number of concentric circles).
 			  
- ido_vx	= 1 
	
	For fgrid=1,3; number of grid points in horizontal angle distribution.

- ido_vz	=  1 

	For fgrid=1,3; number of grid points in vertical angle distribution.
	
- ido\_x\_s	= 1 

	For fgrid=1,2; fsour=1 points along x, fsour=2 number of concentric ellipses.

- ido\_y\_s	= 1 

	For fgrid=1,2; number of points along depth (Y).

- ido\_z\_s	=  1 

	For fgrid=1,2; fsour=1 points along z, fsour=2 number of concentric ellipses.
	
- ido_xl	=             0 
	
	For fgrid=4,5; number of sigma levels in X for phase space ellipse source.
	
- ido_xn	=             0 

	For fgrid=5; number of rays/sigma level in X
	
- ido_zl	=             0 

	For fgrid=4,5; number of sigma levels in X for
 			  phase space ellipse source.

- ido_zn	= 0 -
	For fgrid=5; number of rays/sigma level in Z.

- sigxl1	=  0.0000000000000000E+00 

	For fgrid=4,5; values for sigma, levels in X. (
	sigxl2	=  0.0E+00;   
	sigxl3	=  0.0E+00;
	sigxl4	=  0.0E+00;
	sigxl5	=  0.0E+00;
	sigxl6	=  0.0E+00;
	sigxl7	=  0.0E+00;
	sigxl8	=  0.0E+00;
	sigxl9	=  0.0E+00;
	sigxl10=  0.0E+00;
	sigzl1	=  0.0E+00)

	for fgrid=4,5; values for sigma, levels in Z. (
	sigzl2	=  0.0E+00;   
	sigzl3	=  0.0E+00;
	sigzl4	=  0.0E+00;
	sigzl5	=  0.0E+00;
	sigzl6	=  0.0E+00;
	sigzl7	=  0.0E+00;
	sigzl8	=  0.0E+00;
	sigzl9	=  0.0E+00;
	sigzl10	=  0.0E+00)
 
- conv_fact	=  0.0000000000000000E+00 
	For fwiggler=1; conversion factor from meters to user units.

- cone_max	=  0.0000000000000000E+00
	For fdistr=5; maximum half divergence.

- cone_min	=  0.0000000000000000E+00 
	For fdistr=5; minimum half divergence.
	
- epsi_dx	=  0.0000000000000000E+00
	for fdistr=4,6 or fwiggler=1; in X, the distance from the waist that the emittance value corresponds to, signed. 

- epsi_dz	=  0.0000000000000000E+00
	For fdistr=4,6 or fwiggler=1; in Z, the distance from the waist that the emittance value corresponds to, signed.
	
- epsi_x	=  0.0000000000000000E+00
	For fdistr=4,6 or fwiggler=1;  the beam emittance (in X) in units of radians\*length units used so far. 

- epsi_z	=  0.0000000000000000E+00 
	for fdistr=4,6 or fwiggler=1; the beam emittance (in Z) in units of radians*length units used so far.

- hdiv1	=  0.0000000000000000E+00

 Horizontal divergence in +X (radians).

- hdiv2	=  0.0000000000000000E+00 

	Horizontal divergence in -X (radians).

- ph1	=  11160.00000000000 

	Photon energy:  f_color=1 desired energy, f_color=2 first energy line, f_color=3 minimum energy.
	
- ph2	=  0.0000000000000000E+00 

	Photon energy: f_color=2 second energy line, f_color=3 maximum energy.
	
- ph3	=  0.0000000000000000E+00 

	Photon energy: f_color=2 third energy line.
	(ph4	=  0.0E+00;
 ph5	=  0.0E+00;
 ph6	=  0.0E+00;
 ph7	=  0.0E+00;
 ph8	=  0.0E+00;
 ph9	=  0.0E+00;
 ph10	=  0.0E+00)

- bener	=  0.0000000000000000E+00 

	For fdistr=4,6 or f_wiggler=1; Electron beam energy (GeV).
 				    
- pol_angle	=  0.0000000000000000E+00 
	
	For f_polar=1; phase difference in degrees.

- pol_deg	=  0.0000000000000000E+00 
	
	For f_polar=1; degree of polarization (between 0 and 1).
	
- r_aladdin	=  0.0000000000000000E+00 

	For fdistr=4,6 or f_wiggler=1; bending magnet radius in units of length used for source size, CCW rings negative.
					    
- r_magnet	=  0.0000000000000000E+00 

	for fdistr=4,6 or f_wiggler=1; Bending magnet radius (m).

- sigdix	=  0.0000000000000000E+00 

	For fdistr=3; sigma (radians)for horizontal divergence (gaussian angle distribution).
 				    
- sigdiz	=  0.0000000000000000E+00

	For fdistr=3; sigma (radians) for vertical divergence (gaussian angle distribution).

- sigmax	=  0.0000000000000000E+00 
	
	For fsour=3; sigma in X

- sigmay	=  0.0000000000000000E+00 

	For fsource_depth=3; sigma in Y

- sigmaz	=  0.0000000000000000E+00

	or fsour=3; sigma in Z

- vdiv1	=  6.0000000000000002E-05 

	Vertical divergence in +Z (radians).

- vdiv2	=  6.0000000000000002E-05 

	Vertical divergence in -Z (radians).

- wxsou	=  0.0000000000000000E+00 

	For fsour=1,2; source width (X).

- wysou	=  0.0000000000000000E+00 

	For fsource_depth=2; source depth (Y).

- wzsou	=  0.0000000000000000E+00 

	For fsour=1,2; source height (Z).

- file\_traj	= '   '

	For fwiggler=1,2; filename containing the electron trajectoryfor wigglers orthe CDF's for undulators. (from make_id).
	
- file\_source	= '   '
	
	Filled in by source generation.
            	   
- file\_bound	=  '  '	

	For f\_bound\_sour=1; file containing the output of reflag and histo3. For f\_bound\_sour=2; file containing the slit / acceptance : 
	
		DIST X1 X2 Z1 Z2
   DIST: distance to slit (use 0 for angular acceptance), X1 X2 slit limits (user unit)                                    of angles (if DIST=0) in X. Same for Z.

The last variables are set in the source generation and recorded in END.00 file. They should be left alone.

- oe_number	=             0 
- idummy	=             0	
- dummy	=  0.0000000000000000E+00  
-  f_new = 0 