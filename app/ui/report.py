# HashGuard Report Generator


class Report:


    def generate(self, score):

        if score >= 90:
            status = "Excellent"

        elif score >= 70:
            status = "Good"

        else:
            status = "Needs Attention"


        return {
            "score": score,
            "status": status
        }
