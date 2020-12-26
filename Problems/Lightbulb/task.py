class Lightbulb:
    def __init__(self):
        self.state = "off"
        self.change_status = None

    # create method change_state here
    def change_state(self):
        if self.state == "off":
            print("Turning the light on")
            self.state = "on"
        else:
            print("Turning the light off")
            self.state = "off"
