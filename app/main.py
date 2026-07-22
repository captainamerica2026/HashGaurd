from ui.radar_screen import RadarScreen
from kivymd.app import MDApp
from kivy.lang import Builder

from scanner import Scanner
from ui.report import Report
from ui.dashboard import Dashboard


KV = """

MDScreen:

    md_bg_color: 0.02,0.02,0.03,1


    MDBoxLayout:

        orientation: "vertical"
        padding: "20dp"
        spacing: "15dp"


        MDLabel:
            text: "🛡 HASHGUARD"
            halign: "center"
            font_style: "H3"
            theme_text_color: "Custom"
            text_color: 0,0.8,1,1


        MDLabel:
            text: "Device Health Intelligence"
            halign: "center"


        MDLabel:
            id: score
            text: "Health Score: --"
            halign: "center"
            font_style: "H4"


        MDLabel:
            id: cards
            text: "Ready to scan"
            halign: "center"


        Widget:


        MDRaisedButton:

            text: "📡 SCAN"

            pos_hint:
                {"center_x":0.5}


            on_release:
                app.start_scan()



"""


class HashGuard(MDApp):


    def build(self):

        self.theme_cls.theme_style="Dark"

        return Builder.load_string(KV)



    def start_scan(self):

        scanner = Scanner()

        data = scanner.scan()


        report = Report()

        result = report.generate(data)


        dashboard = Dashboard()

        cards = dashboard.update(result)


        self.root.ids.score.text = (
            "Health Score: "
            + str(result["score"])
            + "/100"
        )


        text = ""

        for card in cards:

            text += (
                card["icon"]
                +" "
                +card["name"]
                +" : "
                +card["value"]
                +"\n"
            )


        self.root.ids.cards.text = text



HashGuard().run()
