from restaurant_info import crawl
import csv

search_list = set()

sl_file = open('link.txt','r')
while True:
    temp = sl_file.readline()
    temp = temp.replace('review/visitor', 'home')
    if not temp: break
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
    csv_list = [['name','address','tel','openingHours','menu1','price','menu2','price','menu3','price','menu4','price']]
    for dict in dict_list:
        templist = [dict['name'],dict['address'],dict['tel'],dict['openingHours']]
        keys = list(dict['menuDtoList'].keys())
        values = list(dict['menuDtoList'].values())
        for i in range(len(keys)):
            templist.append(keys[i])
            templist.append(values[i])
        csv_list.append(templist)

    w.writerows(csv_list)
    f.close()
