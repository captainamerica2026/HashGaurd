# HashGuard UI Card Component


class HealthCard:


    def __init__(self, title, value):

        self.title = title
        self.value = value


    def display(self):

        return (
            self.title
            + ": "
            + self.value
        )
