# Nana

The Roku Channel API wrapper.

Every endpoint is an attribute on the client. Calling it downloads and reads in
one go, and `download` and `load` are the two halves of that.

```python
from nana import Nana
from nana.menu import Menu
from nana.page import Page
from nana.search import Search

client = Nana()

# The menu is the only place the browse page ids are published.
menu = client.menu()
page_id = Menu.extract_pages(menu)[0].meta.id

# A browse page is the rows of titles the screen is built out of.
page = client.page(page_id)
print(page.title, len(Page.extract_content(page)))

# Search answers with whatever it matched, titles and collections alike.
for match in Search.extract_content(client.search("die hart")):
    print(match.type, match.meta.id, match.title)

# One endpoint covers movies, series, seasons and episodes.
series = client.content("14de3bf28d7153ff8d938f554b76dcf5")
for season in series.seasons or []:
    for episode in season.episodes or []:
        print(season.season_number, episode.episode_number, episode.title)

# The file can be downloaded and read separately.
downloaded = client.content.download("14de3bf28d7153ff8d938f554b76dcf5")
series = client.content.load(downloaded)
```
