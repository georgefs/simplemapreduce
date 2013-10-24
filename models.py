# -*- coding: utf-8 -*-
from google.appengine.ext import ndb

class ProductItem(ndb.Model):
    product_key = ndb.StringProperty()
    commerce_id = ndb.StringProperty()
    image_url = ndb.StringProperty(indexed=False)
    link = ndb.StringProperty()
    title = ndb.StringProperty()
    price = ndb.StringProperty()
    store_price = ndb.StringProperty()
    keywords = ndb.StringProperty()
    description = ndb.StringProperty()
    live = ndb.BooleanProperty()
    category_path = ndb.StringProperty(indexed=False)

    created_time = ndb.DateTimeProperty(auto_now_add=True)    
    updated_time = ndb.DateTimeProperty(auto_now=True)
    next_updated = ndb.DateTimeProperty()
