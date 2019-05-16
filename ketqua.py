'''Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Dạng của câu lệnh::

    ketqua.py [NUMBER1] [NUMBER2] [...]

Các thư viện:

- requests
- requests_html hay beautifulsoup4 [tuỳ chọn]
- argparse hay sys.argv

Gợi ý:

- ``nargs`` https://docs.python.org/2/library/argparse.html
'''

import requests
import sys
from bs4 import BeautifulSoup as beau
ses = requests.Session()
resp = ses.get('https://ketqua.net')
data = resp.text
data_format = beau(data, 'html.parser')
list_bingo = []
index_special = data[23047:23049]
# print(data_format.prettify())
def get_list_bingo():
    for i in data_format.find_all('td', class_='chu17 need_blank'):
        if i.text.isdigit():
            list_bingo.append(i.text)
            # print(i.text)
    # print(list_bingo)
get_list_bingo()
def solve():
    if len(sys.argv) == 1:
        print('bạn chưa nhập lô muốn kiểm tra')
    else:
        for i in range(len(sys.argv) -1):
            # print(sys.argv[i+1])
            if str(sys.argv[i+1]) == index_special:
                print('BẠN ĐÃ TRÚNG LÔ ĐẶC BIẾT : ',sys.argv[i+1])
            elif sys.argv[i+1] in list_bingo:
                # print(list_bingo)
                print('bạn đã trúng lô : ',sys.argv[i+1] )
            else:
                print('với lô {} chúc bạn may mắn lần sau'.format(sys.argv[i + 1]))

def main():
    solve()

if __name__ == "__main__":
    main()