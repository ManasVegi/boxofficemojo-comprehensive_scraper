# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import csv
class MoviePipeline():    
    def __init__(self):
        field_names = ['titleId', 'directors','writers','producers','composers','editors','actor1','actor2','actor3']
        self.csvwriter = csv.DictWriter(open("hellothere.csv", "a+", newline=''), fieldnames=field_names)
    def process_item(self, item, spider):
        self.csvwriter.writerow(item)
        print("wrote to csv")
        return item   
    def close_spider(self, spider):
        print("Done")
