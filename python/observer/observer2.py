from observer import Observer


class Observer2(Observer):
    def receive_message(self, message) -> None:
        print(f"From observer2: {message}")
