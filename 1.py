def cetak_gambar(n):
  if n % 2 == 0:
    print("Bilangan n harus ganjil")
  elif n == 1:
    print('*')
  else:
    for i in range(1,n+1):
      mid=(n//2)+1
      if i == mid:
        print("* "*n)
      else:
        print("* "+"= "*(n-2)+"*")


cetak_gambar(5)