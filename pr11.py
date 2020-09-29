"""Măriuca ţine evidenţa iepurilor din crescătorie. Ea îşi notează câţi iepuri sunt la
începutul fiecărei luni, câţi au murit şi câţi s-au născut în cursul fiecăei luni. Puteţi să
realizaţi un program care, primind aceste date, să afişeze la sfârşitul fiecărei luni câţi
iepuri sunt în crescătorie? """
m=int(input("Numarul de iepuri la inceput de luna:"))
n=int(input("Numarul de iepuri morti:"))
p=int(input("Numarul de iepuri nascuti:"))
t=m-n+p
print("La sfarsitul acestei lnin in crescatorie sunt",t,"iepuri")