def get_depths(d, l, level=1):
    for k in d:
        l.append((k,level))
        if isinstance(d[k], dict):
            get_depths(d[k], l, level + 1)

def print_depth(l):
    for k, d in l:
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
            l = []
            get_depths(d, l)
            print_depth(l)

if __name__ == "__main__":
    one()
