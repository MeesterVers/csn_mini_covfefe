# `Covfefe` alarm systeem
## Vak: CSN Alarm systeem

**_Het systeem_**<br>
Covfefe alarm systeem is een systeem dat bestaat uit een server Raspberry Pi, en een client(s) Raspberry Pi. Alle Pi's draaien op het **Raspbian** bestuurings systeem.

**_Systeem installatie_**<br>
Om het systeem werkend te krijgen moet je de volgende stappen uitvoeren. Er is ook een video van hoe het systeem aan de client side een beetje in elkaar zit. De video is te vinden op deze link **[https://youtu.be/eAzqxVyyy_g]**

1. De **Git repo (https://github.com/MeesterVers/csn_mini_covfefe)** moet gefetch of gepulled worden.

2. De volgende genoemde files en folder moeten in de directory `\pi\` op de alarm (client) pi.<br>
    -`1.mp3`
	-`2.mp3`<br>
	-`3.mp3`<br>
	-`4.mp3`<br>
	-`5.mp3`<br>
	-`beep.mp3`<br>
	-`bashscript.sh`<br>
	-`camerascriptpy.py`<br>
	-`\webcam\`

3. Op de server pi moet aleen de file `server.py` fetched, pulled of gedownload worden.

4. De ipadress van de server pi moet je veranderen naar **192.168.42.2**

5. Op de server pi moet de file `server.py` open gemaakt worden in  het programma **Thornny** moet er op **Run** gedrukt worden

6. Op de client pi moet dan de file `camerascriptpy.py` open gemaakt worden in het programma **Thornny**. Daarna moet er op **run** gedrukt worden.

7. Als de client pi connected met de server is moet de gebruiker dan een taal kiezen. 1 voor Engels, 2 voor Duits, 3 voor Japans, 4 voor Spaans, 5 voor Frans

8. Daarna moet de gebruiker de wachtwoord invoeren. De wachtwoorden zijn: `bingo673`, `wachtwoord` en`geheim`

9. Het alarm kan dan geactiveerd worden door het knopje te drukken. Er wordt dan een bericht gestuurd naar de server pi dat dat het alarm geactiveerd is. Tegelijkertijd wordt er een foto gemaakt met de USB camera, er gaat een LED branden op het alarm, een buzzer gaat ook af op het alarm en een timer van 20 seconden gaat in.

10. Als het alarm (**triggered**) kan worden uitgeschakeld door de server als deze een bericht naar het alarm toe stuurt.

11. Als de server het alarm uitschakeld binnen 20 seconden zal het alarm een deactivatie mail sturen naar het emailadres van de gebruiker van het alarm.

12. Als de server het alarm niet binnen 20 seconden uitzet, gaat het alarm een ander geluid maken in de gekozen taal tot het uitgezet wordt door de server. Ook zal het alarm een mail sturen naar de gebruiker van het alarm.