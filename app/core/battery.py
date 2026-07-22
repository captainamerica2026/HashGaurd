# HashGuard Battery Scanner

import psutil


class BatteryScanner:


    def scan(self):

        battery = psutil.sensors_battery()


        if battery:

            return {

                "level":
                str(battery.percent) + "%",

                "charging":
                str(battery.power_plugged),

                "status":
                "Detected"

            }


        return {

            "level":
            "Unknown",

            "charging":
            "Unknown",

            "status":
            "Not Available"

        }
