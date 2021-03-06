# Ray attributes

Shadow Ray structure:

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

invoke them in Oasys using python: 

```python
import Shadow
in_object_1._beam.getshonecol(1)
```
make sure to duplicate the beams before you modify them:

```python
beam_hardcopy = in_object_1._beam.duplicate()
```