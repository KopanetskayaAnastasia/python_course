'''
    Вариант 5.
'''
import osmium as osm
import pandas as pd


class OSMHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def tag_inventory(self, elem, elem_type):
        for tag in elem.tags:
            self.osm_data.append([elem_type,
                                  elem.id,
                                  elem.version,
                                  elem.visible,
                                  pd.Timestamp(elem.timestamp),
                                  elem.uid,
                                  elem.user,
                                  elem.changeset,
                                  len(elem.tags),
                                  tag.k,
                                  tag.v])

    def node(self, n):
        self.tag_inventory(n, "node")

    def way(self, w):
        self.tag_inventory(w, "way")

    def relation(self, r):
        self.tag_inventory(r, "relation")


osmhandler = OSMHandler()
osmhandler.apply_file("5.osm")
df_osm = pd.DataFrame(osmhandler.osm_data)
highway = df_osm[df_osm[9] == 'highway']


print(highway)

osmhandler.apply_file("5- 2.osm")
df_osm = pd.DataFrame(osmhandler.osm_data)
highway = df_osm[df_osm[9] == 'highway']


print(highway)

