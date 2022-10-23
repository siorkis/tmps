import domain


# Factory pattern
def Factory(language="English"):
    """Factory Method"""
    localizers = {
        "French": domain.FrenchLocalizer,
        "English": domain.EnglishLocalizer,
        "Spanish": domain.SpanishLocalizer,
    }

    return localizers[language]()


f = Factory("French")
e = Factory("English")
s = Factory("Spanish")

message = domain.Singleton.get_message()

for msg in message:
    print(f.localize(msg))
    print(e.localize(msg))
    print(s.localize(msg))
