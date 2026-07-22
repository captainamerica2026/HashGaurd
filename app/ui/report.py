# HashGuard Health Report


class Report:


    def generate(self, data):

        score = 0


        if data["battery"]["health"] == "GOOD":
            score += 30


        if data["hardware"]["storage"] == "Healthy":
            score += 30


        if data["thermal"]["status"] == "NORMAL":
            score += 30


        score += 10


        if score >= 90:
            status = "Excellent"

        elif score >= 70:
            status = "Good"

        else:
            status = "Needs Attention"



        return {

            "score": score,
            "status": status,
            "details": data

        }
