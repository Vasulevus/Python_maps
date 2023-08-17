import requests

url = r"https://data.hydrosheds.org/file/HydroRIVERS/HydroRIVERS_v10_eu_shp.zip"


local_file = 'HydroRIVERS_v10_eu_shp.zip'

a = requests.get(url=url)

open(local_file, "wb").write(a.content)

