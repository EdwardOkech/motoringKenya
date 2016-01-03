MotoringKe is a web spider that crawls the web for usefull information on Kenyan websites selling cars, reviewing cars
on various metrics

to use cd into directory
run $ scrapy  scrapy crawl checki  # thats if you want to crawl cheki website
run $ scrapy  scrapy crawl star  # thats if you want to crawl star website
run $ scrapy  scrapy crawl olx  # thats if you want to crawl olx website

to store the crawled data
run $ scrapy crawl cheki -o items.json  #store data from checki as json file
run $ scrapy crawl cheki -o items.csv  #store data from checki as csv file



