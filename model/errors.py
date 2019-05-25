

class ScrappingErrors(Exception):
    def __init__(self, message):
        self.message = message


class InvalidTagError(ScrappingErrors):
    pass


class InvalidNewsApiError(Exception):
    def __init__(self, message):
        self.message = message


