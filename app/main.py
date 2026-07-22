# HashGuard Main Interface

from ui.dashboard import Dashboard
from ui.radar import RadarScanner
from ui.report import Report


class HashGuardApp:

    def __init__(self):
        self.dashboard = Dashboard()
        self.radar = RadarScanner()
        self.report = Report()


    def start(self):

        print("🛡 HASHGUARD")
        print("Device Health Intelligence System")
        print("--------------------------------")

        self.radar.start()

        self.radar.scan_modules()

        result = self.report.generate(87)

        print("\nDEVICE REPORT")
        print("Score:", result["score"])
        print("Status:", result["status"])



if __name__ == "__main__":

    app = HashGuardApp()

    app.start()
