class ClientMessage:
    def __init__(self, message: str) -> None:
        split = message.decode().split(",")

        self.behavior = split[0]

    def get_behavior(self):
        return self.behavior
