import unittest
from supertest import TestCase
from supertest import R
from google.appengine.ext import ndb
from certz.api.ent import Domain
from certz.api.renew import Renew

class DomainTestCase(TestCase):

    def test_save(self):
        Domain(id='test.domain').put()
        domain = Domain.find_by_domain('test.domain')
        renew = Renew(domain).compute_key()
        self.assertEqual(renew._domain.privateKey, renew._key.export_private_key())
        domain.put()
        domain = Domain.find_by_domain('test.domain')
        renew = Renew(domain).compute_key()
        self.assertEqual(renew._domain.privateKey, renew._key.export_private_key())
        renew.renew()




if __name__ == '__main__':
        unittest.main()
