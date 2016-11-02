import numpy as np
import numpy.random as rand
import matplotlib.pyplot as pp
import sys
import scipy.interpolate as intp

seed = None#1844
e_0 = None#0.01
i_0 = None#0.5#*np.pi/180.
mass = 0.02 *  0.000003003 #0.0167 * 0.000003003

if len(sys.argv) != 5:
    print "I need four arguments to this code!  "
    print "   - The number of protoplanets"
    print "   - The random seed value"
    print "   - The initial eccentricity scale"
    print "   - The initial inclination scale (degrees)"
    print "I only got "  + str(len(sys.argv) - 1) + " arguments"
    quit()

number = int(sys.argv[1])
seed = int(sys.argv[2])
rand.seed(seed)
e_0 = float(sys.argv[3])
i_0 = float(sys.argv[4])

if number not in (150, 300, 75):
    print "You aren't giving me an input of 150, 300, or 75"
    print "If you're sure about this, and want to proceed, change the code"
    print "Now quitting..."
    quit()

cusp = "0.01"
m = 544.331054/(.015-.005)
b = -m*.005
def sigma_1(a):
    if a < 0.005 or a > 0.04:
        return 0.
    if a < 0.015:
        return m*a + b
    else:
        return np.power(a,-1.5)

"""def sigma_2(a,amin,amax): #Note: this has arbitrary normalization
    a_temp = a
    zero_point_seven_equivalent = 0.7/1.7*(amax-amin) + amin
    if a_temp < amin or a_temp > amax:
        return 0.
    if a_temp < zero_point_seven_equivalent:
        slope = 1/(zero_point_seven_equivalent - amin)
        b = -slope*amin
        return slope * a_temp + b 
    else:
        #return 8.*np.power(a_temp,-1.5)
        A_ = 1.3/(amax - zero_point_seven_equivalent)
        B_ = 0.7 - A_*zero_point_seven_equivalent
        divide_by_factor = np.power(A_*zero_point_seven_equivalent + B_,-1.5)
        #print A_*a_temp + B_
        return np.power(A_*a_temp + B_,-1.5)/divide_by_factor"""

a_distribution = np.linspace(.0050000000000001,0.04,5500)
sigma_distribution = []
sigmas = []
cumulative = 0.
for i in range(len(a_distribution)):
    cumulative+=sigma_1(a_distribution[i])
    sigmas.append(sigma_1(a_distribution[i]))
    sigma_distribution.append(cumulative)

print sigmas[0]
print sigmas[1]
print a_distribution[np.argmax(sigmas)]

#pp.plot(a_distribution,sigmas)
#pp.show()
    
sigma_distribution = np.subtract(sigma_distribution,sigma_distribution[0])
sigma_distribution = np.divide(sigma_distribution,sigma_distribution[-1])

a_func_sigma = intp.interp1d(sigma_distribution,a_distribution)
midpoints = np.linspace(0.,1.,number+1)
for i in range(number):
    midpoints[i] = (midpoints[i] + midpoints[i+1])/2.0
a_to_start_out = a_func_sigma(midpoints)

#s = 'Initial_aes/initial_a_sim1_' + str(number) + '.txt'
#np.savetxt(s,np.transpose(a_to_start_out))

#Now, for the rest of the orbital elements:

eccentricity = rand.rayleigh(scale=e_0,size=number)
inclination = rand.rayleigh(scale=i_0,size=number)
capital_omega = rand.random(number)
capital_omega = np.multiply(capital_omega,2.*180.)#np.pi)
omega = rand.random(number)
omega = np.multiply(omega,2.*180.)#np.pi)
mean_anomaly = rand.random(number)
mean_anomaly = np.multiply(mean_anomaly,2.*180.)#np.pi)

particle_number = 2

f = open('big.in','w')

f.write(')O+_06 Big-body initial data\n')
f.write(')  seed value: ' + str(seed) + ', cusp: ' + cusp + '\n')
f.write(')----------------------------------------\n')
f.write(' style (Cartesian, Asteroidal, Cometary) = Asteroidal\n')
f.write(' epoch (in days) = 0.\n')
f.write(')-----------------------------------------\n')

for i in range(number):
    f.write(str(particle_number) + '    m=' + '%E' % mass + ' r=1.0D0' + ' d=3.0' + '\n')
    f.write(' %E  %E  %E\n' % (a_to_start_out[i], eccentricity[i], inclination[i]))
    f.write(' %E  %E  %E\n' % (omega[i], capital_omega[i], mean_anomaly[i]))
    f.write(' 0. 0. 0.\n')
    particle_number += 1

