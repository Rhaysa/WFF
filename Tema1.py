def transformare(expresie): 																#procedura prin care eliminam spatiile din sirul de simboluri si eliminam parantezele negatiei
	listaCaractere = []																		#se creaza o lista unidimensionala in care retinem simbolurile exceptand spatiile
	for caracter in expresie:																#structura repetitiva care parcurge ficare caracter din sir
		if((caracter.isalpha()) or (caracter in ['∧', '∨', '→', '↔', ')', '(', '¬', ' '])):	#structura decizionala care verifica daca caracterul este litera sau disjunctie/conjuctie/implicare/echivalenta/paranteza/spatiu
  			if(not(caracter == ' ')):														#structura decizionala care verifica daca caracterul este spatiu sau nu
  				listaCaractere.append(caracter)												#daca caracterul nu era spatiu este adaugat in lista 
		else:
			return False, listaCaractere													#daca caracterul nu era litera sau disjunctie/conjuctie/implicare/echivalenta/paranteza sirul de simboluri nu este o formula propozitionala
	i = 1
	while i<len(listaCaractere):															#structura repetitiva care parcurge noul sir de simboluri fara spatii
		if listaCaractere[i] == "¬":														#structura decizionala care verifica daca caracterul este negatie sau nu
			if listaCaractere[i-1] == '(': 													#structura decizionala care verifica daca caracterul anterior este paranteza de deschidere sau nu 
				intermediar = listaCaractere[i:]											#se retine intr-o variabila lista de simboluri de la caracterul curent pana la ultimul
				intermediar.remove(")")														#se elimina urmatoarea paranteza rotunda care forma setul pentru negatie
				listaCaractere = listaCaractere[:(i-1)] + intermediar						#se formeaza sirul final dintr-o lista de simboluri formata din toate elementele dinaintea parantezei de deschidere a negatiei si variabila intermediat, astfel se indepartea paranteza de deschidere
			else:
				return False,listaCaractere													#daca caracterul anterior nu era paranteza de deschidere nu se respecta sintaxa, astfel sirul nu este o formula propozitionala
		else:
			i += 1																			#daca elementul nu este negatie se trece la elementul urmator
	return True,listaCaractere																#se returneaza sirul final care trebuie verificat fara spatii si dupa ce au fost verificate parantezele negatiei

def parcurgere_formula(restulListei):												#procedura recursiva de verificare a fiecarui element din sir
	ok_propozitie, restulListei= element(restulListei,1)							#stocam in doua variabile daca elementul este propozitie si restul listei care trebuie verificate fara elementul deja verificat in cazul in care elementul era propozitie
	if ok_propozitie:																#daca elementul era propozitie returnam adevarat si restul listei care trebuie verificate fara elementul deja verificat
		return True, restulListei
	ok_negatie, restulListei = element(restulListei,2)								#stocam in doua variabile daca elementul este negatie si restul listei care trebuie verificate fara elementul deja verificat in cazul in care elementul era negatie
	if ok_negatie:																	#daca elementul era negatie verificam daca noua lista este formula (reapelam recursiv procedura)
		ok_formula, restulListei = parcurgere_formula(restulListei)					#stocam in doua variabile daca elementul returneaza adevarat (este formula) si restul listei care trebuie verificate fara elementul deja verificat in cazul in care elementul respecta conditia
		if ok_formula:												
			return True, restulListei
	ok_paranteza_deschidere, restulListei = element(restulListei,3)					#stocam in doua variabile daca elementul este paranteza de deschidere si restul listei care trebuie verificate fara elementul deja verificat in cazul in care elementul era paranteza de deschidere
	if ok_paranteza_deschidere:														#daca elementul era paranteza de deschidere verificam daca noua lista este formula (reapelam recursiv procedura)
		ok_formula, restulListei = parcurgere_formula(restulListei)					#stocam in doua variabile daca elementul returneaza adevarat sau fals (daca este formula) si restul listei care trebuie verificate fara elementul deja verificat in cazul in care elementul respecta conditia
		if ok_formula:																#daca variabila de verificare a formulei era adevarata verificam daca elementul prim al noii liste este operator 
			ok_operator, restulListei= element(restulListei,5)						#stocam in doua variabile daca elementul este operator si restul listei care trebuie verificate fara elementul deja verificat in cazul in care elementul era operator
			if ok_operator:															#daca elementul era operator verificam daca noua lista este formula (reapelam recursiv procedura)
				ok_formula, restulListei = parcurgere_formula(restulListei)			#stocam in doua variabile daca elementul returneaza adevarat sau fals (daca este formula) si restul listei care trebuie verificate fara elementul deja verificat in cazul in care elementul respecta conditia
				if ok_formula:														#daca variabila de verificare a formulei era adevarata verificam daca elementul prim al noii liste este paranteza de inchidere 
					ok_paranteza_inchidere, restulListei = element(restulListei,4)	#stocam in doua variabile daca elementul este paranteza de inchidere si restul listei care trebuie verificate fara elementul deja verificat in cazul in care elementul era paranteza de inchidere
					if ok_paranteza_inchidere:										#daca elementul era paranteza de inchidere rerturnam adevarat si restul listei
						return True, restulListei
	return False, restulListei

def element(restulListei, tip): 									#procedura care verifica daca avem o propozitie/negatie/paranteza/operator
	if (len(restulListei) == 0): 									#conditia care verifica daca sirul este nenul sau nu 
		return False, restulListei									#daca lungimea sirului este 0, s-a parcurs toata lista si inca nu s-a demonstrat ca sirul este o formula propozitionala
	cazuri= {														#toate cazurile posibile in functie de tipul ales
		1: lambda x: (x.isalpha()), 								#tipul 1 reprezinta propozitiile (notate cu litere)
		2: lambda x: (x == '¬'),									#tipul 2 reprezinta negatia
		3: lambda x: (x == '('),									#tipul 3 reprezinta paranteza rotunda de deschidere la stanga
		4: lambda x: (x == ')'),									#tipul 4 reprezinta paranteza rotunde de inchidere la dreapta
		5: lambda x: (x in ['∧', '∨', '→', '↔'])					#tipul 5 reprezinta operatorii (conjunctie, disjunctie, implicare, echivalenta)
	}
	if cazuri[tip](restulListei[0]):								#conditie care verifica daca elementul respecta tipul cautat
		restulListei.remove(restulListei[0])						#eliminam elementul deja verificat, trecand la urmatorul	
		return True, restulListei									#daca elementul respecta tipul cautat returneaza adevarat si noul sir de verificat
	return False, restulListei										#daca elementul nu respecta tipul cautat returneaza fals si noul sir de verificat

def wff(expresie):													#procedura principala a programului care primeste ca paramentru sirul de simboluri care trebuie validat
	print(expresie)													#se afiseaza sirul de simboluri care trebuie validat
	expresie = expresie.upper()										#se transforma toate litere mici in litere mari (notatia propozitiilor se face doar cu litere mari)
	ok, restulListei = transformare(expresie)						#se retine intr-o lista unidimensionala sirul de caractere care trebuie validat dupa ce au fost eliminate spatiile si parantezele negatiei prin procedura "transformare"
	if ok:															#daca dupa procedura de trasnformare variabila ok este adevarata (nu se gasesc simboluri necorespunzatoare si se respecta parantezele negatiei) se verifica sirul		
		ok_formula, restulListei = parcurgere_formula(restulListei)	#se stocheaza in variabila ok_formula adevarat/fals dupa parcurgerea sirului si verificarea acestuia, iar in variabila restulListei ceea ce ramane din sir dupa executia procedurii de verificare
		if(ok_formula and len(restulListei) == 0):
			print("ADEVĂRAT - Este o formulă propozițională")		#daca dupa procedura de verificare se returneaza Adevarat si lungimea sirului este 0(s-a parcurs tot sirul) atunci sirul este o formula propozitionala si se afiseaza True
		else:
			print("FALS - Nu este o formulă propozițională")		#daca nu, se afiseaza False
	else:
		print("FALS - Nu este o formulă propozițională")			#daca variabila ok este falsa (se gasesc simboluri necorespunzatoare sau nu se respecta parantezele negatiei) se afiseaza Fals