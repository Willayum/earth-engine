import ee


def main():
    ee.Authenticate()
    ee.Initialize()

    print(ee.Image("NASA/NASADEM_HGT/001").get("title").getInfo())


if __name__ == '__main__':
    main()
