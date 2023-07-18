from restaurant_info import crawl
import csv

search_list = set()

sl_file = open('storeNumber.txt','r',encoding='utf-8')

while True:
    temp = sl_file.readline()
    if not temp: break
    temp = f'https://m.place.naver.com/restaurant/{temp}/home'
    search_list.add(temp)


sl_file.close()

# return list
dict_list = []

# set to list
search_list = list(search_list)

# crawl
dict_list = crawl(search_list)

print(dict_list)

with open('restaurant_crawling.csv','w',encoding='utf-8',newline='') as f:
    w = csv.writer(f)
    # 추후에 필요시 tel 과 menu1 사이에 ,'openingHours' 추가
    csv_list = [['name','address','tel','menu1','price','menu2','price','menu3','price','menu4','price']]
    for dict in dict_list:
        templist = [dict['name'],dict['address'],dict['tel']]
        keys = list(dict['menuDtoList'].keys())
        values = list(dict['menuDtoList'].values())
        for i in range(len(keys)):
            templist.append(keys[i])
            templist.append(values[i])
        csv_list.append(templist)

    w.writerows(csv_list)
    f.close()
