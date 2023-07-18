import csv

# file setting
input = open('test3.csv','r',encoding='utf-8')
output = open('test4.csv','w',encoding='utf-8',newline='')

# csv reader/writer setting
csvReader = csv.reader(input)
csvWriter = csv.writer(output)

# csv read
inputList = []

for line in csvReader:
    inputList.append(line)

# csv output list
outputList = [['가게이름',
              '음식이 맛있어요',
              '친절해요',
              '특별한 메뉴가 있어요',
              '매장이 청결해요',
              '재료가 신선해요',
              '가성비가 좋아요',
              '양이 많아요',
              '인테리어가 멋져요',
              '혼밥하기 좋아요',
              '링크']]

# read and calc each keyword's percentage
for i in inputList[1:]:
    tempList = [i[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, i[-1]]  # 가게이름, 키워드 9개, 링크
    numList = []
    for j in range(1,10):
        numList.append(int(i[j]))

    total = sum(numList)
    for j in range(1,10):
        tempList[j] = round(int(i[j])/total,3)

    outputList.append(tempList)

# csv write
csvWriter.writerows(outputList)