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
    wordarray = []
    for attr in string.split():
        wordarray.append(attr)
    print(string)

    #print(html)