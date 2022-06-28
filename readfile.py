from this import d


data = []
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
       data.append(line) 
       count += 1
       if count % 100000 == 0:
        print(len(data))
print("檔案讀取完了，總共有", len(data), "筆資料")

sumLen =  0
for l in data:
    sumLen = sumLen + len(l)

print("留言的平均長度為", sumLen/len(data))
