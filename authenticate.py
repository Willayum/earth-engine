import ee
import geemap


def main():
    ee.Authenticate()
    ee.Initialize()

    print(ee.Image("NASA/NASADEM_HGT/001").get("title").getInfo())

if __name__ == '__main__':
    main()

    ########################################################
map = geemap.Map()
print(map)

    # feature = ee.Feature(map)
    #
    # print("Map ID:")
    # print(feature.getMapId())
