# GitHub versiju vēstures plāns

Šo projektu var ievietot GitHub krātuvē ar šādām komandām:

```bash
git init
git add .
git commit -m "Izveidota projekta struktūra un SRS"
git commit -m "Pievienots Tkinter GUI prototips"
git commit -m "Pievienota budžeta aprēķinu loģika"
git commit -m "Pievienota ievades validācija un kļūdu apstrāde"
git commit -m "Pievienota dokumentācija un prezentācija"
git branch -M main
git remote add origin https://github.com/LIETOTAJVARDS/budzeta-planotajs.git
git push -u origin main
```

Reālajā izstrādē katrs `commit` jāveic pēc konkrētas pabeigtas darba daļas. Tas ļauj redzēt projekta attīstības vēsturi un atgriezties pie iepriekšējas versijas, ja kodā rodas kļūda.
