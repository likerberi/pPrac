import shapefile
import json

# with open("Z_SOP_BND_ADM_DONG_PG.shx", "rb") as f:
#   myshx = f.read()
# with open("Z_SOP_BND_ADM_DONG_PG.shp", "rb") as f:
#   myshp = f.read()
# with open("Z_SOP_BND_ADM_DONG_PG.dbf", "rb") as f:
#   mydbf = f.read()

path = 'Z_SOP_BND_ADM_DONG_PG'
sf = shapefile.Reader(path, encoding='EUC-KR')
#sf = shapefile.Reader(shx="Z_SOP_BND_ADM_DONG_PG.shx", dbf="Z_SOP_BND_ADM_DONG_PG.dbf", shp="Z_SOP_BND_ADM_DONG_PG.shp")
fields = sf.fields[1:]
fields_names = [field[0] for field in fields]

buffer = []
for sr in sf.shapeRecords():
    atr = dict(zip(fields_names, sr.record))

    geo = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature", geometry=geo, properties=atr))

geojson = open("pyshp-sample.geojson", "w")
geojson.write(json.dumps({"type": "FeatureCollection", "features": buffer}, indent=2, ensure_ascii=False))
geojson.close()