from subject import Subject
from observer1 import Observer1
from observer2 import Observer2
from observern import ObserverN

if __name__ == "__main__":

    subject = Subject()
    observers = [Observer1(), Observer2(), ObserverN()]

    for observer in observers:
        subject.subscribe(observer)

    for observer in observers:
        subject.notify("Hello world observers!")
        subject.unsubscribe(observer)
        print("\n")
