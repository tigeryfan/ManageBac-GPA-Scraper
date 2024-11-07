from bs4 import BeautifulSoup

def extract_ids(html):
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all('li', class_='f-menu-submenu-item')
    class_ids = []
    for li in results:
        link = li.find('a', href=True)
        if link and '/student/classes/' in link['href']:
            class_id = link['href'].split('/')[-1]
            if class_id.isdigit():
                class_ids.append(class_id)
    return class_ids
                
if __name__ == "__main__":
    with open("export.html", "r") as f:
        html_snippet = f.read()
    print(extract_ids(html_snippet))