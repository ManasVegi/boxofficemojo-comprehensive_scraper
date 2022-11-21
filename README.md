# Box Office Mojo Scraper - Scrapy

## Running The Scraper
1. Add the csv file with all the `titleId`(s) of the movies into the project root.
2. Set that csv file as the argument of df.read_csv(<filename>) in spider.py.
3. If you paused scraping and want to resume, set the total number of rows already scraped in the rowsScraped variable of spider.py.
4. Run with `scrapy crawl mojo -L WARN -o master_dataset.csv` to append the results to an existing csv.
5. Use aggregator.py to join with some other csv file based on the `titleId`.