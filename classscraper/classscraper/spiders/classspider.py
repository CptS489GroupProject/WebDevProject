import scrapy

MAJOR_LIST = []
MAJOR_LEN = 0
INDEX = 0
COND = True

class ClassspiderSpider(scrapy.Spider):
    name = "classspider"
    allowed_domains = ["catalog.wsu.edu"]
    start_urls = ["https://catalog.wsu.edu/Pullman/Courses/"]

    def parse(self, response):
        global COND
        global INDEX
        if COND:
            global MAJOR_LIST
            global MAJOR_LEN
            majors = response.css('td.input option')
            for major in majors:
                MAJOR_LIST.append((major.css('::text').get()).strip()) # grab major names and remove whitespace
            MAJOR_LIST = list(set(MAJOR_LIST)) # remove duplicates
            MAJOR_LIST = [ x for x in MAJOR_LIST if "[" not in x and len(x) > 1]
            COND = False
            MAJOR_LEN = len(MAJOR_LIST)
        else:
            classes = response.css('p.course')
            for item in classes:
                yield{
                    'name' : item.css('span.course_header::text').get().strip(),
                    'description' : item.css('span.course_data::text').get().strip()
                }
        if INDEX != MAJOR_LEN:
            cur_url = 'https://catalog.wsu.edu/Pullman/Courses/BySubject/' + MAJOR_LIST[INDEX]
            INDEX += 1
            yield scrapy.Request(url=cur_url, callback=self.parse)

        
            
    
        
        
