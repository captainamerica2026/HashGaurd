# HashGuard Hardware Scanner

import platform
import psutil


class HardwareScanner:


    def scan(self):

        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")


        return {

            "cpu":
            platform.processor(),


            "ram":
            str(round(memory.total / (1024**3), 2))
            + " GB",


            "ram_usage":
            str(memory.percent)
            + "%",


            "storage":
            str(round(disk.total / (1024**3), 2))
            + " GB",


            "storage_used":
            str(disk.percent)
            + "%"

        }
