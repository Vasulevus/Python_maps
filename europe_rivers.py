import os
import geopandas
import glob
import dload

path = ""
list = []

def load(url,filename,path=path):
    global list
    if not os.path.exists(filename):
        dload.save_unzip(url)
    path = os.getcwd()
    list = glob.glob(path + '/**/*.shp', recursive=True) 

address = r"https://data.hydrosheds.org/file/HydroRIVERS/HydroRIVERS_v10_eu_shp.zip"
name = r"HydroRIVERS_v10_eu_shp.zip"
load(address,name)
a = list[0]
table = geopandas.read_file(a)
df = geopandas.GeoDataFrame(table)
df

