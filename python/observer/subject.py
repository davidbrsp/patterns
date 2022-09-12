class Subject:
    observers = []

    def subscribe(self, subscriber) -> None:
        self.observers.append(subscriber)

    def unsubscribe(self, subscriber) -> None:
        self.observers.remove(subscriber)

    def notify(self, message: str) -> None:
        for observer in self.observers:
            observer.receive_message(message)
