import unittest

from src.classes.History import History


class HistoryTest(unittest.TestCase):
    def test_store(self):
        history: History = History()
        history.store(1, 2, 3)
        self.assertEqual(history.data, ["1 + 2 = 3"])


if __name__ == '__main__':
    unittest.main()
