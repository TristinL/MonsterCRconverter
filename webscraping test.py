from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://www.aidedd.org/dnd/monstres.php?vo=aarakocra"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    title_index = html.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]

    match_results = re.search("<.*>", html, re.IGNORECASE)
    print(match_results.group())
    string = re.sub("<.*?>", "", html)
    string = re.sub("&raquo", "", string)
    string = re.sub("&amp", "", string)
    string = re.sub("@media.*}", "", string)
    pattern = "<title.*?>.*-->"
    match_results2=re.search(pattern, html, re.IGNORECASE)
    monster=match_results2.group()
    print(monster)
    wordarray = []
    for attr in string.split():
        wordarray.append(attr)

    soup = BeautifulSoup(monster, "html.parser")
    better_soup = soup.get_text()
    print(better_soup)
    better_soup = re.sub("\\)*?", ") ", better_soup)

    print(better_soup)

    #print(html)