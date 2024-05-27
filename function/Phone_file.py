class Phone:
    def __init__(self, id=None, phone_name=None):
        self._id = id
        self._phone_name = phone_name
    @property
    def getId(self):
        return self._id
    @property
    def get_phone_name(self):
        return self._phone_name
    