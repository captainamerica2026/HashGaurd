# HashGuard Dashboard Data


class Dashboard:


    def __init__(self):

        self.cards = []


    def update(self, report):

        data = report["details"]


        self.cards = [

            {
                "icon": "🔋",
                "name": "Battery",
                "value": data["battery"]["health"]
            },


            {
                "icon": "🌡",
                "name": "Thermal",
                "value": data["thermal"]["temperature"]
            },


            {
                "icon": "⚙",
                "name": "Hardware",
                "value": "GOOD"
            },


            {
                "icon": "💾",
                "name": "Storage",
                "value": data["hardware"]["storage"]
            }

        ]


        return self.cards
