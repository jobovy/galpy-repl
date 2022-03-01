# A set of Python commands to pre-run for the galpy.org/repl redirect
# Monkey-patch the pyodide astropy
import sys
sys.modules['_ssl']= object
sys.modules['_microprocessing']= object
sys.modules['_yaml']= object
# Install astroquery
import micropip
await micropip.install('astroquery')
# Install galpy
await micropip.install('https://www.galpy.org/wheelhouse/galpy-latest-py3-none-any.whl')
# Turn off warnings
import warnings
from galpy.util import galpyWarning
warnings.simplefilter(action='ignore',category=galpyWarning)
# Import units from astropy to have them handy
from astropy import units
import astropy.units as u
# Set up galpy to return outputs as astropy Quantities
import galpy.util.conversion
galpy.util.conversion._APY_UNITS=True
# Also need to set the following, because pyodide SkyCoord failure prevents this from being set correctly in Orbits
import galpy.orbit.Orbits
galpy.orbit.Orbits._APY_LOADED= True
# Inline plots
%matplotlib inline
