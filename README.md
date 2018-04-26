# ALS-U_Examples

This repository contains a series of files that were used to demonstrate the capabilities of [OASYS](https://www.elettra.trieste.it/oasys.html) through scripting and widgets, and were used by [Luca Rebuffi](https://github.com/lucarebuffi) during a hands-on tutoral given at the ALS in March 2018 to provide real life examples on how these could be used to model ALS-U beamlines, the fourth generation synchrotron at Lawrence Berkeley National Lab. 

Most of these capabilities have been ported to widgets, for easy reuse. These widgets can be found [here](https://github.com/lucarebuffi/OASYS1-ALS-ShadowOui), or via the Options>addons... menu in Oasys.

Questions relative to these scripts should be adressed to [Antoine Wojdyla](https://github.com/awojdyla/).

Please note that there are many other examples available here: [https://github.com/oasys-kit/ShadowOui-Tutorial](https://github.com/oasys-kit/ShadowOui-Tutorial). 

## Examples
### Mirror deformation under heatload

### Tilt analyzer

### Wavefront sensing

### Hartmann sensor

### Beamline energy resolution
We have written a script that allows to visualize various colors, to have a rough estimate of how the various wavelength blend during propagations and determine whether the resolution of the beamline will meet the specfications

![image](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/oasys_colors.png)

- python script: [colors.py](https://github.com/awojdyla/ALS-U_Examples/blob/master/scripts/colors.py)
- OASYS workspace: [Colors.ows](https://github.com/awojdyla/ALS-U_Examples/blob/master/OASYS_examples/Colors.ows)
- jupyter notebook: [colors.ipynb](https://github.com/awojdyla/ALS-U_Examples/blob/master/Shadow_examples/Colors.ipynb)

### Hettrick Underwood monochromator

### Notional ALS-U beamlines

## What we are working on
We are interested in a number of optical beamline simulations that could be helpful for the DLSR and FEL community:

- determining the ___actual volume of the phase space__ for an undulator (the σσ'> λ/4π approximation is only valid for gaussian sources; undulators seem to produce __σσ'~λ/2π__ phase spaces in the blue region, and we would like to investigate this effect with the [M^2 formalism](https://web.archive.org/web/20110604095354/http://www.stanford.edu/~siegman/beams_and_resonators/beam_quality_tutorial_osa.pdf)
- determining how the __effective source position in an undulator__ varies with the wavelength under consideration (with SRW)
- modeling of __diaboloids__, which are modified toroids that yield minimal aberrations (see [McKinney et al. (2009)](http://doi.org/10.1117/12.828490))
- we would like to see to what extent [Forbes polynomials](https://www.osapublishing.org/oe/abstract.cfm?uri=oe-21-16-19061) can be used to describe mirror shapes more accurately, possibly using [QFit](https://pypi.python.org/pypi/Scikit-Qfit)

## Already integrated to OASYS
Please refer to [OASYS1-ALS-ShadowOui](https://github.com/oasys-als-kit/OASYS1-ALS-ShadowOui)
### Creating a source based on SRW calculation

### Scanning a parameter for mirrors and 

## How to make and use python scripts

Here is how to manipulate the `beam` in Oasys using python: 

```python
import Shadow
in_object_1._beam.getshonecol(1)
```

If you are going to modify the beam, make sure to duplicate the beams before you do so:

```python
beam_hardcopy = in_object_1._beam.duplicate()
```

### Ray attributes
Here's the Shadow Ray structure, so that you can access to specific properties within OASYS:

1.   position x in user units
2.   position y in user units
3.   position z in user units
4.   director cosine x (approx angle x' in rad)
5.   director cosine y 
6.   director cosine z (approx angle z' in rad)
7.   electric field s-polarized Es_x
8.   electric field s-polarized Es_y
9.   electric field s-polarized Es_z
10.  flag: 1.0 the ray is good, <1 the ray is lost
11.  wavevector modulus: 2 pi / lambda
12.  ray index (starting from 1.0)
13.  optical path, in user units
14.  s-polarized phase Es_phi
15.  p-polarized phase Ep_phi
16.  electric field p-polarized Ep_x
17.  electric field p-polarized Ep_y
18.  electric field p-polarized Ep_z

## Resources
Make sure you also explore these other tremendous resources:

+ [ShadowOui Tutorial](https://github.com/srio/ShadowOui-Tutorial) - An Oays/ShadowOui tutorial
+ [ALS-ShadowOui](https://github.com/lucarebuffi/OASYS1-ALS-ShadowOui), where most of the scripts here have been integrated as widgets
+ [SOS 2016](https://www.elettra.eu/Conferences/2016/SOS/Main/Program) series of talk based on optical beamline simulatoons


