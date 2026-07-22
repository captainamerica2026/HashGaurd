# HashGuard Radar Scanner

class RadarScanner:

    def start(self):

        print("📡 Radar activated")
        print("Scanning device...")


    def scan_modules(self):

        modules = [
            "Battery",
            "CPU",
            "RAM",
            "Storage",
            "Sensors",
            "Temperature"
        ]

        for module in modules:
            print("Scanning:", module)


        return True
