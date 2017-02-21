import unittest
from supertest import TestCase
from supertest import R
from google.appengine.ext import ndb
from certz.api.ent import Domain

class DomainTestCase(TestCase):

    def test_save(self):
        domain = Domain(
            id = 'test.domain'
        )

if __name__ == '__main__':
        unittest.main()
