import geopandas as gpd

shapefile = 'H:\\Pycharm\\CS work\\World Data\\ne_110m_admin_0_countries.shp'

#read shapefile using Geopandas
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]

#rename the columns
gdf.columns = ['country', 'country_code', 'geometry']
gdf.head()