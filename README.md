# mapscript_testing

This is a python-mapscript adaptation to serve
the example_1.1 map of the mapserver tutorial.
(http://mapserver.org/tutorial/example1-1.html#example1-1)

Download the tutorial data from:
    http://download.osgeo.org/mapserver/docs/mapserver-tutorial.zip

Other reference websites:
    http://mapserver.org/tutorial/index.html
    https://github.com/mapserver/mapserver/wiki
    https://gist.github.com/tomkralidis/9adbd4864c03647aa7eb4f96a3c33297

The application is suposed to return a png map
as response for the given url:

localhost/ms-wsgi?service=WMS&version=1.3.0&request=GetMap

For that default request parameters were here given...


In future:
Implementation of a WFS with NetCDF file format: 
(https://www.nodc.noaa.gov/data/formats/netcdf/v2.0/)

