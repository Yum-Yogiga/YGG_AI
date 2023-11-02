import csv

input = open('review_count.csv','r', encoding='utf-8')
output = open('review_count_postprocessing.csv','w',encoding='utf-8-sig',newline='')

csvReader = csv.reader(input)
csvWriter = csv.writer(output)

inputList = []

for line in csvReader:
    inputList.append(line)

print(inputList[77])

for i in inputList:
    if len(i) < 21:
        link = i[-1]
        i[-1] = ''
        while len(i) < 21:
            i.append('')
        i.append(link)

    #get link data
    stringTemp = i[-1]
    #불필요한 문자열 제거
    #https://map.naver.com/v5/entry/place/ 앞 37 문자 제거
    #\n?c=15,0,0,0,dh 뒤 15문자 제거

    stringTemp = stringTemp[37:-14]
    i[-1]=stringTemp

print(inputList[77])


csvWriter.writerows(inputList)

input.close()
output.close()