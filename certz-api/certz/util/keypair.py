from Crypto.PublicKey import RSA

class KeyPair(object):

    @classmethod
    def create(cls):
        ret = cls()
        ret.key = RSA.generate(4096)
        return ret

    @classmethod
    def parse(cls, private_key):
        ret = cls()
        ret.key = RSA.importKey(private_key)
        return ret

    def export_private_key(self):
        return self.key.exportKey('PEM')

    def export_public_key(self):
        return self.key.publickey().exportKey('PEM')
