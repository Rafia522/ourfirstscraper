import scrapy
import pandas as pd
import psycopg2


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ["https://www.reddit.com/r/gameofthrones/"]

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.xpath('//a/div/h3//text()').extract()
        votes = response.xpath('//div[contains(@data-test-id, post-container)][1]/div/div/button[contains(@aria-label, \'upvote\')][1]/following-sibling::div//text()').extract()

       
        #Give the extracted content row wise
        for item in zip(titles, votes):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info

        
        