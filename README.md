# scrapers


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
What things you need to install the software and how to install them

```bash
pip install -r requirements.txt
```

### Running a Spider


To run a spider, use the following command:
```bash
cd hackernews_scraper
```

Without outputting to a file. 
```bash
scrapy crawl hackernews
```

With output to a file.
```bash
scrapy crawl hackernews -o results.json
```

Using the Scrapy shell
```bash
scrapy shell 'https://news.ycombinator.com/'
```

```python
print(response.css('td.title a::text').get())
print(response.css('td.title a::attr(href)').get())
```

