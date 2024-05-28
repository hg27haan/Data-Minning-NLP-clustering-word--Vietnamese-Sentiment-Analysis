class Phone:
    def __init__(self, id=None, phone_name=None, specifications=None):
        self._id = id
        self._phone_name = phone_name
        self._specifications = specifications
    @property
    def getId(self):
        return self._id
    @property
    def getPhoneName(self):
        return self._phone_name
    @property
    def getSpecifications(self):
        return self._specifications
    