# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ClassscraperPipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)
        description = adapter.get('description')
        split_string = description.split('Course Prerequisite: ')
        if len(split_string) == 2 :
            temp = split_string[1].split('.')
            adapter['prereq'] = temp[0]

            del temp[0]
            adapter['description'] = split_string[0] + ".".join(temp)
        return item
