import tkinter as tk
from tkinter import messagebox

ieraksti = []


def parveidot_summu(summa_teksts):
    try:
        summa = float(summa_teksts.replace(",", "."))
    except ValueError:
        return None
    return summa


def aprekinat_budzetu(dati):
    ienakumi = 0
    izdevumi = 0

    for ieraksts in dati:
        if ieraksts["kategorija"] == "Ienākumi":
            ienakumi += ieraksts["summa"]
        else:
            izdevumi += ieraksts["summa"]

    atlikums = ienakumi - izdevumi

    if atlikums > 0:
        statuss = "Budžets ir pozitīvs."
    elif atlikums == 0:
        statuss = "Budžets ir līdzsvarā."
    else:
        statuss = "Izdevumi pārsniedz ienākumus."

    return ienakumi, izdevumi, atlikums, statuss


def atjaunot_rezultatu():
    ienakumi, izdevumi, atlikums, statuss = aprekinat_budzetu(ieraksti)
    rezultats.config(
        text=f"Ienākumi: {ienakumi:.2f} €\n"
             f"Izdevumi: {izdevumi:.2f} €\n"
             f"Atlikums: {atlikums:.2f} €\n"
             f"{statuss}"
    )


def pievienot_ierakstu():
    nosaukums = nosaukums_ievade.get().strip()
    summa_teksts = summa_ievade.get().strip()
    kategorija = kategorija_var.get()

    if not nosaukums:
        messagebox.showerror("Kļūda", "Ievadi nosaukumu!")
        return

    if not summa_teksts:
        messagebox.showerror("Kļūda", "Ievadi summu!")
        return

    summa = parveidot_summu(summa_teksts)

    if summa is None:
        messagebox.showerror("Kļūda", "Summai jābūt skaitlim!")
        return

    if summa <= 0:
        messagebox.showerror("Kļūda", "Summai jābūt lielākai par 0!")
        return

    if kategorija == "Izvēlies kategoriju":
        messagebox.showerror("Kļūda", "Izvēlies kategoriju!")
        return

    ieraksti.append({"nosaukums": nosaukums, "summa": summa, "kategorija": kategorija})
    saraksts.insert(tk.END, f"{nosaukums} | {kategorija} | {summa:.2f} €")
    nosaukums_ievade.delete(0, tk.END)
    summa_ievade.delete(0, tk.END)
    atjaunot_rezultatu()


def dzest_ierakstu():
    izvele = saraksts.curselection()

    if not izvele:
        messagebox.showerror("Kļūda", "Izvēlies ierakstu, ko dzēst!")
        return

    indekss = izvele[0]
    saraksts.delete(indekss)
    ieraksti.pop(indekss)
    atjaunot_rezultatu()


def notirit_visu():
    if not ieraksti:
        messagebox.showinfo("Informācija", "Nav ko notīrīt.")
        return

    ieraksti.clear()
    saraksts.delete(0, tk.END)
    atjaunot_rezultatu()


logs = tk.Tk()
logs.title("Vienkāršs budžeta plānotājs")
logs.geometry("430x520")
logs.resizable(False, False)

virsraksts = tk.Label(logs, text="Budžeta plānotājs", font=("Arial", 18, "bold"))
virsraksts.pack(pady=10)

instrukcija = tk.Label(logs, text="Ievadi ienākumus vai izdevumus un apskati atlikumu.")
instrukcija.pack()

forma = tk.Frame(logs)
forma.pack(pady=10)

tk.Label(forma, text="Nosaukums:").grid(row=0, column=0, sticky="w", pady=4)
nosaukums_ievade = tk.Entry(forma, width=28)
nosaukums_ievade.grid(row=0, column=1, pady=4)

tk.Label(forma, text="Summa (€):").grid(row=1, column=0, sticky="w", pady=4)
summa_ievade = tk.Entry(forma, width=28)
summa_ievade.grid(row=1, column=1, pady=4)

tk.Label(forma, text="Kategorija:").grid(row=2, column=0, sticky="w", pady=4)
kategorija_var = tk.StringVar(value="Izvēlies kategoriju")
kategorija_menu = tk.OptionMenu(forma, kategorija_var, "Ienākumi", "Izdevumi")
kategorija_menu.grid(row=2, column=1, sticky="ew", pady=4)

poga_pievienot = tk.Button(logs, text="Pievienot ierakstu", command=pievienot_ierakstu, width=25)
poga_pievienot.pack(pady=5)

saraksts = tk.Listbox(logs, width=55, height=10)
saraksts.pack(pady=10)

pogu_rinda = tk.Frame(logs)
pogu_rinda.pack()

tk.Button(pogu_rinda, text="Dzēst izvēlēto", command=dzest_ierakstu, width=18).grid(row=0, column=0, padx=5)
tk.Button(pogu_rinda, text="Notīrīt visu", command=notirit_visu, width=18).grid(row=0, column=1, padx=5)

rezultats = tk.Label(
    logs,
    text="Ienākumi: 0.00 €\nIzdevumi: 0.00 €\nAtlikums: 0.00 €",
    font=("Arial", 12),
    justify="left"
)
rezultats.pack(pady=15)

logs.mainloop()
