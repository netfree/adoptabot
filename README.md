# ADOPTABOT

<img src="https://github.com/netfree/adoptabot/blob/master/logo.jpg" width="240">

> **Mijloc didactic pentru elevii pasionați de informatică și robotică.**

* Link Presentare: goo.gl/z4QbuZ
* Resursele folosite se află în fișierul resurseFolosite.md 

**Echipă:**
Diana Țibre,
Andrei Muntean

**Profesori îndrumători:**
Adriana Chereș,
Mihaela Muntean

**Liceu:**
Liceul Teoretic **„Nicolae Bălcescu”** Cluj-Napoca

## Despre conținutul proiectului:

Fișierul **server.py** conține codul propriu-zis pe care l-am scris, iar celelalte fișiere sunt fișiere auxiliare, sursa lor fiind menționată în fișierul **resurseFolosite.md**.
Fișierul **server.py** conține un algoritm scris cu ajutorul funțiilor și procedurilor predefinite de Finch API care ocolește obstacole și reacționează prin mai multe metode la stimulii din mediu în care se află. (resprectiv temperatură și lumină puternică).

## Misiunea noastră: ##

În primăvara anului 2017, ne-am confruntat cu problema creării **unui robot autonom, cât mai ieftin posibil.** Înțelegem perfect că, din păcate, educația nu dispune de fondurile de care ar trebui să dispună pentru a le da elevilor șansa de a înțelege mai bine noțiunile informatice prin aplicarea lor, asa că ne-am luat misiunea de a găsi cea mai ieftină alternativă.

Ne-am orientat către o platformă deja existentă, Finch. Finch este un fel de robot ce conține o placă cu senzori și roți. Zic un fel de robot deoarece are toate principalele caracterisitici ale unui robot (senzori, motoare etc.) ,dar **nu poate funcționa independent**, având nevoie să fie în permanență conectat la un calculator pentru a-i putea fii controlați senzorii. 

Am corectat acest neajuns conectându-l la un micro-calculator și o baterie. Partea interesantă începând acum, fiind necesară configurarea acestuia pe un sistem **ARM** (Raspberry Pi).

## Preț total: ##
Finch Barebone Sensor and Motor Shield: 80$, Raspberry PI 30$ Baterie 15$ 
**Total: 125$**

## De ce este proiectul nostru un pas înainte pentru elevi? ##
*  le oferă șansa de a experimenta linux, rețelistică, de a învăța un limbaj nou de programare și ocazia de a folosi un framework (Finch API, funcții și proceduri deja definite de programatori, pe care aceștia doar le aplică), lucru care îi apropie pe elevi de industria IT,acolo unde nu scrii programul de la cap la coadă, ca în clasă sau ca la Olimpiadă, ci te folosești și de codul colegilor care lucrează pe același proiect. 
*  crearea unei reprezentări tangibile a codului


## Utilitate Practică: ##
* punerea în practică a noțiunilor de algoritmică prin transformarea robotului într-un mijloc didactic pentru elevii pasionați de informatică și robotică
* utilizarea acestuia oferă o imagine asupra modului în care funcționează un robot, felul în care acesta relaționează cu mediul și răspunde la stimuli prin intermediul senzorilor săi. 

## Electronică
* robotul are o autonomie calculată de 28 de ore și un timp de încărcare de 5 ore
este un robot autonom care relaționează cu mediul prin toți senzorii de care dispune: lumină, temperatură, proximitate și orientare
* robot autonom în mediu necunoscut datorită unui mini calculator (Raspberry Pi) și a unei baterii


## Mecanică

Finch barebone este deja echipat cu 2 motoare și senzori (temperatură, lumină, obstacole și accelerometru).
Acestea sunt puse într-un format compact pentru a rezista generațiilor de elevi care vor învăța cu ele.

## Software | Cum am făcut asta?

Am scris pe un card MicroSD  imaginea sistemului de operare pentru ARM, Raspbian. 


Pentru a ne conecta la o rețea wireless, am scris manual pe cardul MicroSD (din cauză că nu am dispus de un monitor HDMI), în partiția de Boot configurările necesare NIC-ului (plăcii de rețea). 
Fișierele de care aveam nevoie erau pe o partiție formatată ex4, acest tip nefiind suportat de către Windows, motiv pentru care am apelat la un LiveCD cu Linux pentru a ne permite descoperirea și editarea configuraților de rețea.

Cu ajutorul nmap, am scanat toate dispozitivele de pe rețea și am aflat adresa IP a Raspberry-ului, conectarea la robot se face prin tcp/ssh, modalitate care oferă acces la linia de comandă a Raspberry PI-ului. 

Se pare că portul 22 (tcp/ssh) era predefinit blocat pe Raspberry, așa că pentru a avea acces la linia de comandă, a fost necesară scrierea pe Cardul MicroSD a configurărilor necesare deschiderii portului 22 (tcp/ssh). 

Ajunși la linia de comandă, am descărcat cu wget fișierele necesare utilizării finch-ului și le-am adus în directorul proiectului. Din fericire, deși fișierele erau făcute să funcționeze pentru i386/AMD64, am reușit grație Python să le rulăm și pe ARM. 

Tot ce ne-a mai rămas de făcut era să facem un fișier cu nano și să scriem codul nostru acolo. Am folosit funcțiile și procedurile Finch-ului pentru a citi valorile senzorilor și de a da comenzi motoarelor.  După asta, am rulat programul cu comanda Python urmat de numele fișierului și a funcționat. 
Proiectul a fost un succes.

## Rolul fiecărui component al echipei de realizare a proiectului ##
**Diana** este partea creativă a echipei noastre, aceasta realizând suporturile vizuale de prezentare cât și o parte din documentația proiectului. Probabil că fără entuziasmul de care dă dovadă, nu am fii participat la Etapa județeană.

**Andrei** este o fire foarte curioasă, creativă și analitică care a venit cu tot felul de soluții ingenioase la diversele probleme pe care le-am întâmpnat în realizarea proiectului. El s-a ocupat mai mult de partea tehnică, ceea ce îl pasionează foarte mult. 



## Disclaimer: ##

Prin proiectul acesta nu încercăm să ne asumăm meritele pentru Finch, platformă deja existentă (și open-source), ci vrem doar să demonstrăm că pentru 125$ în total el poate fi combinat cu un Raspberry PI și o baterie pentru a deveni autonom și un mijloc superior în mediul educațional.

Resursele folosite se află în fișierul resurseFolosite.md

