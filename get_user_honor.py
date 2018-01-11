from urllib.request import urlopen
import bs4


def get_honor(username):
    if not username or type(username) != str:
        raise AttributeError("Only valid strings acceptable")
    url_path = "https://www.codewars_solutions.com/users/leaderboard"
    url = urlopen(url_path)
    html = url.read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    leaders = soup.find("table")
    for leader in leaders:
        columns = leader.findAll('td')  # Bring all the columns
        if len(columns) > 0:
            honor = int(columns[3].get_text())
            return honor


def get_honor_select(username):
    if not username or type(username) != str:
        raise AttributeError("Only valid strings acceptable")
    url_path = "https://www.codewars_solutions.com/users/leaderboard"
    url = urlopen(url_path)
    html = url.read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    table = soup.select("div.row > div.panel.is-darkened > div > table > tr")
    for line in table:
        if line.has_attr("data-username") and line.attrs["data-username"] == username:
            honor = line.contents[3].get_text()
            return int(honor)


print(get_honor('g964'))