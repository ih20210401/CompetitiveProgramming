#str = input()  # sはstr型
str = "FisHDoGCaTAAAaAAbCAC"

index = 0

length = len(str)

resultList = []
while index < length :

    word = ""
    word += str[index]
    index += 1

    while index < length and str[index].islower() :
        word += str[index]
        index += 1

    word += str[index]
    index += 1
    #print(word)
    resultList.append(word)

#sorted(resultList,key=str.lower)
#resultList.sort(key=str.lower)
resultList.sort(key=str.upper)

for val in resultList :
    print(val,end="")
