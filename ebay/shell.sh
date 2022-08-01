# go to directory
cd .path/star_wars_ebay_scrapy_and_eda

# create virtual env py
python3 -m venv env
source env/bin/activate

# install scrapy framework
pip install scrapy

# create project in scrapy
scrapy startproject STARWARS_EBAY

# go to project
cd STARWARS_EBAY

# view composition
tree

# scrapy shell
scrapy shell

# fetch url to scrape (expected 200 resp)
fetch("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l2632&_nkw=star+wars+vintage&_sacat=246&LH_TitleDesc=0&_odkw=star+wars+action+figures&_osacat=0")

# full container
response.xpath('//*[@id="srp-river-results"]').get()

# first product in search
response.xpath('//div/div/ul/li[contains(@class, "s-item" )]').get()

# save variable to all items
products = response.xpath('//div/div/ul/li[contains(@class, "s-item" )]')

# get 1st name
products.xpath('.//*[@class="s-item__title"]//text()').get()

# get price
products.xpath('.//*[@class="s-item__price"]//text()').get()

# run spyder & save to .json or .csv
scrapy crawl STARWARS_EBAY -O STARWARS_EBAY.csv