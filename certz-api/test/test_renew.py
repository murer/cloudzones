import unittest
from supertest import TestCase
from supertest import R
from google.appengine.ext import ndb
from certz.api.ent import Domain

class DomainTestCase(TestCase):

    def test_save(self):
        Domain(id='test.domain').put()
        domain = Domain.find_by_domain('test.domain')
        self.assertEqual('test.domain', domain.key.id())

if __name__ == '__main__':
        unittest.main()
