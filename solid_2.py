# Builder Pattern
class Local:

    def __init__(self):
        self.localize(msg="hello")
        self.translate()

    def localize(self, msg):
        raise NotImplementedError

    def translate(self):
        raise NotImplementedError


class FrenchLocalizer(Local):
    translations = {"car": "voiture", "bike": "bicyclette",
                    "cycle": "cyclette"}

    def translate(self):
        pass

    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer(Local):
    translations = {"car": "coche", "bike": "bicicleta",
                    "cycle": "ciclo"}

    def translate(self):
        pass

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer(Local):
    translations = {"car": "car", "bike": "bike",
                    "cycle": "cycle"}

    def translate(self):
        pass

    def localize(self, msg):
        return self.translations.get(msg, msg)


# singleton pattern
class Singleton:
    message = ["car", "bike", "cycle"]

    @staticmethod
    def get_message():
        return Singleton.message


# Factory pattern
def Factory(language="English"):
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()


if __name__ == "__main__":

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = Singleton.get_message()

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
