# -*- coding: utf-8 -*-
"""
Práce s listy v Pythonu - Dataset automobilových modelů
Formát: (značka, typ_karoserie, maximální_rychlost_km_h, rok_výroby, cena_v_kc)
"""

# 📊 VYTVOŘENÍ DATASETU
automobily = [
    ("Škoda Octavia", "sedan", 228, 2023, 650000),
    ("Škoda Fabia", "hatchback", 195, 2022, 420000),
    ("Škoda Kodiaq", "SUV", 215, 2023, 950000),
    ("BMW 3 Series", "sedan", 250, 2024, 1200000),
    ("BMW X5", "SUV", 243, 2023, 1800000),
    ("Audi A4", "sedan", 250, 2024, 1100000),
    ("Audi Q7", "SUV", 245, 2023, 2100000),
    ("Mercedes C-Class", "sedan", 250, 2024, 1350000),
    ("Mercedes GLE", "SUV", 240, 2023, 2250000),
    ("Volkswagen Golf", "hatchback", 210, 2023, 580000),
    ("Volkswagen Tiguan", "SUV", 205, 2022, 820000),
    ("Toyota Corolla", "sedan", 180, 2023, 550000),
    ("Toyota RAV4", "SUV", 180, 2024, 890000),
    ("Ford Focus", "hatchback", 200, 2022, 520000),
    ("Ford Mustang", "coupe", 250, 2024, 1650000),
    ("Hyundai i30", "hatchback", 195, 2023, 490000),
    ("Hyundai Tucson", "SUV", 190, 2023, 750000),
    ("Peugeot 308", "hatchback", 215, 2024, 620000),
    ("Porsche 911", "coupe", 293, 2024, 3500000),
    ("Tesla Model 3", "sedan", 261, 2024, 1450000),
]

print("=" * 70)
print("🚗 DATABÁZE AUTOMOBILŮ")
print("=" * 70)
print(f"\nCelkový počet modelů: {len(automobily)}\n")

# Zobrazení prvních 5 aut
print("Ukázka prvních 5 modelů:")
for i, auto in enumerate(automobily[:5], 1):
    znacka, typ, rychlost, rok, cena = auto
    print(f"{i}. {znacka} ({typ}) - {rychlost} km/h, {rok}, {cena:,} Kč".replace(",", " "))

print("\n" + "=" * 70)
print("🔍 FILTROVÁNÍ SEZNAMU")
print("=" * 70)

# 1. Filtrování podle typu karoserie
print("\n1️⃣ SUV modely:")
suv_modely = [auto for auto in automobily if auto[1] == "SUV"]
for auto in suv_modely:
    print(f"   • {auto[0]} - {auto[2]} km/h, {auto[4]:,} Kč".replace(",", " "))

# 2. Filtrování podle rychlosti
print("\n2️⃣ Auta s maximální rychlostí nad 240 km/h:")
rychla_auta = [auto for auto in automobily if auto[2] > 240]
for auto in rychla_auta:
    print(f"   • {auto[0]} - {auto[2]} km/h")

# 3. Filtrování podle ceny
print("\n3️⃣ Auta do 600 000 Kč:")
levna_auta = [auto for auto in automobily if auto[4] <= 600000]
for auto in levna_auta:
    print(f"   • {auto[0]} - {auto[4]:,} Kč".replace(",", " "))

# 4. Kombinované filtrování
print("\n4️⃣ Sedany rychlejší než 240 km/h:")
rychle_sedany = [auto for auto in automobily if auto[1] == "sedan" and auto[2] > 240]
for auto in rychle_sedany:
    print(f"   • {auto[0]} - {auto[2]} km/h, {auto[4]:,} Kč".replace(",", " "))

print("\n" + "=" * 70)
print("📊 ŘAZENÍ PODLE RŮZNÝCH ATRIBUTŮ")
print("=" * 70)

# 1. Řazení podle rychlosti (sestupně)
print("\n1️⃣ TOP 5 nejrychlejších aut:")
serazene_podle_rychlosti = sorted(automobily, key=lambda x: x[2], reverse=True)
for i, auto in enumerate(serazene_podle_rychlosti[:5], 1):
    print(f"   {i}. {auto[0]} - {auto[2]} km/h")

# 2. Řazení podle ceny (vzestupně)
print("\n2️⃣ TOP 5 nejlevnějších aut:")
serazene_podle_ceny = sorted(automobily, key=lambda x: x[4])
for i, auto in enumerate(serazene_podle_ceny[:5], 1):
    print(f"   {i}. {auto[0]} - {auto[4]:,} Kč".replace(",", " "))

# 3. Řazení podle roku výroby
print("\n3️⃣ Nejnovější modely (rok 2024):")
modely_2024 = sorted([auto for auto in automobily if auto[3] == 2024], 
                     key=lambda x: x[2], reverse=True)
for auto in modely_2024:
    print(f"   • {auto[0]} - {auto[2]} km/h")

# 4. Řazení podle značky (abecedně)
print("\n4️⃣ Seřazeno podle značky (prvních 8):")
serazene_abecedne = sorted(automobily, key=lambda x: x[0])
for auto in serazene_abecedne[:8]:
    print(f"   • {auto[0]}")

print("\n" + "=" * 70)
print("📈 POPISNÉ STATISTIKY")
print("=" * 70)

# Extrakce jednotlivých atributů
rychlosti = [auto[2] for auto in automobily]
roky = [auto[3] for auto in automobily]
ceny = [auto[4] for auto in automobily]

# Statistiky rychlosti
print("\n🏁 Rychlost (km/h):")
print(f"   • Průměr: {sum(rychlosti) / len(rychlosti):.1f} km/h")
print(f"   • Minimum: {min(rychlosti)} km/h")
print(f"   • Maximum: {max(rychlosti)} km/h")
print(f"   • Medián: {sorted(rychlosti)[len(rychlosti)//2]} km/h")

# Statistiky cen
print("\n💰 Cena (Kč):")
print(f"   • Průměr: {sum(ceny) / len(ceny):,.0f} Kč".replace(",", " "))
print(f"   • Minimum: {min(ceny):,} Kč".replace(",", " "))
print(f"   • Maximum: {max(ceny):,} Kč".replace(",", " "))
print(f"   • Medián: {sorted(ceny)[len(ceny)//2]:,} Kč".replace(",", " "))

# Statistiky typů karoserie
typy = [auto[1] for auto in automobily]
from collections import Counter
pocet_typu = Counter(typy)
print("\n🚙 Rozdělení podle typu karoserie:")
for typ, pocet in pocet_typu.most_common():
    print(f"   • {typ}: {pocet} modelů")

# Statistiky značek
znacky = [auto[0].split()[0] for auto in automobily]  # První slovo = značka
pocet_znacek = Counter(znacky)
print("\n🏢 Počet modelů podle značky:")
for znacka, pocet in sorted(pocet_znacek.items()):
    print(f"   • {znacka}: {pocet} model(ů)")

print("\n" + "=" * 70)
print("📊 GRAFICKÁ REPREZENTACE")
print("=" * 70)

# Histogram rychlostí (ASCII verze)
print("\n📈 Histogram maximálních rychlostí (rozděleno po 20 km/h):\n")

# Vytvoření intervalů
intervaly = {}
for rychlost in rychlosti:
    interval = (rychlost // 20) * 20
    intervaly[interval] = intervaly.get(interval, 0) + 1

# Seřazení intervalů
serazene_intervaly = sorted(intervaly.items())

# Vykreslení ASCII histogramu
max_pocet = max(intervaly.values())
for interval, pocet in serazene_intervaly:
    blok = "█" * int(pocet * 30 / max_pocet)
    print(f"   {interval}-{interval+19} km/h: {blok} ({pocet})")

# Histogram cen
print("\n💰 Histogram cen (v milionech Kč):\n")

ceny_v_milionech = [cena / 1000000 for cena in ceny]
intervaly_cen = {}
for cena in ceny_v_milionech:
    if cena < 0.5:
        kluc = "0.0-0.5"
    elif cena < 1.0:
        kluc = "0.5-1.0"
    elif cena < 1.5:
        kluc = "1.0-1.5"
    elif cena < 2.0:
        kluc = "1.5-2.0"
    elif cena < 2.5:
        kluc = "2.0-2.5"
    else:
        kluc = "2.5+"
    intervaly_cen[kluc] = intervaly_cen.get(kluc, 0) + 1

# Vykreslení
poradi = ["0.0-0.5", "0.5-1.0", "1.0-1.5", "1.5-2.0", "2.0-2.5", "2.5+"]
max_pocet_cen = max(intervaly_cen.values())
for interval in poradi:
    pocet = intervaly_cen.get(interval, 0)
    if pocet > 0:
        blok = "█" * int(pocet * 30 / max_pocet_cen)
        label = f"{interval} mil. Kč:".ljust(20)
        print(f"   {label} {blok} ({pocet})")

print("\n" + "=" * 70)
print("✅ ANALÝZA DOKONČENA")
print("=" * 70)
print("\n💡 Zajímavá zjištění:")
print(f"   • Nejrychlejší auto: {serazene_podle_rychlosti[0][0]} ({serazene_podle_rychlosti[0][2]} km/h)")
print(f"   • Nejdražší auto: {sorted(automobily, key=lambda x: x[4], reverse=True)[0][0]}")
print(f"   • Nejoblíbenější typ: {pocet_typu.most_common(1)[0][0]} ({pocet_typu.most_common(1)[0][1]} modelů)")
print(f"   • Průměrná cena: {sum(ceny) / len(ceny):,.0f} Kč".replace(",", " "))