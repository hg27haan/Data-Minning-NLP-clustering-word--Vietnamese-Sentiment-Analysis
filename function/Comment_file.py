class Comment:
    def __init__(self,comment=None,predict=None):
        self._comment=comment 
        self._predict=predict
    @property
    def getPredict(self):
        return self._predict
    @property
    def getComment(self):
        return self._comment