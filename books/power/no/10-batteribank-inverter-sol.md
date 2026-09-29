# Batteribank, inverter og sol

Batterier er stille og gir ingen eksos der de brukes. Det gjør dem spesielt attraktive i leiligheter og til små/mellomstore laster.

## Nominell kapasitet er startpunktet

Et 12 V, 100 Ah batteri tilsvarer nominelt:

`12 V × 100 Ah = 1200 Wh`

Det betyr **ikke** at 1200 Wh nødvendigvis kan leveres til et 230 V-apparat. Brukbar kapasitet avhenger blant annet av batteritype, tillatt utlading, temperatur, alder og konverteringstap.

Boken bruker derfor to verdier:

- **nominell energi**
- **planlagt brukbar energi**

Antakelsen mellom dem skal alltid være synlig.

## Inverter

En inverter konverterer DC til AC. Den må både:

1. tåle kontinuerlig effekt
2. tåle nødvendig start-/toppeffekt
3. være egnet for utstyret som kobles til

En 2000 W inverter gjør ikke et 1200 Wh batteri til et 2000 Wh batteri. Effektkapasitet og energikapasitet er forskjellige størrelser.

## Eksempel: 500 Wh brukbar energi

Dersom vi allerede har fastslått at systemet kan levere **500 Wh brukbar energi**, blir idealisert kjøretid:

- 10 W last → 50 timer
- 50 W last → 10 timer
- 100 W last → 5 timer
- 500 W last → 1 time

Dette er matematikk, ikke et løfte om faktisk kjøretid. Virkelige laster, temperatur og systemtap må inn i planleggingen.

## Power station

En portabel power station kombinerer typisk batteri, lader, styring og flere utganger i én enhet. Evaluer den etter:

- brukbar Wh
- DC/USB-utganger
- kontinuerlig AC-effekt
- toppeffekt
- ladetid
- hvilke ladekilder den støtter
- temperaturbegrensninger
- om batteriet kan vedlikeholdes/erstattes

Ikke kjøp etter «W» alene.

## Sol

Solpanel kan fylle på batteriet og forlenge utholdenheten, men solproduksjon er variabel.

Skill mellom:

- panelets nominelle W
- faktisk energi høstet i Wh per dag
- lade-/konverteringstap
- årstid
- vær
- orientering og skygge

I Norge er forskjellen mellom sommer og vinter så viktig at en vinterplan ikke skal baseres på sommerproduksjon.

## Hybridplan

For et hus kan en robust løsning være:

**batteri → stille kontinuerlige små laster → aggregat i avgrensede perioder → lading av batteri + utvalgte store laster**

Da slipper aggregatet nødvendigvis å gå kontinuerlig.

I en leilighet er batteri/power station ofte langt mer praktisk enn forbrenningsbasert produksjon, men energibudsjettet må da være desto strengere.


## Behold driftsmoduser

Definer minst tre moduser: normal beredskapsdrift, sparemodus og minimumsdrift. Bestem hvilke laster som kobles bort på hvert trinn før batteriet nærmer seg tomt.

Reserver energi til funksjonene som betyr mest, i stedet for å behandle alle tilgjengelige wattimer som umiddelbart forbrukbare.

## Mål det virkelige systemet

For hver kritiske last registrerer du målt eller dokumentert effekt, timer per døgn, eventuell driftssyklus, starteffekt og om AC-konvertering er nødvendig.

Test deretter hele kjeden du faktisk skal bruke: lader, batteri, inverter eller DC-utgang, kabel og apparat. Reell beredskapskapasitet er den kapasiteten systemet kan levere sikkert og repeterbart, ikke bare tallet som står på én komponent.

## Sikkerhet må følge batterikjemien

Batteribank, lader, kabling, sikring, inverter og eventuell solregulator er ett elektrisk system. Følg produsentens grenser for den konkrete batterikjemien og utstyret, og bruk komponenter og beskyttelse som er beregnet for systemets spenning og strøm.

Boka skal ikke anta universelle temperaturgrenser, ladegrenser eller ventilasjonskrav på tvers av batterikjemier. Slike sikkerhetskritiske grenser må kvalifiseres mot primærkilder før de oppgis som konkrete tall eller regler.
