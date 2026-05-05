# Programmas testēšana un kļūdu apstrāde

| Nr. | Testa darbība | Sagaidāmais rezultāts |
|---:|---|---|
| 1 | Nosaukums ir tukšs, summa un kategorija ievadīta | Parādās kļūda “Ievadi nosaukumu!” |
| 2 | Summa ir tukša | Parādās kļūda “Ievadi summu!” |
| 3 | Summas laukā ievada tekstu “abc” | Parādās kļūda “Summai jābūt skaitlim!” |
| 4 | Summas laukā ievada `0` vai negatīvu skaitli | Parādās kļūda “Summai jābūt lielākai par 0!” |
| 5 | Nav izvēlēta kategorija | Parādās kļūda “Izvēlies kategoriju!” |
| 6 | Pievieno ienākumu `600` | Sarakstā parādās ieraksts, ienākumi ir 600.00 € |
| 7 | Pievieno izdevumu `45.50` | Izdevumi palielinās, atlikums tiek pārrēķināts |
| 8 | Dzēš izvēlēto ierakstu | Ieraksts pazūd no saraksta, rezultāts tiek pārrēķināts |
| 9 | Spiež “Dzēst izvēlēto”, neko neiezīmējot | Parādās kļūda “Izvēlies ierakstu, ko dzēst!” |
| 10 | Spiež “Notīrīt visu” tukšam sarakstam | Parādās paziņojums “Nav ko notīrīt.” |

Programma kļūdas apstrādā ar `messagebox.showerror()` un `messagebox.showinfo()`. Nepareizi dati netiek pievienoti sarakstam, tāpēc programma nepārtrauc darbu un paliek lietojama.
