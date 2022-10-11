from lxml import etree
from bs4 import BeautifulSoup
import requests
from crazytimemodel import CrazyTimeModel

class bestwin_sendtext:

    def load(bot_message_winbot_message_win):
        elenco = []
        URL = "https://tracksino.com/crazytime/"
        webpage = requests.get(URL)
        soup = BeautifulSoup(webpage.content , "html.parser")
        dom = etree.HTML(str(soup))
        multi_name_1 = (dom.xpath('//*[@class="gameevents-table table-responsive"/table/tbody/tr[3]/td[2]/text()'))
        
        multi_name_2 = (dom.xpath('//*[@class="gameevents-table table-responsive"/table/tbody/tr[3]/td[2]/text()'))
        
        multi_name_3 = (dom.xpath('//*[@class="gameevents-table table-responsive"/table/tbody/tr[3]/td[2]/text()'))
        
        multipli_1 = (dom.xpath('//*[@class=""wrapper container-fluid""]/div/div[4]/div[1]/div/div/div/div/div[1]/div[1]/span/span/text()'))
        multipli_2 = (dom.xpath('//*[@class=""wrapper container-fluid""]/div/div[4]/div[1]/div/div/div/div/div[2]/div[1]/span/span/text()'))
        multipli_3 = (dom.xpath('//*[@class=""wrapper container-fluid""]/div/div[4]/div[1]/div/div/div/div/div[3]/div[1]/span/span/text()'))
        
        timestamp_1 = (dom.xpath('//*[@class="pt-2 container-fluid"/div[1]/div[2]/text()'))
        timestamp_2 = (dom.xpath('//*[@class="pt-2 container-fluid"/div[2]/div[2]/text()'))
        timestamp_3 = (dom.xpath('//*[@class="pt-2 container-fluid"/div[3]/div[2]/text()'))
        
        
        
        send_text = 'I migliori moltiplicatori di oggi sono:' + str(multi_name_1) + ' con il' + str(multipli_1) + 'il' + str(timestamp_1) + str(multi_name_2) + ' con il' + str(multipli_2) + 'il' + str(timestamp_2) + str(multi_name_3) + ' con il' + str(multipli_3) + 'il' + str(timestamp_3)
        
        ##res = (dom.xpath('//*[@class="subtitle"]/b/text()'))
        ##indice = (dom.xpath('//*[@class="card-body"]/center/div/div/div/img/@alt'))
        ##lista = dict(zip(indice,res))
        #for key,value in lista.items():
        #    if "Crazy Time" not in key and "Bonus" not in key: 
        #        a = CrazyTimeModel(key.replace("Segment", ""),value)
        #        elenco.append(a) 
        #    elif "Bonus" not in key :
        #        a = CrazyTimeModel(key.replace("Crazy Time","").replace("Segment", ""),value)
        #        elenco.append(a)
        #    else:
        #        a = CrazyTimeModel(key.replace("Segment", ""),value)
        #        elenco.append(a
