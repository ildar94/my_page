class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value


class My_converter:
    regex = '[+-]?(\d*\.)?\d+'


    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return '%04d' % value
