# ALS-U_Examples

This repository contains a series of files that were used to demonstrate the capabilities of [OASYS](https://www.elettra.trieste.it/oasys.html) through scripting and widgets, and were used by [Luca Rebuffi](https://github.com/lucarebuffi) during a hands-on tutoral given at the ALS in March 2018 to provide real life examples on how these could be used to model ALS-U beamlines, the fourth generation synchrotron at Lawrence Berkeley National Lab. 

Most of these capabilities have been ported to widgets, for easy reuse. These widgets can be found [here](https://github.com/lucarebuffi/OASYS1-ALS-ShadowOui), or via the Options>addons... menu in Oasys.

Questions relative to these scripts should be adressed to [Antoine Wojdyla](https://github.com/awojdyla/).

## How to use python scripts


## How to read a file and generate a source by resampling

The initial profile ws generated using xoppy (which itself call SRW)

## Creating a source based on SRW calculation


## Example were HYBRID fails
The file [Hybrid_test](https://github.com/awojdyla/ALS-U_Examples/blob/master/Hybrid_fails.ows) provides an example where Oasys fails
![Hybrid test](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/hybrid_test.png "Hybrid test")

Hybrid should *not* be used when the aberrations are quite large (error figure larger than the wavelength), since the resampling of the beam to account for diffraction effects will destroy any correlations between ray slope an position, typical of slope-error bound optics.

For example, here is the beam without Hybrid
![without Hybrid](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/hybrid_wo.png "without hybrid")

and here with Hybrid
![with Hybrid](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/hybrid_w.png "with hybrid")

As a general rule, one should abstain from daisy-chaining Hybrid screens, since each time the beam undergoes a resampling.
![Hybrid nono](https://github.com/awojdyla/ALS-U_Examples/blob/master/images/hybrid_nono.png "do not do this!")

## Scanning and looping

`scanning_ellipse_shape.py` and 
`scanning_vls_ruling_density`

in action: 
`Looping and Scanning variable via Python scripts`

They all have been integrated as standalone widget into [Shadow ALS utility](https://github.com/lucarebuffi/OASYS1-ALS-ShadowOui)

## Resources
Make sure you also explore these other tremendous resources:

+ [ShadowOui Tutorial](https://github.com/srio/ShadowOui-Tutorial) - An Oays/ShadowOui tutorial
+ [ALS-ShadowOui](https://github.com/lucarebuffi/OASYS1-ALS-ShadowOui), where most of the scripts here have been integrated as widgets
+ [SOS 2016](https://www.elettra.eu/Conferences/2016/SOS/Main/Program) series of talk based on optical beamline simulatoons


