class MockDb:

    def __init__(self):
        pass

    def search(self, searchOptions):
        return [(0, "fake row", 0.0)]

