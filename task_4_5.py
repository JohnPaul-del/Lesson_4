from sys import argv
import requests
import requests.utils as utils
from decimal import Decimal
import datetime


def curr_rate():
    """
    Get currency rate from bank
    :param: name of currency
    :return: currency rate
    """
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    curr = argv
    try:
        buf_index = content.find(str(curr).upper())
        val = content.index('</Value>', buf_index)
        _bufvalue = content[val - 7:val]
        value = Decimal(_bufvalue.replace(',', '.')).quantize(Decimal('0.00'), rounding='ROUND_DOWN')
        _bufdate = content.rfind('Date="')
        _bufdate = content[_bufdate + 6:_bufdate + 16]
        data = datetime.datetime.strptime(_bufdate, "%d.%m.%Y").date()
    except TypeError:
        exit()
    except ValueError:
        print("None")
    print(f'{value},{data}')


if __name__ == "__main__":
    print(curr_rate())
