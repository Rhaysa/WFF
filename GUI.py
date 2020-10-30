import PySimpleGUI as sg  #se introduc modulele de la pachetul PySimpleGUI pentru a avea o interfata grafica
from Tema1 import wff
#layout-ul cuprinde toate elementele interfetei grafice
layout = [  [sg.Text("Introduceți un șir de simboluri pentru a decide dacă șirul respectiv este o formulă propozițională.")],                       #textul afisat care ne cere sirul de simboluri
            [sg.Input(key='input',size=(70,1))],                                                                                                    #casuta de input cu dimensiunea ei
            [sg.Button('('), sg.Button(')'), sg.Button('∧'), sg.Button('∨'), sg.Button('→'), sg.Button('↔'), sg.Button('¬'), sg.Button('Șterge')],  #butoanele pentru introducerea simbolurilor, exceptand literele
            [sg.Output(size=(70,1))],                                                                                                               #casuta de output (ne afisează formula propozițională introdusă și dacă este sau nu validă)
            [sg.Button('Verifică')] ]                                                                                                               #butonul de executare a codului ("Verifică")
window = sg.Window('Temă 1', layout, default_button_element_size=(5,2), auto_size_buttons=False)  #crearea ferestrei cu denumirea ei, marimea butoanelor
valoari_introduse = ''                                                                            #se initializeaza o variabila care retine sirul introdus
while True:                                                                                       #structura repetitiva infinita cat timp nu se realizeaza niciun eveniment
    eveniment, valori = window.read()                                                             #se citesc evenimentele si valorile din fereastra constant
    if eveniment == sg.WIN_CLOSED:                                                                #se verifica daca utilizatorul inchide fereastra/programul prin butonul "X" din coltul din dreapta sus
        break                                                                                     #odata apasat butonul se iasa din structura repetiva, astfel se inchide programul
    if eveniment == 'Șterge':                                                                     #daca utilizatorul apasa pe butonul "Sterge" variabila initiala devine din nou nula, stergandu-se din memorie elementele de pana atunci
        valori_introduse = ''
    elif eveniment in '(¬∧∨→↔)':                                                                  #daca utilizarorul apasa pe unul din butoanele de simboluri se adauga valoarea lor in variabila initiala
        valori_introduse = valori['input']                                                        #ceea ce s-a introdus deja
        valori_introduse += eveniment                                                             #se adauga noul caracter
    elif eveniment == 'Verifică':                                                                 #daca utilizatorul apasa butonul "Verifica" incepe executia programului de verificare a formulei propozitionale
        valori_introduse = valori['input']                                                        #ceea ce s-a introdus deja
        wff(valori_introduse)                                                                     #se executa codul pentru ceea ce este stocat in variabila "valori_introduse" si se afiseaza rezultatul sau
    window['input'].update(valori_introduse)                                                      #se schimba in fereastra sirul introdus constant