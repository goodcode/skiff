

class SkiffAction(object):
    """SkiffAction"""
    def __init__(self, options=None, **kwargs):
        super(SkiffAction, self).__init__()
        if not options:
            options = kwargs

        self.__dict__.update(options)