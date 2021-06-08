import scrapy
import csv
import pandas as pd


class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = ['','',''] # enter ur email addresses
    def parse(self, response):
        emails = []
        curs = response.xpath('//body//text()').re(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}')
        curs = [[cur] for cur in list(dict.fromkeys(curs))]
        emails.extend(curs)
        print(emails)
        # write your sample csv file

        with open('emails.csv', 'w') as f:
            write = csv.writer(f)

            write.writerows(emails)




# response.xpath('//*[contains(text(), "212")]').get()
#  response.xpath('//*/text()').re(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}')

