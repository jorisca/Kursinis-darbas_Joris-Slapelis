#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Sveiki atvykę į žaidimą "Klasikinės kartuvės"!

#Pasveikinti žaidėją
vardas = input("Įveskite savo vardą: ")
print("Labas, " + vardas, ".Pažaiskime klasikines kartuves!")

print("Taigi, koks yra tavo pirmas spėjimas?")

#Mūsų žaidimo žodis: vasara
žodis = "vasara"

#Sukurti kintamąjį su tuščia reikšme
spėjimai = ''

#Nustatyti bandymų skaičių
bandymai = 10

#Patikrinkite ar skaičius yra didesnis nei nulis
while bandymai > 0:         

    #Klaidų skaičiavimas prasideda nuliu 
    klaida = 0             

    #Kiekvienam slaptojo žodžio simboliui   
    for x in žodis:      

    #Atpausdinti, jei raidė yra žaidėjo spėjime
        if x in spėjimai:    
          print(x)
        else:
   
        #Jei neatspėjo, atspausdinti brūkšnį
            print("_")
       
        #Gavus klaidingą spėjimą, padidinti nepavykusių bandymų skaičių +1
            klaida += 1    

    #Jeigu teisingai, atspausdinti laimėjimą
    if klaida == 0:        
        print("Bravo! Tu laimėjai!")

    #Palikti programą
        break              

    print()
    #Prašyti žaidėjo spėti raidę
    spėjimas = input("Atspėk raidę: ") 

    #Žaidėjų spėliojimas
    spėjimai += spėjimas                    

    #Jeigu spėjimo raidė nėra rasta žodyke
    if spėjimas not in žodis:  
 
     #Tada bandymų skaičius mažėja po -1
        bandymai -= 1        
        print("Klaidingas spėjimas")    
 
    #Kiek liko bandymų
        print("Tu turi likusius", + bandymai, 'spėjimus')  
    #Jeigu liko nulis bandymų, žaidėjas išnaudojo visus 10 ėjimų
        if bandymai == 0:           
    
        #Atspausdinti pralaimėjimą
            print ("Tu pralaimėjai")


# In[ ]:




