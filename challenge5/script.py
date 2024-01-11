import requests
from bs4 import BeautifulSoup

login_url = 'https://lms.iitmandi.ac.in/login/index.php'
homepage_url = 'https://lms.iitmandi.ac.in/'

payload={
    'username': 'b23354',
    'password': 'Piyush@2904'
}

with requests.Session() as s:
    p = s.get(login_url)
    soup = BeautifulSoup(p.content, 'lxml')
    payload['logintoken'] = soup.find('input', attrs={'name': 'logintoken'})['value']
    r = s.post(login_url, data=payload)
    soup = BeautifulSoup(r.content, 'lxml')
    print(soup.prettify())
    course_links = soup.find_all('a', hre)
    # print(course_links)
