'''3
Viết script lấy top **N** câu hỏi được vote cao nhất của tag **LABEL** trên stackoverflow.com.
In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất

Link API: https://api.stackexchange.com/docs

Dạng của câu lệnh:

  python3 so.py N LABEL'''


import requests
import sys

url_api_stack = 'https://api.stackexchange.com/2.2/questions'


def get_link_api (n, label):
    result = {}
    params = {
        'pagesize': n,
        'order': 'desc',
        'sort': 'votes',
        'tagged': label,
        'site': 'stackoverflow'
    }
    ses = requests.Session()
    resp  = ses.get(url_api_stack,params=params)
    if resp.status_code == 200:
        items = resp.json().get('items')
        for item in items:
            print('Title : ',item['title'])
            id = item['accepted_answer_id']
            print('Link top Answer : {}/{}#{}'.format(item['link'],id,id))
            print('----------------------------------------\n')
    else: 
        print


def solve():
    if len(sys.argv) == 1 or len(sys.argv) == 2 :
        print('Vui Lòng Nhập Đúng Cú Pháp')
        n =  input ('số lượng command: ')
        tag = input('Tags cần tìm kiếm: ')
        get_link_api(n,tag)
    elif len(sys.argv) == 3:
        n = sys.argv[1]
        tag = sys.argv[2]
        get_link_api(n,tag)
    else:
        print('Vui Lòng Nhập Đúng Cú Pháp')
        n =  input ('số lượng command: ')
        tag = input('Tags cần tìm kiếm: ')
        get_link_api(n,tag)

def main():
    solve()

if __name__ == "__main__":
    main()