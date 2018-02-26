import datetime
import re
from collections import namedtuple

class Entry(object):

    def __init__(self, content, date_req):
        self.req_conntent = content
        self.entry_date = date_req

    def __str__(self):

        return "Content: {} and has {} bytes".format(self.entry_date,
        len(self.req_conntent))

class CacheObject(object):

    def __init__(self, capacity=10):

        self.cache_entries = {}
        self.capacity = capacity

    def __contains__(self, key):
        return key in self.cache_entries

    def __iter__(self):
        self.current_entry = -1
        return self

    def __next__(self):

        if self.current_entry >= self.size() - 1:
            raise StopIteration()
        self.current_entry+=1
        return list(self.cache_entries.values())[self.current_entry]

    def __getitem__(self, key):
        http_pattern = re.compile("htt[ps]://[a-zA-Z0-9].[a-z]{3}+")
        if key not in self.cache_entries or http_pattern.search(key) is None:
                raise KeyError("Request not in cache or dosen't match the pattern")
        return self.cache_entries[key]

    def add_entry_field(self, key, value):

        if key not in self.cache_entries and \
                len(self.cache_entries) == self.capacity:
                self.delete_entry_field()
        self.cache_entries[key] = value


    def delete_entry_field(self, key):

        oldest_entry_key = None

        for e_key, e_value in self.cache_entries.iteritems():
            if oldest_entry_key is None:
                oldest_entry_key = e_key
            elif e_value.entry_date > self.cache_entries[oldest_entry_key]:
                oldest_entry_key = e_key
        del self.cache_entries[oldest_entry_key]

    def size(self):

        return len(self.cache_entries)


e = Entry("http://pula.html", datetime.datetime.now())
c = CacheObject()
c.add_entry_field("http://pula.html", e)
c.add_entry_field("http://www.facebook.com", e)
c.add_entry_field("http://www.google.com", e)

for e in c:
    print(e)
