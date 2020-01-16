def get_depths(d, klp, level=1):
    for k in d:
        klp.append((k, level))
        if isinstance(d[k], dict):
            get_depths(d[k], klp, level + 1)


def print_depth(klp):
    for k, d in klp:
        print(k, d)


def one():
    dd = [
        {
            'key1': 1,
            'key2': {
                    'key3': 1,
                    'key4': {
                        'key5': 4
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
    one()
