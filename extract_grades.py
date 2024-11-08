from bs4 import BeautifulSoup

def extract_grades(html):
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find("div", class_="sidebar-items-list")
    grades = results.find_all("div", class_="cell")
    grades = grades[3].text.split("\n")
    del grades[0]
    del grades[-1]
    try:
        grades[1] = grades[1].replace("(", "").replace(")", "")
    except IndexError:
        # gracefully handle classes with no grades
        return None
    
    return grades
                
if __name__ == "__main__":
    with open("export-grades.html", "r") as f:
        html_snippet = f.read()
    print(extract_grades(html_snippet))