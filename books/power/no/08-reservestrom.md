# Reservestrøm

Reservestrøm begynner med behov, ikke produkt. Lag tre lister: **må fungere**, **bør fungere** og **komfort**.

## W og Wh

**Watt (W)** forteller hvor stor effekt en last krever akkurat nå. **Wattimer (Wh)** forteller hvor mye energi som brukes over tid.

En last på 10 W i 5 timer bruker ideelt:

`10 W × 5 h = 50 Wh`

En last på 100 W i 4 timer bruker:

`100 W × 4 h = 400 Wh`

Dette er grunnlaget for hele energiplanen.

## Mål før du kjøper

For hver viktig last registreres:

- målt eller dokumentert effekt
- timer per døgn eller faktisk driftssyklus
- om lasten har motor/kompressor og høy startstrøm
- om den virkelig trenger 230 V
- hvor mange døgn den må kunne drives

Måling på eget utstyr er bedre enn generiske tabellverdier. Et kjøleskap trekker for eksempel ikke nødvendigvis merkestrømeffekt kontinuerlig.

## Fra last til døgnenergi

Eksempel, kun for å vise metoden:

| Last | Effekt | Bruk | Energi |
| --- | ---: | ---: | ---: |
| LED-lys | 5 W | 5 h | 25 Wh |
| Router | 10 W | 8 h | 80 Wh |
| Radio | 3 W | 4 h | 12 Wh |
| Telefonlading | målt/estimert | per lading | registreres |

Summer wattimer, ikke bare watt. Deretter bestemmes hvilke laster som kan kuttes dersom hendelsen varer lenger.

## Tre energinivåer

### Nivå A — USB/DC

Telefoner, små lamper, radio og enkelte nettverksenheter kan ofte drives direkte fra USB eller DC. Det unngår unødvendig invertertap.

### Nivå B — batteribank/power station

Når flere laster eller 230 V-utstyr skal drives, blir en større batteribank aktuell. Kapasiteten må sammenlignes med døgnbudsjettet, ikke bare produktets markedsførte effekt.

### Nivå C — aggregat eller annen produksjon

Langvarige og store laster kan kreve energiproduksjon i tillegg til lagring. Aggregat og sol behandles som energikilder med egne begrensninger, ikke som uendelig strøm.

## Prioritering under hendelsen

Planen skal ha minst tre driftsmoduser:

1. **normal beredskapsdrift** — planlagte kritiske laster
2. **sparedrift** — bare det viktigste
3. **minimumsdrift** — kommunikasjon, nødvendig lys og andre reelt kritiske behov

`ploos-prep` skal gjøre disse scenariene sammenlignbare uten å skjule antakelsene.
