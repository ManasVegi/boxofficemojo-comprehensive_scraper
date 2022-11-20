import scrapy
import pandas as pd
from ..items import MovieItem
def getUrl(id):
    return f'https://www.boxofficemojo.com/title/{id}/credits/'
class MojoSpider(scrapy.Spider):

    name = "mojo"
    rowsScraped = 0
    df = pd.read_csv('aggregated_data.csv')[rowsScraped:]
    df = df['titleId'].apply(getUrl)

    start_urls = df.tolist()
    print(start_urls)
    
    def parse(self, response):
        item = MovieItem()
        titleId = '-'
        #box office mojo automatically redirects to /title/tt.../credits when there is no box office

        if response.request.url.rsplit('/',4)[-4] == 'title':
            titleId = response.request.url.rsplit('/',4)[-3]
        else:
            return

        directors = '|'.join(response.xpath('//*[@id="principalCrew"]//tr[td[2] = "Director"]/td[1]/a/text()').getall())
        writers = '|'.join(response.xpath('//*[@id="principalCrew"]//tr[td[2] = "Writer"]/td[1]/a/text()').getall())
        producers = '|'.join(response.xpath('//*[@id="principalCrew"]//tr[td[2] = "Producer"]/td[1]/a/text()').getall())
        composers = '|'.join(response.xpath('//*[@id="principalCrew"]//tr[td[2] = "Composer"]/td[1]/a/text()').getall())
        editors = ','.join(response.xpath('//*[@id="principalCrew"]//tr[td[2] = "Editor"]/td[1]/a/text()').getall())
        actor1 = response.xpath('//*[@id="principalCast"]//tr[2]/td[1]//text()').extract()
        actor2 = response.xpath('//*[@id="principalCast"]//tr[3]/td[1]//text()').extract()
        actor3 = response.xpath('//*[@id="principalCast"]//tr[4]/td[1]//text()').extract()
        # domestic_gross = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[1]/div/div[1]/span[2]/span/text()').extract()
        # worldwide_gross = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[1]/div/div[3]/span[2]/span/text()').extract() 
        # distributor = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[contains(span, "Distributor")]/span[2]/text()').extract()

        #COMES IN FORMAT: '/release/rl1482458625/weekend?ref_=bo_tt_gr#table'
        opening_url = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[contains(span, "Opening")]/span[2]/a/@href').extract() #ONLY CRAWL THIS LINK WHEN NON EMPTY LIST

        # running_time = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Running Time"]/span[2]/text()').extract()
        # earliest_release_date = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[contains(span, "Release Date")]/span[2]/text()').extract()
        # genres = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Genres"]/span[2]/text()').extract()
        # mpaa = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "MPAA"]/span[2]/text()').extract()

        # budget = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span[1] = "Budget"]//span[@class="money"]/text()').extract()
        #distributor = data.xpath('[span[1]="Distributor"]/span[2].text()').extract()
        # movie_title = response.xpath('//*[@id="a-page"]/main/div/div[1]/div[1]/div/div/div[2]/h1/text()')[0].extract()
        #print(movie_title)

        #title and field name must match
        item['titleId'] = titleId
        item['directors'] = "-" if len(directors) == 0 else directors
        item['writers'] = "-" if len(writers) == 0 else writers
        item['producers'] = "-" if len(producers) == 0 else producers
        item['composers'] = "-" if len(composers) == 0 else composers
        item['editors'] = "-" if len(editors) == 0 else editors
        item['actor1'] = "-" if len(actor1) == 0 else actor1[0]
        item['actor2'] = "-" if len(actor2) == 0 else actor2[0]
        item['actor3'] = "-" if len(actor3) == 0 else actor3[0]
        if len(opening_url) > 0 and len(opening_url[0]) > 0:
            yield scrapy.Request(f'https://www.boxofficemojo.com{opening_url[0].split("?")[0] + "/"}', self.parse_link, meta={'item': item}) 
        else:
            print(item)
            yield item
        

    def parse_link(self, response):

        item = response.meta.get('item') #since there are no return values this is how to return item
        opening_theatres = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[contains(span, "Opening")]/span[2]/text()').extract() 
        in_release = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "In Release"]/span[2]/text()').extract()
        widest_release = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Widest Release"]/span[2]/text()').extract()

        #title and field name must match
        item['opening_theatres'] = "-" if len(opening_theatres) == 0 else opening_theatres[0].split('\n')[0]
        item['in_release'] = "-" if len(in_release) == 0 else in_release[0]
        item['widest_release'] = "-" if len(widest_release) == 0 else widest_release[0]
        print(item)
        yield item