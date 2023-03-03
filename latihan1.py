#SOAL NO 1
for i in range(1,101):
    print(i)

#SOAL NO 2
print("Program bilangan bulat 1 hingga n")
n = int(input("Masukkan bilangan bulat: "))
for i in range(n+1):
  if(i%2 == 0):
    continue
  else:
    print(i)

#SOAL NO 3
print("Program bilangan bulat 1 hingga n")
n = int(input("Masukkan bilangan bulat: "))
def cek_genap_ganjil(bilangan):
  for i in range(n):
    if bilangan % 2 == 0:
        print(f"{bilangan} adalah bilangan genap")
    else:
        print(f"{bilangan} adalah bilangan ganjil")

for i in range(100):
    cek_genap_ganjil(i)

