


class Domain(ndb.Model):
    privateKey = ndb.StringProperty(indexed = False)
    chain = ndb.StringProperty(indexed = False)
    cert = ndb.StringProperty(indexed = False)
