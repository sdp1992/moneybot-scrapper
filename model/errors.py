

class ScrappingErrors(Exception):
    def __init__(self, message):
        self.message = message


class UnableToExtractError(ScrappingErrors):
    pass


