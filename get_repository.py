''' 
1
-
Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:

Ví dụ với user ``pymivn``, sử dụng dữ liệu ở JSON format tại
https://api.github.com/users/pymivn/repos

Câu lệnh của chương trình có dạng::

  python3 githubrepos.py username

Gợi ý:

Sử dụng các thư viện:

- requests
- sys or argparse
'''


import requests
import json
import sys
user = ''
def get_data(user):
    list_name_repo = []
    url = 'https://api.github.com/users/{}/repos'.format(user)
    ses = requests.Session()
    data = ses.get(url)
    data_json = data.json()
    for i in data_json:
        list_name_repo.append(i['name'])
        print(i['name'])
    if list_name_repo == []:
        print('user ban nhap khong ton tai or chua co repo')
    return list_name_repo



def solve():
    if len(sys.argv) == 1:
        user = input('nhap user can lay du lieu : ')
    else:
        user = sys.argv[1]
    return get_data(user)


def main():
    solve()
if __name__ == "__main__":
    main()
