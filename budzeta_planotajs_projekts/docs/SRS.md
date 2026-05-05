# Programmas specifikācija (SRS)

## Projekta mērķis
Programmas mērķis ir izveidot vienkāršu budžeta plānotāju, kur lietotājs var ievadīt ienākumus un izdevumus. Programma aprēķina kopējos ienākumus, kopējos izdevumus un atlikumu, lai lietotājs ātri redzētu budžeta stāvokli.

## Mērķauditorija
Programma paredzēta skolēniem un ikdienas lietotājiem, kuriem vajag vienkārši pierakstīt naudas plūsmu. Lietotājam nav nepieciešamas programmēšanas vai finanšu zināšanas.

## Funkcionālās prasības
Programmai jāļauj ievadīt ieraksta nosaukumu, summu un kategoriju: “Ienākumi” vai “Izdevumi”. Programmai jāspēj pievienot ierakstu sarakstam, dzēst izvēlēto ierakstu, notīrīt visus ierakstus un automātiski pārrēķināt rezultātu.

## Tehniskās prasības
Programma jāizstrādā Python valodā, izmantojot Tkinter grafiskās saskarnes bibliotēku. Programmai jāstrādā lokāli bez interneta pieslēguma un bez ārējām bibliotēkām.

## Ievades validācija
Programmai jāpārbauda, vai nosaukuma lauks nav tukšs, summa ir ievadīta un tā ir pozitīvs skaitlis. Ja lietotājs ievada nepareizus datus, programma parāda kļūdas paziņojumu un neļauj ierakstu pievienot.

## Datu izvade
Programma sarakstā parāda visus ievadītos ierakstus ar nosaukumu, kategoriju un summu. Zem saraksta tiek parādīti kopējie ienākumi, izdevumi, atlikums un īss budžeta statusa teksts.
