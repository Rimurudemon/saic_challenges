import requests
from bs4 import BeautifulSoup

login_url = 'https://lms.iitmandi.ac.in/login/index.php'
course_url = 'https://lms.iitmandi.ac.in/course/view.php?id=3562'  # Example course URL

payload = {
    'username': 'b23354',
    'password': 'bhrle'
}

with requests.Session() as s:
    r= s.get(login_url)
    doc= r.text
    print(doc)
 