from certz.util.keypair import KeyPair
from certz.util import codecutil as codec
import json
import binascii
import hashlib

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

    def _get_public_key(self):
        exp = self._key.key.e
        n = self._key.key.n
        exp = hex(exp)[2:].rstrip('L')
        n = hex(n)[2:].rstrip('L')
        exp = '0%s' % (exp) if len(exp) % 2 else exp
        n = '0%s' % (n) if len(n) % 2 else n
        exp = binascii.unhexlify(exp)
        n = binascii.unhexlify(n)
        exp = codec.ub64enc(exp)
        n = codec.ub64enc(n)
        return exp, n

    def renew(self):
        exp, n = self._get_public_key()
        header = { "alg": "RS256", "jwk": { "e": exp, "kty": "RSA", "n": n } }
        accountkey_json = json.dumps(header['jwk'], sort_keys=True, separators=(',', ':'))
        thumbprint = codec.ub64enc(hashlib.sha256(accountkey_json.encode('utf8')).digest())
        print accountkey_json, thumbprint
