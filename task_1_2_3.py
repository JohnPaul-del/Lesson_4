import requests
import requests.utils as utils
from decimal import Decimal
import datetime


def curr_rate(curr):
    """
    Get currency rate from bank
    :param curr: name of currency
    :return: currency rate
    """
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    _bufdate = content.rfind('Date="')
    _bufdate = content[_bufdate + 6:_bufdate + 16]
    data = datetime.datetime.strptime(_bufdate, "%d.%m.%Y").date()
    try:
        buf_index = content.find(curr)
        val = content.index('</Value>', buf_index)
        _bufvalue = content[val - 7:val]
        value = Decimal(_bufvalue.replace(',', '.')).quantize(Decimal('0.00'), rounding='ROUND_DOWN')
        return value, data
    except ValueError:
        print("None")


cur = input("Enter currency: ").upper()
try:
    bufcur, bufdate = curr_rate(cur)
    print(bufcur, bufdate)
except UnboundLocalError:
    exit()
