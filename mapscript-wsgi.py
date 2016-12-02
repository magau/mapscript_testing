#!/usr/bin/env python
#-*-coding:utf8-*-
"""# This is a python-mapscript adaptation to serve
# the example_1.1 map of the mapserver tutorial.
# (http://mapserver.org/tutorial/example1-1.html#example1-1)
# Download the tutorial data from:
# http://download.osgeo.org/mapserver/docs/mapserver-tutorial.zip
 
# Other reference websites:
#     http://mapserver.org/tutorial/index.html
#     https://github.com/mapserver/mapserver/wiki
#     https://gist.github.com/tomkralidis/9adbd4864c03647aa7eb4f96a3c33297

# The application is suposed to return a png map
# as response for the given url:
#
# localhost/ms-wsgi?service=WMS&version=1.3.0&request=GetMap
#
# For that default request parameters were here given.

# Copy the example1-1.map mapfile, from the
# totorial downloaded folder, to the base_path
# location:
# 
# Original location:
#     ms4w/apps/tutorial/htdocs/example1-1.map
# 
# The atribute SHAPEPATH of the mapfile copy
# must be change according with the new location 
# of the tutorial folder 'data' directory.
# (relative path is here used)
# 
# SHAPEPATH      "ms4w/apps/tutorial/data"
 
# The folowing tags had been added to the
# MAP tag of the original mapfile:
# 
# PROJECTION # Projection definition:
#    "init=epsg:4326"
# END # End of the output Projection definition ---
# 
# WEB
#   METADATA
#     "ows_enable_request" "*"
#   END
# END
"""

import os
import sys

import mapscript

# Edit the 'base_path' value according with yours:
settings_local = {
    'base_path':'/<user>/<base>/<dir>'
}


# List of all environment variable used by MapServer
MAPSERV_ENV = [
  'CONTENT_LENGTH', 'CONTENT_TYPE', 'CURL_CA_BUNDLE', 'HTTP_COOKIE',
  'HTTP_HOST', 'HTTPS', 'HTTP_X_FORWARDED_HOST', 'HTTP_X_FORWARDED_PORT',
  'HTTP_X_FORWARDED_PROTO', 'MS_DEBUGLEVEL', 'MS_ENCRYPTION_KEY',
  'MS_ERRORFILE', 'MS_MAPFILE', 'MS_MAPFILE_PATTERN', 'MS_MAP_NO_PATH',
  'MS_MAP_PATTERN', 'MS_MODE', 'MS_OPENLAYERS_JS_URL', 'MS_TEMPPATH',
  'MS_XMLMAPFILE_XSLT', 'PROJ_LIB', 'QUERY_STRING', 'REMOTE_ADDR',
  'REQUEST_METHOD', 'SCRIPT_NAME', 'SERVER_NAME', 'SERVER_PORT'
]


def application(env, start_response):
    for key in MAPSERV_ENV:
        if key in env:
            os.environ[key] = env[key]
        else:
            os.unsetenv(key)

    # Using a statically assigned mapfile:
    filename = os.path.join( settings_local['base_path'], 'test_mapfile.map')
    mapfile = mapscript.mapObj(filename)

    req = mapscript.OWSRequest()
    mapscript.msIO_installStdoutToBuffer()

    req.loadParamsFromURL(env['QUERY_STRING'])
    set_default_parameters(req)

    try:
        status = mapfile.OWSDispatch(req)
    except Exception as err:
        pass

    content_type = mapscript.msIO_stripStdoutBufferContentType()
    result = mapscript.msIO_getStdoutBufferBytes()
    start_response('200 OK', [('Content-type', content_type)])
    return [result]

def set_default_parameters(req):
    # Parameters from url overwrite the default
    # values.
    default_p = {
        "LAYERS": 'states',
        # The folowing crs (EPSG:4326) require lon/lat bbox
        # (http://mapserver.org/uk/ogc/wms_server.html)
        "CRS"   : 'EPSG:4326',
        "BBOX"  : '41.619778,-97.238976,49.385620,-82.122902',
        ## The folowing crs (CRS:84) require lat/lon bbox
        #"CRS"   : 'CRS:84',
        #"BBOX"  : '-97.238976,41.619778,-82.122902,49.385620',
        "FORMAT": 'image/png',
        "WIDTH" : '600',
        "HEIGHT": '400'
    }

    for p_name, p_value in default_p.iteritems():
        if req.getValueByName(p_name) is None:
            req.setParameter(p_name, p_value)
            


if __name__ == '__main__':  # run inline using WSGI reference implementation
    from wsgiref.simple_server import make_server
    port = 8001
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    httpd = make_server('', port, application)
    print('Serving on port %d...' % port)
    httpd.serve_forever()
