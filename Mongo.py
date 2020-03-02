from datetime import datetime


class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        """returns True if s is a valid MongoID; otherwise False"""
        if s and isinstance(s, str) and len(s) == 24:
            for c in s:
                if c.isupper():
                    return False
            try:
                int(s, 16)
                return True
            except ValueError:
                return False
        return False

    @classmethod
    def get_timestamp(cls, s):
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""
        if Mongo.is_valid(s):
            return datetime.fromtimestamp(int(s[:8], 16))
        return False


Mongo.is_valid('507f1f77bcf86cd799439011')  # True
Mongo.get_timestamp('507f1f77bcf86cd799439011')  # Wed Oct 17 2012 21:13:27 GMT-0700 (Pacific Daylight Time)


x = '507f1f77bcf86cd799439011'[:8]
y = int(x, 16)
print(datetime.utcfromtimestamp(y))

