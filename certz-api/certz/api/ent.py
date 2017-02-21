from google.appengine.ext import ndb


class Domain(ndb.Model):
    privateKey = ndb.StringProperty(indexed = False)
    chain = ndb.StringProperty(indexed = False)
    cert = ndb.StringProperty(indexed = False)

    @classmethod
    def find_by_domain(cls, domain):
        return cls.get_by_id(domain)
