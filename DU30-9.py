def najdi_nejvetsi_cislo(data):
    nejvetsi = None

    with open(data, "r", encoding="utf-8") as soubor:
        for radek in soubor:
            radek = radek.strip()
            if radek:
                cislo = int(radek)
                if nejvetsi is None or cislo > nejvetsi:
                    nejvetsi = cislo

    if nejvetsi is not None:
        print(f"Největší číslo v souboru je: {nejvetsi}")

najdi_nejvetsi_cislo("data.txt")