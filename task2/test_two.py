from unittest import main, TestCase
from two import Person, get_depths


class TestTwo(TestCase):
    def test_two(self):
        person_a = Person("Fa", "La", None)
        person_b = Person("Fb", "Lb", person_a)
        d = {
            'key1': 1,
            'key2': {
                'key3': 1,
                'key4': {
                    'key5': 4,
                    'user': person_b
                }
            }
        }
        kd = []
        get_depths(d, kd)
        ex = [
            ('key1', 1), ('key2', 1),
            ('key3', 2), ('key4', 2),
            ('key5', 3), ('user', 3),
            ('first_name', 4), ('last_name', 4),
            ('father', 4), ('first_name', 5),
            ('last_name', 5), ('father', 5)
        ]
        self.assertEqual(ex, kd)


if __name__ == '__main__':
    main()
