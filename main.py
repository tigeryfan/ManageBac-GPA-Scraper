import toml
import requests
import extract_classes
import extract_grades
import excel_wrapper

config = toml.load("config.toml")
mb_cookie = config["secrets"]["mb_cookie"]
mb_url = config["mb"]["mb_url"]
excel_file = config["excel"]["file_name"]

# Set User Agent here. Keep in mind that ManageBac may block some UAs due to scripting abuse
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0"

# Cookies
cookies = {
    "_managebac_session": mb_cookie
}

# Headers
headers = {
    "User-Agent": ua,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Priority": "u=0, i",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}

classes_html = requests.get("https://" + mb_url + "/student/classes/my", cookies=cookies, headers=headers)
classes = extract_classes.extract_classes(classes_html.text)

total_grades = {}
for class_id, class_name in classes.items():
    class_html = requests.get("https://" + mb_url+ "/student/classes/" + class_id + "/units", cookies=cookies, headers=headers)
    grades = extract_grades.extract_grades(class_html.content)
    print(class_name, ": ", grades, sep="")
    total_grades[class_id] = grades

print(total_grades)