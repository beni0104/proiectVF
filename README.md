# Proiect verificare formală 
**SAT solving using minisat solver**
În cadrul acestui proiect, ne propunem să analizăm funcționalitatea *MiniSat* prin testarea unui benchmark folosit în competiția *SAT Competition 2024*. 
Am finalizat sarcinile principale: rularea unei familii de input-uri, evaluarea rezultatelor obținute și analiza codului la un nivel general, iar în săptămânile următoare ne propunem să aprofundăm și să clarificăm aspectele lucrării realizate până acum.

**SĂPTĂMÂNA 12**
* am adăugat explicații pentru diagramele realizate
  
**SĂPTĂMÂNA 11**
* am extins secțiunile de rezultate experimentale și provocări
  
**SĂPTĂMÂNA 10**
* ne-am consultat cu privire la problemele identificate în raportul nostru și am revizuit planul pentru săptămânile următoare
* am modificat diagrama de clase (de modificat și descrierea din raport)
* am făcut o primă variantă a diagramei de secvențe
===========================================================================
**INSTALARE MINISAT**
  
*Windows*
1. clonarea proiectului de la adresa:
   https://github.com/niklasso/minisat
2. configurarea mediului pentru compilarea (MinGW) și build-ul (CMake) proiectului clonat
3. executarea în linia de comandă a comenzilor:
   
   `cmake -G "MinGW Makefiles" ..`
   
   `cmake --build .`
4. în final, s-a generat executabilul *minisat.exe*
5. rularea comenzii pentru testarea minisat:
    `minisat.exe input.cnf`
*Linux*
1. executarea în terminal a comenzii:
   `sudo apt install minisat`
2. rularea comenzii pentru testarea minisat:
   `minisat input.cnf`
===========================================================================
**MEMBRII ECHIPEI ȘI SARCINILE FIECĂRUIA**
**Moise Alexandra** (alexandra.moise02@e-uvt.ro):
  * analizarea structurii generale a codului (metode și structuri de date)
  * contribuție la realizarea diagramelor UML
  * crearea fișierelor readme și license
    
**Stancu Maria** (maria.stancu03@e-uvt.ro)
  * redactarea raportului 
  * realizarea diagramelor UML
    
**Szekrenyes Benjámin** (benjamin.szekrenyes02@e-uvt.ro)
  * rularea benchmark-ului
  * analizarea rezultatelor obținute
    
**Anghel Bogdan** (bogdan.anghel00@e-uvt.ro)
  * redactarea raportului
  * analizarea rezultatelor obținute
