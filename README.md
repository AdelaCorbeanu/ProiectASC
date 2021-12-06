# ProiectASC
Fisierul encrypt.py cripteaza textul din fisierul input.txt prin criptare XOR, folosind o cheie primita in linia de comanda si returneaza rezultatul in fisierul output.

Sintaxa: python encrypt.py input.txt cheie output

Fisierul decrypt.py decripteaza textul din fisierul output prin metoda XOR, folosind cheia primita in linia de comanda, si returneaza rezultatul in fisierul input_recuperat.txt

Sintaxa: python decrypt.py output cheie input_recuperat.txt

Resurse utilizate:
https://en.wikipedia.org/wiki/XOR_cipher
https://www.w3resource.com/python/python-bytes.php
https://www.codegrepper.com/code-examples/python/python+byte+to+char
https://pteo.paranoiaworks.mobi/diacriticsremover/
https://text-compare.com/


Partea a doua a proiectului:

**!Cheia este "cheiaCHEILOR12"**
1) gasirea cheii folosind atat input-ul, cat si output-ul

Folosind programul findKey.py am aplicat operatia XOR intre elementele din input si cele din output pentru primele 49 de elemente. Afisand rezultatul, obtinem: cheiaCHEILOR12cheiaCHEILOR12cheiaCHEILOR12cheiaCH

Deoarece se observa cu usurinta ca sirul care se repeta la afisare este "cheiaCHEILOR12" nu mai sunt necesare verificari suplimentare, acesta fiind parola.
(Observatie: fisierul output a fost utilizat raportat la fel in care a fost conceput de echipa respectiva - cu extensia .txt, continand reprezentarea in baza 2 a caracterelor criptate)

2) gasirea cheii folosind doar output-ul
