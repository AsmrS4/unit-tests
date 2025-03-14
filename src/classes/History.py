class History:

    def __init__(self):
        self.data = []

    def store(self, a, b, result):
        self.data.append(self.__stringify(a, b, result));

    def __stringify(self, a, b, result):
        return str(a) + " + " + str(b) + " = " + str(result);
