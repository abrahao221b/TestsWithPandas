import pandas
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# Class SiteExtraction
class SiteExtraction:
    '''url: string, tag: string, attribute: string, attribute_name: string, headline_name_tag: string, link_name: string, meta_data_name: string'''
    def __init__(self, url, tag, attribute, attribute_name, headline_tag, headline_at, 
                 headline_name_at, meta_data_tag, meta_data_at, meta_data_name_at):
        self.site = url
        self.tag = tag
        self.attribute = attribute
        self.attribute_name = attribute_name
        self.headline_tag = headline_tag
        self.headline_at = headline_at
        self.headline_name_at = headline_name_at
        self.meta_data_tag = meta_data_tag
        self.meta_data_at = meta_data_at
        self.meta_data_name_at = meta_data_name_at
    
    def extract(self):
        text_string = requests.get(self.site).text
        hour_extraction = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        bsp_text = BeautifulSoup(text_string, 'html.parser')
        list_news = bsp_text.find_all(f'{self.tag}', attrs={f'{self.attribute}': f'{self.attribute_name}'})
        data = []
        
        for news in list_news:
            headline = news.find(f'{self.headline_tag}', attrs={f'{self.headline_at}': f'{self.headline_name_at}'})
            link = news.find('a').get('href')
            news_contents_index = len(news.contents) - 1
            description = news.contents[news_contents_index].text 
            if not description:
                description = news.find(f'{self.tag}', attrs={f'{self.attribute}': f'{self.link_name}'})
                description = description.text if description else None
            meta_data = news.find(f'{self.meta_data_tag}', attrs={f'{self.meta_data_at}':f'{self.meta_data_name_at}'})
            time_delta = meta_data.find(f'{self.meta_data_tag}', attrs={f'{self.meta_data_at}': f'{self.meta_data_name_at}'})
            section = meta_data.find(f'{self.meta_data_tag}', attrs={f'{self.meta_data_at}': f'{self.meta_data_name_at}'})
            time_delta = section.text if section else None
            data.append((headline, description, link, section, hour_extraction, time_delta))
        
        df = pandas.DataFrame(data, columns=['headline', 'description', 'link', 
                                             'section', 'hour_extraction', 'time_delta'])
        
        return df