import requests
import bs4


books_url = "http://books.toscrape.com/catalogue/page-{}.html"
quotes_url = "http://quotes.toscrape.com/page/"

# Get books title
two_star_titles = []

for n in range(1, 51):
    scrape_url = books_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)


# Get quotes author
page_still_valid = True
authors = set()
page = 1

while page_still_valid:
    page_url = quotes_url + str(page)
    res = requests.get(page_url)

    if 'No quotes found!' in res.text:
        break

    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    for name in soup.select('.author'):
        authors.add(name.text)

    page += 1


# Get quotes
quotes = []

for quote in soup.select('.quote'):
    quotes.append(quote.text)
