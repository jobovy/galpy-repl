# A set of Python commands to pre-run for the galpy.org/repl redirect
# Install galpy
import micropip
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
%matplotlib inline