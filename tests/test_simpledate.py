import json

from basicdate import BasicDate, BasicDateEncoder, BasicDateDecoder

class TestBasicDate:
    def test_json(self):
        d = '{"_type": "BasicDate", "value": "20180117"}'
        assert json.loads(d, cls=BasicDateDecoder) == BasicDate('17/01/2018')
        assert json.dumps(BasicDate('17/01/2018'), cls=BasicDateEncoder) == d
