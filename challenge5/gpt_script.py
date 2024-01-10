import requests
from bs4 import BeautifulSoup

login_url = 'https://lms.iitmandi.ac.in/login/index.php'
homepage_url = 'https://lms.iitmandi.ac.in/'
course_url = 'https://lms.iitmandi.ac.in/course/view.php?id=3562'  # Example course URL

payload = {
    'username': 'b23354',
    'password': 'Piyush@2904'
}

with requests.Session() as s:
    p = s.post(login_url, data=payload)
    r = s.get(course_url)
    soup = BeautifulSoup(r.content, 'html.parser')

    assignment_links = []

    # Find all links within the course page
    all_links = soup.find_all('a', href=True)
    print(f"Found {len(all_links)} links in the course page.")

    for link in all_links:
        if 'mod/assign/view.php' in link['href']:
            assignment_url = link['href']
            print(f"Assignment URL: {assignment_url}")
            assignment_links.append(assignment_url)

    if not assignment_links:
        print("No assignment links found.")
    else:
        print("Assignment Links:")
        for link in assignment_links:
            print(link)

