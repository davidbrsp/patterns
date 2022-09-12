from observer import Observer


class ObserverN(Observer):
    def receive_message(self, message) -> None:
        print(f"From observerN: {message}")
