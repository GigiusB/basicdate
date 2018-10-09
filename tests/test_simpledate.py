import datetime
import json

from basicdate import BasicDate, BasicDateEncoder, BasicDateDecoder

class TestBasicDate:
    def test_json(self):
        d = '{"_type": "BasicDate", "value": "20180117"}'
        assert json.loads(d, cls=BasicDateDecoder) == BasicDate('17/01/2018')
        assert json.dumps(BasicDate('17/01/2018'), cls=BasicDateEncoder) == d

    def test_identity(self):
        a, b, c = BasicDate('17/01/2018'), BasicDate(datetime.datetime(2018, 1, 17, 14, 11)), BasicDate('18/01/2018')
        assert a == b
        assert a != c
        assert type(a) == type(b) == type(c)
        assert a is b
        assert a is not c
        assert a == c - 1
        assert BasicDate(a) is a
        assert BasicDate(a) is b
        assert BasicDate(a) == a
        assert BasicDate(a) == b


    def test_as_key(self):
        a, b, c = BasicDate('17/01/2018'), BasicDate('17/01/2018'), BasicDate('11/01/2018')
        assert a is b
        assert a is not c
        d = {}
        a = d.setdefault(a, {'one': 1})
        b = d.setdefault(b, {'two': 2})
        c = d.setdefault(c, {'three': 3})
        assert len(d) == 2
        assert BasicDate('17/01/2018') in d
        assert BasicDate('18/01/2018') not in d
        assert a == b == {'one': 1}
        assert a != c


