# HashGuard Android Device Info

import platform


class AndroidDevice:


    def scan(self):

        return {

            "device":
            platform.machine(),

            "system":
            platform.system(),

            "version":
            platform.version()

        }
