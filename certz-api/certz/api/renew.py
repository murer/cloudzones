from certz.util.keypair import KeyPair

class Renew(object):

    def __init__(self, domain):
        self._domain = domain

    def compute_key(self):
        if self._domain.privateKey:
            self._key = KeyPair.parse(self._domain.privateKey)
            return self
        self._key = KeyPair.create()
        self._domain.privateKey = self._key.export_private_key()
        return self
