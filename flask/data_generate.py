import csv
import random

file = open('data/data.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(file)

list = [["text", "target"]]

# target = [a,b,c,d,e,f,g,h,i]
# a 음식이 맛있어요
# b 친절해요
# c 특별한 메뉴가 있어요
# d 매장이 청결해요
# e 재료가 신선해요
# f 가성비가 좋아요
# g 양이 많아요
# h 인테리어가 멋져요
# i 혼밥하기 좋아요

text_set = [["음식이 맛있고 ","음식이 맛있는 곳"],
            ["친절하고 ","친절한 곳"],
            ["메뉴가 특별하고 ", "메뉴가 특별한 곳"],
            ["깨끗하고 ","깨끗한 곳"],
            ["재료가 신선하고 ","재료가 신선한 곳"],
            ["가성비가 좋고 ","가성비가 좋은 곳"],
            ["양이 많고 ","양이 많은 곳"],
            ["인테리어가 이쁘고 ", "인테리어가 이쁜 곳"],
            ["혼밥하기 좋고 ", "혼밥하기 좋은 곳"]]

for i in range(10000):
    iter = random.randrange(2,10)
    data_range = random.sample([0,1,2,3,4,5,6,7,8],iter)
    target_list = [0,0,0,0,0,0,0,0,0]
    text_list = ""

    for dr in data_range[0:len(data_range)]:
        target_list[dr] = 1
        text_list = text_list + text_set[dr][0]

    target_list[data_range[len(data_range)-1]] = 1
    text_list = text_list + text_set[data_range[-1]][1]

    list.append([text_list, target_list])

csvWriter.writerows(list)