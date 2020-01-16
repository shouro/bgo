class Person():
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def get_depths(d, klp, level=1):
    for k in d:
        klp.append((k, level))
        if isinstance(d[k], dict):
            get_depths(d[k], klp, level + 1)
        elif isinstance(d[k], Person):
            get_depths(vars(d[k]), klp, level + 1)


def print_depth(klp):
    for k, d in klp:
        print(k, d)


def two():
    person_a = Person("Fa", "La", None)
    person_b = Person("Fb", "Lb", person_a)

    dd = [
        {
            'key1': 1,
            'key2': {
                'key3': 1,
                'key4': {
                    'key5': 4,
                    'user': person_b
                }
            }
        }
    ]

    for d in dd:
        if isinstance(d, dict):
            klp = []
            get_depths(d, klp)
            print_depth(klp)


if __name__ == "__main__":
    two()
