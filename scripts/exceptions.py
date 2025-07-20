

class AnimationManagerAmountError(Exception):
    def __init__(self, attrname, expected, actual):
        super().__init__("Expected %d of %ss, got %d" % (expected, attrname, actual))
        
