from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation


KV = """

MDScreen:

    md_bg_color: 0.02,0.02,0.03,1


    MDBoxLayout:

        orientation: "vertical"
        padding: "25dp"
        spacing: "20dp"


        MDLabel:

            text: "🛡 HASHGUARD"

            halign: "center"

            font_style: "H3"

            theme_text_color: "Custom"

            text_color: 0,0.8,1,1



        MDLabel:

            text: "Device Health Intelligence"

            halign: "center"



        MDCard:

            size_hint: .8,.25

            pos_hint:
                {"center_x":0.5}

            md_bg_color:
                0.05,0.05,0.08,1


            MDLabel:

                text:

                    "DEVICE SCORE\\n\\n87 / 100"

                halign:

                    "center"

                font_style:

                    "H4"



        Widget:



        MDRaisedButton:

            id: radar_button

            text:

                "📡\\nSCAN"

            font_size:

                "28sp"


            size_hint:

                .5,.4


            pos_hint:

                {"center_x":0.5}


            on_release:

                app.scan()



        MDLabel:

            id: status

            text:

                "System Ready"

            halign:

                "center"


"""


class HashGuard(MDApp):


    def build(self):

        self.theme_cls.theme_style="Dark"

        return Builder.load_string(KV)



    def scan(self):

        btn=self.root.ids.radar_button

        anim=Animation(
            opacity=.3,
            duration=.5
        )

        anim += Animation(
            opacity=1,
            duration=.5
        )

        anim.repeat=True

        anim.start(btn)


        self.root.ids.status.text = (
            "📡 Scanning Device..."
        )



HashGuard().run()
