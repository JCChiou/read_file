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

