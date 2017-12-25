name = []
data = ""
count = 0
print(range(len(data)))

while data != 'q':
    print('Please enter your name : ')
    data = input()
    name.append(data)
name.remove(data)

print('Please enter any one letter')
lettersearch=input()

while len(lettersearch) != 1:
    print('Please enter correct search')
    print('Please enter any one letter Again')
    lettersearch = input()

count = 0
for v in range(len(name)):
    for i in range(len(name[v])):
       if lettersearch.lower() in name[v][i] or lettersearch.upper() in name[v][i]:
            count += 1
print(lettersearch,'appeared for', count, 'times')
