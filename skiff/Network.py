

class SkiffNetwork(object):
    """SkiffNetwork"""
    def __init__(self, options=None, **kwargs):
        super(SkiffNetwork, self).__init__()
        if not options:
            options = kwargs

        self.__dict__.update(options)