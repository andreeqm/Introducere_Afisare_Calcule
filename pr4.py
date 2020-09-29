"""Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre. Numărul globuleţelor
albe se citeşte de la tastatură. Câte globuleţe are brăduţul, ştiind că numărul de
globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, iar globuleţele
albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii. """
na=int(input("Introduceti numarul de globulete albe:"))
nr=3+na
nb=(na+nr)-2
total=na+nb+nr
print("Bradutul are",total,"globulete")