from bs4 import BeautifulSoup

def extract_classes(html):
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all('li', class_='f-menu-submenu-item')
    classes = {}
    
    for li in results:
        link = li.find('a', href=True)
        if link and '/student/classes/' in link['href']:
            class_id = link['href'].split('/')[-1]
            class_name = link.find('span', class_='f-menu-submenu-link-title').text.strip()
            if class_id.isdigit():
                classes[class_id] = class_name
                
    return classes
                
if __name__ == "__main__":
    with open("export.html", "r") as f:
        html_snippet = f.read()
    print(extract_classes(html_snippet))