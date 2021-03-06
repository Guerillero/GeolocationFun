# Pro Tip: You have to run this directly from ArcMap
# This should output the dataset that I use for my work.

__author__ = 'Tom Fish <guerillero.net>'
__copyright__ = '(c) 2014 by Tom Fish'
__licence__ = 'MIT'

# Script starts here
import arcpy
from arcpy import env
from arcpy.sa import *

# Fix the file paths.
points = "E:\Documents\GIS\Wikipedia\wiki.gdb\PointsWGS84"
counties = "E:\Documents\GIS\Wikipedia\wiki.gdb\US_Counties"
output = "E:\Documents\GIS\Wikipedia\wiki.gdb\countiesWithArticles"
KDOut = "E:\Documents\GIS\Wikipedia\wiki.gdb\KD"

# setup
mxd = arcpy.mapping.MapDocument('CURRENT')
PntLyr = arcpy.mapping.Layer('points')
PntLyr.name = "Point Layer"
PolyLyr = arcpy.mapping.Layer('counties')
PolyLyr.name = "County Layer"

if PntLyr.name == "PointsLayer":
    # I only want/need to see the points on earth. This should speed this up quite a bit
    PntLyr.definitionQuery = "'globe' = 'earth'"
    # Do the join and save it
    arcpy.SpatialJoin_analysis(PolyLyr, PntLyr, output)
    # Do the KD and then save it
    KD = KernelDensity(PntLyr, "NONE")
    KD.save(KDOut)

