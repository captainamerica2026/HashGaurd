# HashGuard Master Scanner

from core.thermal import ThermalScanner
from core.battery import BatteryScanner
from core.hardware import HardwareScanner


class Scanner:


    def __init__(self):

        self.battery = BatteryScanner()
        self.hardware = HardwareScanner()



    def scan(self):

        print("HashGuard Deep Scan Started")

        result = {

            "battery":
            self.battery.scan(),


            "hardware":
            self.hardware.scan()

        }


        print("Scan Complete")

        return result
