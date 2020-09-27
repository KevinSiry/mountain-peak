class NotFoundException(Exception):
    error_message = None

    def __init__(self, error_message):
        Exception.__init__(self)
        self.error_message = error_message

    def to_dict(self):
        return {'errors': self.error_message}


class InvalidParametersException(Exception):
    error_message = None

    def __init__(self, error_message):
        Exception.__init__(self)
        self.error_message = error_message

    def to_dict(self):
        return {'errors': self.error_message}
