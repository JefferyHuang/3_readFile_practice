
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

new = []
for l in data:
    if len(l) < 100:
        new.append(l)
print("總共有", len(new), "筆資料長度小於100")
print(new[0])

good = []
for l in data:
    if "good" in l:
        good.append(l)
print("總共有", len(good), "筆資料提到good")
print(good[2])

#快寫法
good = [l for l in data if good in l] #印出含有good的清單

bad = ["bad" in l for l in data] #印出 True 或 Flase
