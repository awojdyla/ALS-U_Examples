# ALS-U_Examples

This repository contains a series of files that were used to demonstrate the capabilities of [OASYS](https://www.elettra.trieste.it/oasys.html) through scripting and widgets, and were used by [Luca Rebuffi](https://github.com/lucarebuffi) during a hands-on tutoral given at the ALS in March 2018 to provide real life examples on how these could be used to model ALS-U beamlines, the fourth generation synchrotron at Lawrence Berkeley National Lab. 

Most of these capabilities have been ported to widgets, for easy reuse. These widgets can be found [here](https://github.com/lucarebuffi/OASYS1-ALS-ShadowOui), or via the Options>addons... menu in Oasys.

Questions relative to these scripts should be adressed to [Antoine Wojdyla](https://github.com/awojdyla/).

Please note that there are many other examples available here: [https://github.com/oasys-kit/ShadowOui-Tutorial](https://github.com/oasys-kit/ShadowOui-Tutorial). 

## Examples
### Mirror deformation under heatload
For DLSR and FEL, the first mirror (HHLO or HOMS) will experience a servere heatload, with the incident beam carrying up to 20kW. Even with very efficient cooling, the mirror will bulge and cause some wavefront error. We have studied these effects with FEM using ANSYS, and we provide a script that adequately loads the deformed mirror shape and allows to study the propagation.

![hhlo](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/hhlo.png)

- python script: [hhlo.py](https://github.com/awojdyla/ALS-U_Examples/blob/master/scripts/hhlo.py)
- OASYS workspace: [HHLO.ows](https://github.com/awojdyla/ALS-U_Examples/blob/master/OASYS_examples/HHLO.ows)

A sample ANSYS deformation file is available here : [49_7.txt](https://github.com/awojdyla/ALS-U_Examples/blob/master/assets/49_7.txt)

### Wavefront 
We have written a script that allows to retrieve the wavefront after an element. For the script to work, 

![wavefront](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/oasys_wavefront.png)

- python script: [wavefront.py](https://github.com/awojdyla/ALS-U_Examples/blob/master/scripts/wavefront.py)
- OASYS workspace: [Wavefront.ows](https://github.com/awojdyla/ALS-U_Examples/blob/master/OASYS_examples/Wavefront.ows)
- jupyter notebook: [Wavefront.ipynb](https://github.com/awojdyla/ALS-U_Examples/blob/master/Shadow_examples/Wavefront.ipynb)

_It seems that this element works well with toroidal mirrors, but at the moment compound focusing elements such as KB pairs seems to have some issues associated with the optical path. See "Hartmann sensor" below for a workaround_

### Wavefront analyzer
Decomposition of the wavefront on a Zernike basis. __This requires [poppy](https://github.com/mperrin/poppy)__ and might not work straight out of the box.

![zernikes](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/oasys_zernikes.png)

- python script: [zernikes.py](https://github.com/awojdyla/ALS-U_Examples/blob/master/scripts/zernikes.py)
- OASYS workspace: [Zernikes.ows](https://github.com/awojdyla/ALS-U_Examples/blob/master/OASYS_examples/Zernikes.ows)
- jupyter notebook: [Zernikes.ipynb](https://github.com/awojdyla/ALS-U_Examples/blob/master/Shadow_examples/Zernikes.ipynb)

### Tilt sensitivity analyzer
Since the misalignment of an optics can cause aberrations, it can be intersting to study the sensitivity to this misalignment. In this example, we show how in particular how astigmatism and coma change as a toroid is rotated along the tangential direction.

This is an example of use of [poppy](https://github.com/mperrin/poppy) outside the OASYS environment, which can be useful if you couldn't make the previous example wrok (don't forget to install poppy by running `pip install poppy` in the terminal!)

![tilt](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/toroid_tilt.png)

- jupyter notebook: [Tilt.ipynb](https://github.com/awojdyla/ALS-U_Examples/blob/master/Shadow_examples/Tilt.ipynb)

### Hartmann sensor
In order to get an unbiased estimate of the wavefront, it is possible to use the slope at a certain location in the beam to estimate the wavefront errors. 

This is a workaround for the case where using the optical path length in the beam fails (e.g. many compounded optical elements or large source/incoherent illumination)

__This is still under development__: The reconstruction has numerical errors, and the units are not properly taken into account

![hartmann](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/hartmann.png)

- python script: [hartmann.py](https://github.com/awojdyla/ALS-U_Examples/blob/master/scripts/hartmann.py)
- OASYS workspace: [Hartmann.ows](https://github.com/awojdyla/ALS-U_Examples/blob/master/OASYS_examples/Hartmann.ows)

### Beamline energy resolution
We have written a script that allows to visualize various colors, to have a rough estimate of how the various wavelength blend during propagations and determine whether the resolution of the beamline will meet the specfications

![colors](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/oasys_colors.png)

- python script: [colors.py](https://github.com/awojdyla/ALS-U_Examples/blob/master/scripts/colors.py)
- OASYS workspace: [Colors.ows](https://github.com/awojdyla/ALS-U_Examples/blob/master/OASYS_examples/Colors.ows)
- jupyter notebook: [colors.ipynb](https://github.com/awojdyla/ALS-U_Examples/blob/master/Shadow_examples/Colors.ipynb)

### Hettrick Underwood monochromator
The Hettrick Underwood monochromator is an example where the beam is focused before the monochromator (see MC Hettrick and JH Underwood "[Stigmatic high throughput monochromator for soft x rays](https://doi.org/10.1364/AO.25.004228)" (1986) for more information)

- OASYS workspace: [Hettrick-Underwood.ows](https://github.com/awojdyla/ALS-U_Examples/blob/master/OASYS_examples/Hettrick-Underwood.ows)


### Notional ALS-U beamlines
Two of the notional beamline for the ALS-U project have been modeled using optical beamline simulations:

- [ALS-U SXR Flagship beamline.ows](https://github.com/awojdyla/ALS-U_Examples/blob/master/ALS-U%20SXR%20flagship%20beamline.ows)
- [ALS-U TXR Flagship beamline.ows](https://github.com/awojdyla/ALS-U_Examples/blob/master/ALS-U%20TXR%20flagship%20beamline.ows)

They bith aim at a 1:5000 energy resolution and a 5um beam at the exist slits, each operating in a different energy range (SXR: 250-1400eV; TXR:1-8keV)

### Magic toroid configuration
Toroidal mirrors do exhibit severe aberrations, but there is a configuration in which the primary coma vanishes, leading to superior optical performances -- this is a first step towards the ideal diaboloid shape. 
For more information, see Appendix A in [McDowell et al.(2004)](https://doi.org/10.1107/S0909049504024835)

- OASYS workspace: [Magic_Toroid.ows]((https://github.com/awojdyla/ALS-U_Examples/blob/master/OASYS_examples/Magic_Toroid.ows)
)


## What we are working on
We are interested in a number of optical beamline simulations that could be helpful for the DLSR and FEL community:

- determining the ___actual volume of the phase space__ for an undulator (the σσ'> λ/4π approximation is only valid for gaussian sources; undulators seem to produce __σσ'~λ/2π__ phase spaces in the blue region, and we would like to investigate this effect with the [M^2 formalism](https://web.archive.org/web/20110604095354/http://www.stanford.edu/~siegman/beams_and_resonators/beam_quality_tutorial_osa.pdf)
- determining how the __effective source position in an undulator__ varies with the wavelength under consideration (with SRW)
- modeling of __diaboloids__, which are modified toroids that yield minimal aberrations (see [McKinney et al. (2009)](http://doi.org/10.1117/12.828490))
- we would like to see to what extent [Forbes polynomials](https://www.osapublishing.org/oe/abstract.cfm?uri=oe-21-16-19061) can be used to describe mirror shapes more accurately, possibly using [QFit](https://pypi.python.org/pypi/Scikit-Qfit)

## Already integrated to OASYS

A few scripts we were working on have been integrated to the list of widgets in OASYS. Please refer to [OASYS1-ALS-ShadowOui](https://github.com/oasys-als-kit/OASYS1-ALS-ShadowOui)
### Creating a source based on SRW calculation

### Scanning a parameter for mirrors and gratings

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


