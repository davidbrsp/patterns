from observer import Observer


class Observer1(Observer):
    def receive_message(self, message) -> None:
        print(f"From observer1: {message}")
