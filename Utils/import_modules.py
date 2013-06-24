# Licensed under a 3-clause BSD style license - see LICENSE

# import general modules
import struct, getopt, sys
import os
from os import popen4, system, path
import glob
import types
import datetime
import operator
import string

# import numpy and scipy modules
import scipy
import scipy.weave
import scipy.ndimage
import scipy.optimize
import scipy.interpolate
import scipy.io
import scipy.constants
import scipy.stats
import numpy

# try to import ppgplot and Presto's Pgplot to enable some plotting capabilities
try:
    import Pgplot
    from Pgplot import plotxy, plot2d, plotbinned, nextplotpage, closeplot, resetdefaults, ppgplot
except:
    print( "Cannot import Pgplot. This is not a critical error, but some of the plotting functionalities might be impossible." )
try:
    import matplotlib, pylab
except:
    print( "Cannot import matplotlib/pylab. This is not a critical error, but some of the plotting functionalities might be impossible." )

# define some useful constants
cts = scipy.constants
cts.Msun = 1.9891e30
cts.Mjup = 1.8987e27
cts.Mearth = 5.9736e24
cts.Rsun = 695510000.0
cts.Rjup = 71492000.0
cts.Rearth = 6378000.0
cts.g_earth = 9.80665
cts.logg_earth = numpy.log10(cts.g_earth*100)
cts.g_sun = 27.94 * cts.g_earth
cts.logg_sun = numpy.log10(cts.g_sun*100)

# define more constants
ARCSECTORAD = float('4.8481368110953599358991410235794797595635330237270e-6')
RADTOARCSEC = float('206264.80624709635515647335733077861319665970087963')
SECTORAD    = float('7.2722052166430399038487115353692196393452995355905e-5')
RADTOSEC    = float('13750.987083139757010431557155385240879777313391975')
RADTODEG    = float('57.295779513082320876798154814105170332405472466564')
DEGTORAD    = float('1.7453292519943295769236907684886127134428718885417e-2')
RADTOHRS    = float('3.8197186342054880584532103209403446888270314977710')
HRSTORAD    = float('2.6179938779914943653855361527329190701643078328126e-1')
PI          = float('3.1415926535897932384626433832795028841971693993751')
TWOPI       = float('6.2831853071795864769252867665590057683943387987502')
PIBYTWO     = float('1.5707963267948966192313216916397514420985846996876')
SECPERDAY   = float('86400.0')
SECPERJULYR = float('31557600.0')
KMPERPC     = float('3.0856776e13')
KMPERKPC    = float('3.0856776e16')
Tsun        = float('4.925490947e-6') # sec
Msun        = float('1.9891e30')      # kg
Mjup        = float('1.8987e27')      # kg
Rsun        = float('6.9551e8')       # m
Rearth      = float('6.378e6')        # m
SOL         = float('299792458.0')    # m/s
MSUN        = float('1.989e+30')      # kg
G           = float('6.673e-11')      # m^3/s^2/kg 
C           = SOL




