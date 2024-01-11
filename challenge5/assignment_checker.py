import requests
from bs4 import BeautifulSoup

login_url = 'https://lms.iitmandi.ac.in/login/index.php'
course_url = 'https://lms.iitmandi.ac.in/course/view.php?id=3562'  # Example course URL

payload = {
    'username': 'b23354',
    'password': 'bhrle'
}

with requests.Session() as s:
    p = s.post(login_url, data=payload)
    r = s.get(course_url)
    print(r).
    # soup = BeautifulSoup(r.content, 'lxml')
    # print(soup.prettify())

    # # Find all links within the course page
    # all_links = soup.find_all('a', href=True)
    # print(f"Found {len(all_links)} links in the course page.")

    # for link in all_links:
    #     print(link['href'])
