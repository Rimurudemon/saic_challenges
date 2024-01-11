import requests
from bs4 import BeautifulSoup

login_url = 'https://lms.iitmandi.ac.in/login/index.php'
homepage_url = 'https://lms.iitmandi.ac.in/'

payload={
    'username': 'b23354',
    'password': 'Piyush@2904'
}

with requests.Session() as s:
    p = s.post(login_url, data=payload)
    r = s.get(homepage_url)
    soup = BeautifulSoup(r.content, 'lxml')
    course_links = soup.find_all('a', class_="pointer-hover")
    print(course_links)
