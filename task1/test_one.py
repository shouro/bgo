from unittest import main, TestCase
from one import get_depths

class TestOne(TestCase):
    def test_one(self):
        d = {
            'key1': 1,
            'key2': {
                    'key3': 1,
                    'key4': {
                        'key5': 4
                    }
            }
        }
        kd = []
        get_depths(d, kd)
        prime = [('key1', 1), ('key2', 1), ('key3', 2), ('key4', 2), ('key5', 3)]
        self.assertEqual(prime, kd)

if __name__ == '__main__':
    main()

