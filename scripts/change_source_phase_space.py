import numpy
import scipy.stats as stats
from oasys.widgets import congruence

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['figure.max_open_warning'] = '0'

class Distribution:
    POSITION = 0
    DIVERGENCE = 1
    
class Axis:
    X = 0
    Z = 1

def extract_distribution_from_file(distribution_file_name):
    distribution = []

    try:
        distribution_file = open(distribution_file_name, "r")

        rows = distribution_file.readlines()

        for index in range(0, len(rows)):
            row = rows[index]

            if not row.strip() == "":
                values = row.split()

                if not len(values) == 2: raise Exception("Malformed file, must be: <value> <spaces> <frequency>")
                               
                value = float(values[0].strip())
                frequency = float(values[1].strip())

                distribution.append([value, frequency])

    except Exception as err:
        raise Exception("Problems reading distribution file: {0}".format(err))
    except:
        raise Exception("Unexpected error reading distribution file: ", sys.exc_info()[0])

    return numpy.array(distribution)

def resample_distribution(x_values, y_values, new_dim):
    e_min = x_values[0]
    e_max = x_values[len(x_values)-1]

    new_x_values = e_min + numpy.arange(0, new_dim+1) * (e_max-e_min)/new_dim

    return new_x_values, numpy.interp(new_x_values, x_values, y_values)

def sample_from_distribution(distribution, npoints):
    if distribution[0, 0] == 0:
        y_values = distribution[1:, 1]
        x_values = distribution[1:, 0]
    else:
        y_values = distribution[:, 1]
        x_values = distribution[:, 0]
   
    coefficient = 1.0
    if len(x_values) < 10000:
        coefficient = 10000
        x_values, y_values = resample_distribution(x_values*10000, y_values, 10000)

  
    # normalize distribution function
    y_values /= numpy.max(y_values)
    y_values /= y_values.sum()

    random_generator = stats.rv_discrete(a=numpy.min(x_values), 
                                         b=numpy.max(x_values), 
                                         name='user_defined_distribution', values=(x_values, y_values))
        
    #plt.figure()
    #plt.plot(x_values, y_values, 'r')
    #plt.show()
    
    return random_generator.rvs(size=npoints)/coefficient

def generate_user_defined_distribution(beam_out, 
                                       user_defined_file, 
                                       axis=Axis.X, 
                                       distribution_type=Distribution.POSITION,
                                       minimum_value=-2e-5, 
                                       step=1e-6):
                                       
    distribution = extract_distribution_from_file(congruence.checkFile(user_defined_file))
        
    sampled_distribution = sample_from_distribution(distribution, len(beam_out._beam.rays))
    
    if distribution_type == Distribution.POSITION:
        if axis == Axis.X:
            axis_index = 0 
        elif axis == Axis.Z:
            axis_index = 2 
    elif distribution_type == Distribution.DIVERGENCE:
        if axis == Axis.X:
            axis_index = 4 
        elif axis == Axis.Z:
            axis_index = 6 

    beam_out._beam.rays[:, axis_index] = minimum_value + sampled_distribution*step
    
##########################################

shadow_beam = in_object_1

x_positions_file = "./x_positions.txt"

generate_user_defined_distribution(beam_out=shadow_beam, 
                                   user_defined_file=x_positions_file, 
                                   axis=Axis.X, 
                                   distribution_type=Distribution.POSITION, 
                                   minimum_value=-2e-5, 
                                   step=1e-6)


z_positions_file = "./z_positions.txt"

generate_user_defined_distribution(beam_out=shadow_beam, 
                                   user_defined_file=z_positions_file, 
                                   axis=Axis.Z, 
                                   distribution_type=Distribution.POSITION, 
                                   minimum_value=-1e-5, 
                                   step=0.5e-6)


x_divergences_file = "./x_divergences.txt"

generate_user_defined_distribution(beam_out=shadow_beam, 
                                   user_defined_file=x_divergences_file, 
                                   axis=Axis.X, 
                                   distribution_type=Distribution.DIVERGENCE, 
                                   minimum_value=-2e-5, 
                                   step=1e-6)


z_divergences_file = "./z_divergences.txt"

generate_user_defined_distribution(beam_out=shadow_beam, 
                                   user_defined_file=z_divergences_file, 
                                   axis=Axis.Z, 
                                   distribution_type=Distribution.DIVERGENCE, 
                                   minimum_value=-1e-5, 
                                   step=0.5e-6)


out_object = shadow_beam