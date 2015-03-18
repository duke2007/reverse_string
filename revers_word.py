#Un program care inverseaza cuvintele
#Programul functioneaza atata timp cat userul nu
#scrie cuvantul No

raspuns ="No"
raspuns = input("Introdu un cuvant (No ca sa iesi) ")
print (raspuns, "inversat este", raspuns[::-1])
while raspuns != 'No' :
    raspuns = input("Introdu un alt cuvant ('No' ca sa iesi) ")
    print (raspuns, "inversat este", raspuns[::-1])
