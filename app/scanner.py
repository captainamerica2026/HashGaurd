# HashGuard Master Scanner

from core.sensors import SensorScanner 
from core.thermal import ThermalScanner
from core.battery import BatteryScanner
from core.hardware import HardwareScanner


class Scanner:


    def __init__(self):

        self.battery = BatteryScanner()
        self.hardware = HardwareScanner()
        self.thermal = ThermalScanner()
        self.sensors = SensorScanner()

    def scan(self):

        print("HashGuard Deep Scan Started")

        result = {

    "battery":
    self.battery.scan(),

    "hardware":
    self.hardware.scan(),

    "thermal":
    self.thermal.scan()

      "sensors":
    self.sensors.scan()
        }


        print("Scan Complete")

        return result
