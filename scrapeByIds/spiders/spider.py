import scrapy
from scrapy import signals
import pandas as pd
import time
from ..items import MovieItem
def getUrl(id):
    return f'https://www.boxofficemojo.com/title/{id}/'
class MojoSpider(scrapy.Spider):

    name = "mojo"
    rowsScraped = 0
    df = pd.read_csv('imdbIdsFiltered.csv')[rowsScraped:]
    df['titleId'] = df['titleId'].apply(getUrl)

    start_urls = df.stack().tolist()
    
    def parse(self, response):
        item = MovieItem()
        #box office mojo automatically redirects to /title/tt.../credits when there is no box office
        if response.request.url.rsplit('/',3)[-3] == 'title':
            titleId = response.request.url.rsplit('/',3)[-2]
        else:
            return
        domestic_gross = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[1]/div/div[1]/span[2]/span/text()').extract()
        worldwide_gross = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[1]/div/div[3]/span[2]/span/text()').extract() 
        distributor = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[contains(span, "Distributor")]/span[2]/text()').extract()
        domestic_opening = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[contains(span, "Opening")]/span[2]//span[@class="money"]/text()').extract()
        running_time = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Running Time"]/span[2]/text()').extract()
        earliest_release_date = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[contains(span, "Release Date")]/span[2]/text()').extract()
        genres = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Genres"]/span[2]/text()').extract()
        mpaa = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "MPAA"]/span[2]/text()').extract()

        budget = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span[1] = "Budget"]//span[@class="money"]/text()').extract()
        #distributor = data.xpath('[span[1]="Distributor"]/span[2].text()').extract()
        # movie_title = response.xpath('//*[@id="a-page"]/main/div/div[1]/div[1]/div/div/div[2]/h1/text()')[0].extract()
        #print(movie_title)

        #title and field name must match
        item['titleId'] = titleId
        item['domestic_opening'] = "-" if len(domestic_opening) == 0 else domestic_opening[0]
        item['domestic_gross'] = "-" if len(domestic_gross) == 0 else domestic_gross[0]
        item['worldwide_gross'] = "-" if len(worldwide_gross) == 0 else worldwide_gross[0]
        item['earliest_release_date'] = "-" if len(earliest_release_date) == 0 else earliest_release_date[0]
        item['distributor'] = "-" if len(distributor) == 0 else distributor[0]
        item['running_time'] = "-" if len(running_time) == 0 else running_time[0]
        item['genres'] = "-" if len(genres) == 0 else genres[0]
        item['mpaa'] = "-" if len(mpaa) == 0 else mpaa[0]
        item['budget'] = "-" if len(budget) == 0 else budget[0]
        print(item)
        yield item
        

    # def parse_link(self, response):

    #     item = response.meta.get('item') #since there are no return values this is how to return item
    #     distributor = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Distributor"]/span[2]/text()').extract() 
    #     running_time = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Running Time"]/span[2]/text()').extract()
    #     genres = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Genres"]/span[2]/text()').extract()
    #     mpaa = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "MPAA"]/span[2]/text()').extract()

    #     budget = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span[1] = "Budget"]//span[@class="money"]/text()').extract()
    #     #distributor = data.xpath('[span[1]="Distributor"]/span[2].text()').extract()
    #     # movie_title = response.xpath('//*[@id="a-page"]/main/div/div[1]/div[1]/div/div/div[2]/h1/text()')[0].extract()
    #     #print(movie_title)

    #     #title and field name must match
    #     item['distributor'] = "-" if len(distributor) == 0 else distributor[0]
    #     item['running_time'] = "-" if len(running_time) == 0 else running_time[0]
    #     item['genres'] = "-" if len(genres) == 0 else genres[0]
    #     item['mpaa'] = "-" if len(mpaa) == 0 else mpaa[0]
    #     item['budget'] = "-" if len(budget) == 0 else budget[0]
    #     print(item)
    #     yield item