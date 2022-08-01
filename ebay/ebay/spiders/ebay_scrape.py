import scrapy

class EbayWebSpider(scrapy.Spider):
    name = "ebay"
    domain = ["ebay.com"]
    start_urls = [
        "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l2632&_nkw=star+wars+vintage&_sacat=246&LH_TitleDesc=0&_odkw=star+wars+action+figures&_osacat=0"
    ]

    def parse(self, response):
        products = response.xpath('//div/div/ul/li[contains(@class, "s-item" )]')
        for product in products:
            name = product.xpath('.//*[@class="s-item__title"]//text()').get()
            # treat new listing to avoid errors
            if name == 'New Listing':
                name = product.xpath('.//*[@class="s-item__title"]//text()').extract()[1]
            price = product.xpath('.//*[@class="s-item__price"]//text()').get().replace('$','')
            geo = product.xpath('.//*[@class="s-item__location s-item__itemLocation"]//text()').get().replace('from ','')
            condition_items = product.xpath('.//*[@class="s-item__subtitle"]//text()').get()
            product_url = product.xpath('.//a[@class="s-item__link"]/@href').get()
            # treating conditions for when > 1
            try:
                if len(condition_items) == 1:
                    condition = product.xpath('.//*[@class="s-item__subtitle"]//text()').get()
                elif len(condition_items) > 1:
                    condition = product.xpath('.//*[@class="SECONDARY_INFO"]//text()').get()
            except Exception as e:
                print(f"product condition not found - due to {e}")
                condition = 'not found'
            # return all collected html data
            yield {
                'product_name': name,
                'price': price,
                'country': geo,
                'condition': condition,
                'url': product_url
            }
        # get button for url next page
        next_page = response.css('a.pagination__next.icon-link').attrib['href']
        print(f'this is the next page: {next_page}')
        # continue loop while url appears
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)