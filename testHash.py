import scrapy


name = 'blogspider'
start_urls = ['https://blog.scrapinghub.com']

def parse(self, response):
    for title in response.css('.post-header>h2'):
        print(title)
        return {'title': title.css('a ::text').get()}

    for next_page in response.css('a.next-posts-link'):
        print(next_page)
        return response.follow(next_page, self.parse)

