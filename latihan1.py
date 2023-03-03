#SOAL NO 1
print("Soal No 1")
for i in range(1,101):
    print(i)

#SOAL NO 2
print("Soal No 2")
for i in range(1,101):
  if(i%2 == 0):
    continue
  else:
    print(i)

#SOAL NO 3
print("Soal No 3")
def is_odd(num):
    return num % 2 == 1

for i in range(1,101):
    if is_odd(i):
        print(i)

