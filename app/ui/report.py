# HashGuard Smart Health Report


class Report:


    def generate(self, data):

        score = 100


        # Battery check
        battery = data["battery"]

        if battery["status"] != "Detected":
            score -= 20



        # Storage check
        storage = data["hardware"]["storage_used"]

        if storage.endswith("%"):

            used = int(
                storage.replace("%","")
            )

            if used > 90:
                score -= 20

            elif used > 75:
                score -= 10



        # Thermal check
        if data["thermal"]["status"] != "NORMAL":

            score -= 15



        # Sensors check
        if len(data["sensors"]) < 3:

            score -= 10



        if score >= 90:

            status = "Excellent"

        elif score >= 70:

            status = "Good"

        elif score >= 50:

            status = "Warning"

        else:

            status = "Critical"



        return {

            "score": score,

            "status": status,

            "details": data

        }
