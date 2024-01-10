import requests
from bs4 import BeautifulSoup

login_url = 'https://lms.iitmandi.ac.in/login/index.php'
example_assignment_link = 'https://lms.iitmandi.ac.in/mod/assign/view.php?id=50348'

payload = {
    'username': 'b23354',
    'password': 'Piyush@2904'
}

with requests.Session() as s:
    p = s.post(login_url, data=payload)
    r = s.get(example_assignment_link)
    soup = BeautifulSoup(r.content, 'html.parser')

    activity_dates = soup.find('div', class_='activity-dates')
    if activity_dates:
        opened_date = activity_dates.find('strong', text='Opened:')
        due_date = activity_dates.find('strong', text='Due:')

        opened_date_text = opened_date.next_sibling.strip() if opened_date else "Opened date not found"
        due_date_text = due_date.next_sibling.strip() if due_date else "Due date not found"

        print(f"Opened Date: {opened_date_text}")
        print(f"Due Date: {due_date_text}")
    else:
        print("No activity dates found.")