import requests as rq
from bs4 import BeautifulSoup
import csv
import json


def write_csv(data):
    with open('WbFirstTest1.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow([data['name'],
                         data['supplier'],
                         data['cost'],
                        data['url']])



def get_data(url):
    div = rq.get(url).text
    data = json.loads(div)
    data1 = data.get("data").get('products')
    for i in range(len(data1)):
        name = data1[i].get('name')
        cost = str(data1[i].get('priceU'))[:2]
        supplier = data1[i].get('supplier')
        url = 'https://www.wildberries.ru/catalog/' + str(data1[i].get('id')) + '/detail.aspx?targetUrl=SP'
        lastdata = {'name':name,
                    'cost':cost,
                    'supplier':supplier,
                    'url':url}
        write_csv(lastdata)



for i in range(1,11):
    print(get_data(f"https://catalog.wb.ru/catalog/bl_shirts/catalog?TestGroup=sim_goods_srch_infra&TestID=323&appType=1&cat=8126&curr=rub&dest=-1257786&page={i}&sort=popular&spp=25"))
