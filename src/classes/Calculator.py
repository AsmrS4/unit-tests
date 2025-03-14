from src.classes.History import History


class Calculator:
    def __init__(self):
        self.history = History();

    def sum(self, a, b):
        result = a + b;
        self.history.store(a, b, result);
        return result;
