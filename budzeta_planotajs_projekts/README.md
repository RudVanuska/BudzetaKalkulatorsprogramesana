# Vienkāršs budžeta plānotājs

Šis ir vienkāršs Python projekts ar Tkinter grafisko saskarni. Programma ļauj lietotājam ievadīt ienākumus un izdevumus, apskatīt ierakstu sarakstu un redzēt kopējo budžeta atlikumu.

## Funkcijas
- Pievienot ienākumu vai izdevumu ierakstu.
- Dzēst izvēlēto ierakstu.
- Notīrīt visus ierakstus.
- Automātiski aprēķināt ienākumus, izdevumus un atlikumu.
- Parādīt kļūdas paziņojumus nepareizas ievades gadījumā.

## Uzstādīšana
Nepieciešams Python 3. Tkinter parasti jau ir iekļauts Python instalācijā.

## Palaišana
Terminālī atver projekta mapi un izpildi komandu:

```bash
python vienkarsa_programma.py
```

## Lietošana
1. Laukā “Nosaukums” ievadi ieraksta nosaukumu, piemēram, “Alga” vai “Pārtika”.
2. Laukā “Summa (€)” ievadi pozitīvu skaitli.
3. Izvēlies kategoriju “Ienākumi” vai “Izdevumi”.
4. Nospied “Pievienot ierakstu”.
5. Vajadzības gadījumā izvēlies ierakstu sarakstā un nospied “Dzēst izvēlēto”.
6. Lai izdzēstu visus ierakstus, nospied “Notīrīt visu”.

## Failu struktūra
```text
vienkarsa_programma.py              Galvenais programmas fails
docs/SRS.md                         Programmas specifikācija
docs/GUI_prototips.md               Saskarnes prototips
docs/Arhitektura_un_datu_plusma.md  Datu plūsmas un arhitektūras apraksts
docs/Testesana_un_kludu_apstrade.md Testēšanas apraksts
screenshots/programma.png           Programmas ekrānuzņēmums
```

## Galvenās funkcijas kodā
`pievienot_ierakstu()` pārbauda lietotāja ievadi un pievieno jaunu ierakstu. `dzest_ierakstu()` izdzēš izvēlēto ierakstu. `notirit_visu()` iztīra sarakstu. `aprekinat_budzetu()` aprēķina kopējos ienākumus, izdevumus, atlikumu un statusu.
