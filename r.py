#read file
data = []
avg_rew = 0
count = 0
with open('original.txt', 'r') as f:
    for line in f:
        data.append(line)
print('檔案讀取完畢,總共有', len(data), "筆資料")

for e_review in data:
    avg_rew += len(e_review)
print(avg_rew / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
good_str = []
for d in data:
    if 'good' in d:
        good_str.append(d)
print('一共有', len(good_str), '筆提到good')
print(good[0])


# 文字計數 
wc = {} # word count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增加新的key進wc字典
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
    
print(len(wc))

while True:
    word = input('請問你想查什麼字: ')
    if word == 'q':
        break
    if word in wc:     
        print(word, '出現過的次數為: ', wc[word],'次')
    else:
    	print('這個字沒出現過哦')

print('感謝使用')




