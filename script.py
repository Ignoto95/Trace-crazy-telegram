from lxml import etree
from bs4 import BeautifulSoup
import requests
from crazytimemodel import CrazyTimeModel

class Allert:

    def load(self):
        elenco = []
        URL = "https://tracksino.com/crazytime/"
        webpage = requests.get(URL)
        soup = BeautifulSoup(webpage.content , "html.parser")
        dom = etree.HTML(str(soup))
        res = (dom.xpath('//*[@class="subtitle"]/b/text()'))
        indice = (dom.xpath('//*[@class="card-body"]/center/div/div/div/img/@alt'))
        lista = dict(zip(indice,res))
        for key,value in lista.items():
            if "Crazy Time" not in key and "Bonus" not in key: 
                a = CrazyTimeModel(key.replace("Segment", ""),value)
                elenco.append(a) 
            elif "Bonus" not in key :
                a = CrazyTimeModel(key.replace("Crazy Time","").replace("Segment", ""),value)
                elenco.append(a)
            else:
                a = CrazyTimeModel(key.replace("Segment", ""),value)
                elenco.append(a)

        return elenco
