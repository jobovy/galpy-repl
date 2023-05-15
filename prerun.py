# A set of Python commands to pre-run for the galpy.org/repl redirect
# Install astroquery
import micropip
await micropip.install('astroquery')
# Install galpy
import pyodide_js
await pyodide_js.loadPackage(['numpy','scipy','matplotlib','astropy','future','setuptools','https://www.galpy.org/wheelhouse/galpy-latest-cp310-cp310-emscripten_3_1_14_wasm32.whl'])
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
