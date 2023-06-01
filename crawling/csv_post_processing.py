import csv

input = open('input.csv','r', encoding='utf-8')
output = open('output.csv','w',encoding='utf-8',newline='')

csvReader = csv.reader(input)
csvWriter = csv.writer(output)

inputList = []

for line in csvReader:
    inputList.append(line)

print(inputList[117])

for i in inputList:
    if i[-1] == '' :
        while i[-1] =='':
            i.remove('')
        link = i[-1]
        i[-1] = ''
        while len(i) < 21:
            i.append('')
        i.append(link)

print(inputList[117])


csvWriter.writerows(inputList)

input.close()
output.close()