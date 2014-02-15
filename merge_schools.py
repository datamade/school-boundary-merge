from cStringIO import StringIO
import shapefile
import json
import zipfile
from itertools import izip_longest
import os

SCHOOLS = []


def extract_schools(arg, d, files):
    geo = {'type': 'FeatureCollection', 'features': []}
    for f in files:
        shp = StringIO()
        dbf = StringIO()
        shx = StringIO()
        if f.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(d, f)) as zf:
                for name in zf.namelist():
                    if name.endswith('.shp'):
                        shp.write(zf.read(name))
                    if name.endswith('.shx'):
                        shx.write(zf.read(name))
                    if name.endswith('.dbf'):
                        dbf.write(zf.read(name))
            shape_reader = shapefile.Reader(shp=shp, dbf=dbf, shx=shx)
            records = shape_reader.shapeRecords()
            # print shape_reader.fields
            fields = [f[0] for f in shape_reader.fields[1:7]]
            for record in records:
                if record:
                    properties = {}
                    for k,v in zip(fields, record.record):
                        properties[k] = v
                    dump = {
                        'type': 'Feature', 
                        'geometry': record.shape.__geo_interface__,
                        'id': properties['OBJECTID'],
                        'properties': properties
                    }
                    if properties['SCHOOLID'] not in SCHOOLS:
                        geo['features'].append(dump)
                        SCHOOLS.append(properties['SCHOOLID'])
    outp = open('all_schools.geojson', 'wb')
    outp.write(json.dumps(geo))
    outp.close()
    return geo

if __name__ == "__main__":
    d = os.path.join(os.path.curdir, 'source_data/data_portal')
    os.path.walk(d, extract_schools, None)
