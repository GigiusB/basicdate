import json

from basicdate import BasicDate, BasicDateEncoder, BasicDateDecoder

class TestBasicDate:
    def test_json(self):
        d = '{"_type": "BasicDate", "value": "20180117"}'
        assert json.loads(d, cls=BasicDateDecoder) == BasicDate('17/01/2018')
        assert json.dumps(BasicDate('17/01/2018'), cls=BasicDateEncoder) == d

    def test_as_key(self):
        a, b, c = BasicDate('17/01/2018'), BasicDate('17/01/2018'), BasicDate('18/01/2018')
        assert a == b
        assert a != c
        assert type(a) == type(b) == type(c)
        assert a is b
        assert a is not c
        assert a == c - 1

