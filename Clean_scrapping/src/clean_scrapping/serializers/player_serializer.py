import json

class PlayerEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            return o.__dict__
        except AttributeError:
            return super().default(o)
