import time

data = []
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
       data.append(line) 
       count += 1
       if count % 100000 == 0:
        print(len(data))
print("檔案讀取完了，總共有", len(data), "筆資料")


#文字計數
start_time = time.time()
wc = {} #word_count
for d in data:
    words = d.split(" ")
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增新的key進字典
for word in wc:
    if wc[word] > 100:
        print(word, wc[word])
end_time = time.time()

print("花了", end_time - start_time, "秒")
print(len(wc))

while True:
    word = input("請問想查甚麼字: ")
    if word == "q":
        break
    if word in wc:
        print(word, "出現過的次數為:", wc[word])
    else:
        print("這個字沒有出現過")
print("感謝使用本次查詢功能")


