#zad1
# lista = ['Pustkowie Smauga', 'Niezwykla podroz', 'Bitwa pieciu armii', 'Dwie wieze']
# print(lista)
# lista.reverse()
# print(lista)
# lista.insert(5,'Druzyna pierscienia')
# lista.append('Interstellar')
# lista.append('Theory of Everything')
# lista.append('Star wars jedi awaken')
# lista.append('Star wars last jedi')
# lista.append('The thing')
# print(lista)
# # zad2
# slownik={'top1':lista[0], 'top2':lista[1], 'top3':lista[2],
#          'top4':lista[3], 'top5':lista[4], 'top6':lista[5],
#          'top7':lista[6], 'top8':lista[7], 'top9':lista[8],
#          'top10':lista[9]}
# print(slownik['top1'])
# zad3
# slownik3={1:'CAD-komputerowe wspomaganie projektowania', 2:'Wizualizajca danych', 3:'J.angielski', 4:'Prog. strukt.', 5:'El. mat. dys.', 6:'Rachunek rozn.'}
# x=len(slownik3)
# print(x)
# zad4
# liczba=input("Podaj liczbe")
# liczba=int(liczba)
# liczba**=liczba
# print(liczba)
# zad5
# import sys as system
# system.stdout.write("Wpisz dowolny komunikat: \n")
# napis=system.stdin.readline()
# print(type(napis))
# system.stdout.write(napis)
# x=napis.count("a")
# print(x)
# zad6
# a=input("Podaj a: \n")
# a=int(a)
# b=input("Podaj b: \n")
# b=int(b)
# c=input("Podaj c: \n")
# c=int(c)
# if (a%2==0) & (b>c):
#     print("liczba "+str(a)+" jest parzysta oraz jednoczescie "+str(b)+" jest wieksze od "+str(c))
# else:
#     print("liczby sie nie zgadzaja")
# zad7
# lista=[1,2.5,3,4.5,5,6.5,7,8.5]
# for i in range(1,len(lista),1):
#     print(lista[i]+lista[i-1])
# zad8
# lista1=[]
# lista2=[]
# i=0
# while i<10:
#     x=input("Podaj liczbe "+str(i+1)+" : \n")
#     i+=1
#     lista1.append(x)
#
# print(lista1)
# for i in range(0,len(lista1),1):
#     if int(float(lista1[i]))==float(lista1[i]):
#         lista2.append(int(float(lista1[i])))
#
# print(lista2)
# zad9
# lista=[1,2,3,4,5,6]
# for i in lista:
#     if i==1 or i==6:
#         print("O"*6)
#     else:
#         print("O    O")
# zad10
# x=input("Podaj liczbe: \n")
# try:
#     float(x)/float(x)
#     print("to liczba")
# except ValueError:
#     print("to nie liczba")



