# A set of Python commands to pre-run for the galpy.org/repl redirect
# Install astroquery
import micropip
await micropip.install('astroquery')
# Install galpy, first need to uninstall the version that comes with pyodide
micropip.uninstall('galpy',verbose=True)
await micropip.install(['numpy','scipy','matplotlib','astropy','future','setuptools','https://www.galpy.org/wheelhouse/galpy-1.11.1.dev0-cp312-cp312-pyodide_2024_0_wasm32.whl'],verbose=True)
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
# Get astroquery in Orbit.from_name to work by using pyodide-http
await micropip.install(["ssl","pyodide-http>=0.2.1"])
import pyodide_http
pyodide_http.patch_all()
# Currently need to reload these http and urllib libraries (see koenvo/pyodide-http/issues/33)
from importlib import reload
import http.client
import urllib.request
reload(http.client)
reload(urllib.request)
# Inline plots
%matplotlib inline
