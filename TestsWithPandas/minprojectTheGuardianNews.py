import pandas
import requests
from bs4 import BeautifulSoup


# Tacking the data from the website and treating it 

text_string = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text

# print(text_string[:200])

bsp_text = BeautifulSoup(text_string, 'html.parser')

list_news = bsp_text.find_all('span', attrs={'class':'short-desc'})


print(f"bsp_text type: {type(bsp_text)}")

print(f"list_news type: {type(list_news)}")

i = 5
print(f"list_news[{i}]: {list_news[i]}")

print("\n\nContent")

datas = []

for news in list_news:
    date = news.contents[0].text.strip() + ', 2017' # Extracting from the <strong>Jan. 25</strong> only the content
    comment = news.contents[1].strip().replace("“", '').replace("”", '')
    explanation = news.contents[2].text.strip().replace("(", '').replace(")", '')
    url = news.find('a')['href']
    datas.append((date, comment, explanation, url))
    
print(datas[1])


# Analysing the website data, that is stored in the tuple's list datas. With pandas

# df: DataFrame
df_news = pandas.DataFrame(datas, columns=['date', 'comment', 'explanation', 'url'])

# Printing the DataFrame information

print("\n\nPrinting the DataFrame information: \n\n")

print(f"df_news.shape: {df_news.shape}")

print(f"df_news.dtypes: {df_news.dtypes}")

df_news.head()



