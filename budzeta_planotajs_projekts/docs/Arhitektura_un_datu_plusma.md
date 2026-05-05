# Datu plūsma un iekšējā arhitektūra

## Datu plūsma
```text
Lietotājs ievada datus
        ↓
Nospiež pogu “Pievienot ierakstu”
        ↓
Funkcija pievienot_ierakstu() pārbauda ievadi
        ↓
Ja dati ir pareizi, ieraksts tiek pievienots sarakstam ieraksti
        ↓
Funkcija atjaunot_rezultatu() pārrēķina ienākumus, izdevumus un atlikumu
        ↓
Rezultāts tiek parādīts GUI logā
```

## Galvenās funkcijas
`pievienot_ierakstu()` nolasa ievadi, pārbauda kļūdas un pievieno ierakstu. `dzest_ierakstu()` dzēš izvēlēto ierakstu no saraksta. `notirit_visu()` iztīra visus ierakstus. `aprekinat_budzetu()` aprēķina ienākumus, izdevumus, atlikumu un statusu.

## Loģiskie lēmumi un datu apstrādes punkti
1. Ja nosaukuma lauks ir tukšs, tiek parādīta kļūda.
2. Ja summas lauks ir tukšs, tiek parādīta kļūda.
3. Ja summu nevar pārveidot par skaitli, tiek parādīta kļūda.
4. Ja summa ir mazāka vai vienāda ar nulli, tiek parādīta kļūda.
5. Ja kategorija nav izvēlēta, tiek parādīta kļūda.
6. Ja kategorija ir “Ienākumi”, summa tiek pieskaitīta ienākumiem.
7. Ja kategorija nav “Ienākumi”, summa tiek pieskaitīta izdevumiem.
8. Ja atlikums ir pozitīvs, programma rāda pozitīva budžeta statusu.
9. Ja atlikums ir nulle, programma rāda līdzsvarota budžeta statusu.
10. Ja atlikums ir negatīvs, programma rāda brīdinājumu par pārsniegtiem izdevumiem.
11. Ja lietotājs mēģina dzēst bez izvēlēta ieraksta, tiek parādīta kļūda.
12. Ja lietotājs mēģina notīrīt tukšu sarakstu, tiek parādīts informatīvs paziņojums.
