class ClientMessage:
    def __init__(self, message: str) -> None:
        split = message.decode().split(",")

        self.behavior = split[0]
        self.use_item = split[1]
        self.timestamp = split[2]

    def get_behavior(self):
        return self.behavior

    def get_use_item_flag(self):
        return self.use_item

    def get_timestamp(self):
        return self.timestamp
    