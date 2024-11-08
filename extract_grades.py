from bs4 import BeautifulSoup
import re

def extract_grades(html):
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find('div', class_='sidebar-items-list')
    grades = results.find_all("div", class_="cell")
    overall_grade = grades[3].text.strip("\n").replace(" ", "").split("\n")
    del overall_grade[-1]
    overall_grade[1] = overall_grade[1].replace("(", "").replace(")", "")
    
    return overall_grade
                
if __name__ == "__main__":
    with open("export-grades.html", "r") as f:
        html_snippet = f.read()
    print(extract_grades(html_snippet))