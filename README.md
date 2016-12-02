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

For that default request parameters were here given.

Copy the example1-1.map mapfile, from the
totorial downloaded folder, to the base_path
location:

Original location:
    ms4w/apps/tutorial/htdocs/example1-1.map

The atribute SHAPEPATH of the mapfile copy
must be change according with the new location 
of the tutorial folder 'data' directory.
(relative path is here used)

SHAPEPATH      "ms4w/apps/tutorial/data"

The folowing tags had been added to the
MAP tag of the original mapfile:

PROJECTION # Projection definition:
   "init=epsg:4326"
END # End of the output Projection definition ---

WEB
  METADATA
    "ows_enable_request" "*"
  END
END


