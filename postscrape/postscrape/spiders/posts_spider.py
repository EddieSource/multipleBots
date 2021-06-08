import scrapy
import csv


websites = []
with open('company_url.csv', newline='') as f:
    reader = csv.reader(f)  # put in all the company websites
    headings = next(reader)  # remove the header
    for row in reader:
        websites.append(row[1])


class PostsSpider(scrapy.Spider):
    name = "posts"
    # start_urls = ['https://www.rendelmanlaw.com/', 'https://www.normapotroslawfirm.com/','https://grant.legal/'] # enter ur email addresses
    start_urls = websites
    emails = []

    def parse(self, response):
        curs = response.xpath('//body//text()').re(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}')
        curs = [[cur] for cur in list(dict.fromkeys(curs))]
        self.emails.extend(curs)
        # write your sample csv file

        with open('emails.csv', 'w') as f:
            write = csv.writer(f)
            write.writerows(self.emails)



# response.xpath('//*[contains(text(), "212")]').get()
#  response.xpath('//*/text()').re(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}')

