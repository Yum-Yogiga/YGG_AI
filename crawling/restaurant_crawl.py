from restaurant_info import crawl
from crawl_copy import crawling
import csv

search_list = []

sl_file = open('storeNumber.txt','r',encoding='utf-8')

while True:
    temp = sl_file.readline()
    if not temp: break
    temp = f'https://m.place.naver.com/restaurant/{temp}/home'
    search_list.append(temp)


sl_file.close()

# return list
dict_list = []

# # set to list
# search_list = list(search_list)

# crawl
dict_list = crawling(search_list)

with open('restaurant_crawling.csv','w',encoding='utf-8-sig',newline='') as f:
    w = csv.writer(f)
    # 추후에 필요시 tel 과 menu1 사이에 ,'openingHours' 추가
    csv_list = [['name','address','tel','menu1','price','image1','menu2','price','image2','menu3','price','image3','menu4','price','image4']]
    for dict in dict_list:
        templist = [dict['name'],dict['address'],dict['tel']]
        names = list(dict['menuDtoList'].keys())
        try:
            prices ,images = zip(*dict['menuDtoList'].values())
            prices = list(prices)
        except:
            prices, images = ["none","none","none","none"], ["none","none","none","none"]
        for i in range(len(names)):
            templist.append(names[i])
            templist.append(prices[i])
            templist.append(images[i])
        csv_list.append(templist)

    w.writerows(csv_list)
    f.close()
