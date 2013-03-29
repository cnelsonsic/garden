import json
import pickle

class Saveable(object):
    def save(self):
        data = pickle.dumps(self)
        with open("savegame.pkl", "wb") as f:
            f.write(data)
        print "wrote", len(data), "bytes to disk"

    def load(self):
        with open("savegame.pkl", "rb") as f:
            data = pickle.load(f)
        for k, v in data.__dict__.iteritems():
            print k, v
            setattr(self, k, v)
        print "done loading"
