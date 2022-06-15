# A set of Python commands to pre-run for the galpy.org/repl redirect
# Install astroquery
import micropip
await micropip.install('astroquery')
# Install galpy
import pyodide_js
await pyodide_js.loadPackage(['numpy','scipy','matplotlib','astropy','future','setuptools','https://www.galpy.org/wheelhouse/galpy-latest-cp310-cp310-emscripten_wasm32.whl'])
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
