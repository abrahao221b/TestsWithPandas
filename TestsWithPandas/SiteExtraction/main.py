from tackingSiteContent import SiteExtraction


siteExtraction = SiteExtraction("https://www.ibge.gov.br/", "li", "class", "tipo-n pure-u-1 pure-u-md-1-2", 
                                "h3", "class", "", "span", "class", "home-noticia-data")

df = siteExtraction.extract()

print(type(df))
print(df.info)