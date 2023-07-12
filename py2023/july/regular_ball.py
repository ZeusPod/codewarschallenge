class Ball:
    def __init__(self, object='regular'):
        self.object = object

    def ball_type(self):
        if not object:
            return 'regular'
        else:
            return self.object



miball = Ball('super')
print(miball.ball_type())
