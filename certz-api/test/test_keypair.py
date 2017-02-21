import unittest
from unittest import TestCase
from certz.util.keypair import KeyPair

class KeyPairTestCase(TestCase):

    def test_keypair(self):
        kp = KeyPair.create()
        other = KeyPair.parse(kp.export_private_key())
        self.assertEqual(kp.export_private_key(), other.export_private_key())
        self.assertEqual(kp.export_public_key(), other.export_public_key())

if __name__ == '__main__':
        unittest.main()
