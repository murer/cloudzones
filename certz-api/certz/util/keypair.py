from Crypto.PublicKey import RSA

class KeyPair(object):

    @classmethod
    def create(cls):
        ret = cls()
        ret._key = RSA.generate(2048)
        return ret

    @classmethod
    def parse(cls, private_key):
        ret = cls()
        ret._key = RSA.importKey(private_key)
        return ret

    def export_private_key(self):
        return self._key.exportKey('PEM')

    def export_public_key(self):
        return self._key.publickey().exportKey('PEM')
