from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

from ui.radar import Radar


KV = """

MDScreen:

    md_bg_color: 0.02,0.02,0.03,1


    FloatLayout:


        MDLabel:

            text: "🛡 HASHGUARD"

            halign: "center"

            pos_hint:
                {"center_y":0.9}

            font_style:
                "H3"

            theme_text_color:
                "Custom"

            text_color:
                0,0.8,1,1



        MDLabel:

            text:
                "Device Health Intelligence"

            halign:
                "center"

            pos_hint:
                {"center_y":0.82}



        FloatLayout:

            id:
                radar_area

            size_hint:
                1,.45

            pos_hint:
                {"center_y":0.52}



        MDRaisedButton:

            id:
                scan_button


            text:
                "📡 SCAN"


            size_hint:
                .4,.12


            pos_hint:

                {"center_x":0.5,"center_y":0.15}


            on_release:

                app.start_scan()



        MDLabel:

            id:
                status


            text:
                "System Ready"


            halign:
                "center"


            pos_hint:

                {"center_y":0.05}


"""


class HashGuard(MDApp):


    def build(self):

        self.theme_cls.theme_style="Dark"

        screen = Builder.load_string(KV)

        self.radar = Radar()

        screen.ids.radar_area.add_widget(
            self.radar
        )

        return screen



    def start_scan(self):

    from scanner import Scanner
    from ui.report import Report


    self.root.ids.status.text = (
        "📡 Deep Scan Running..."
    )


    scanner = Scanner()

    data = scanner.scan()


    report = Report()

    result = report.generate(data)


    self.root.ids.status.text = (
        "🛡 Score: "
        + str(result["score"])
        + "/100  "
        + result["status"]
    )


HashGuard().run()
