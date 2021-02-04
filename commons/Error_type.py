

class TIMEOUT_ERROR(Exception):
    def __init__(self, err_msg):
        super().__init__(self)
        self.error = err_msg

    def __str__(self):
        return self.error

