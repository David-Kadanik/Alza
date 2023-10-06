kategorie = ["stolní počítače", "notebooky", "mobily"]
produkty = {
    "stolní počítače": {
        "Dědův pc": 15000,
        "HP pro gamer master pc": 50000,
        "Battlebox raptor-mamtraktor": 20000
    },
    "notebooky": {
        "MamBook air 13": 22000,
        "LenoMamHleno youga slim 7": 14000,
        "AcerMacer aspire 5": 16000
    },
    "mobily": {
        "Xiaomi big chilling 3000": 6000,
        "Slamsung gutsmaxy 12": 8000,
        "Iphone 30 super delux edition": 100000
    }
}
# inicializuje seznamy pro ukládání vybraných věcí
vybrane_produkty = {kategorie: [] for kategorie in kategorie}
# smyčka pod kterou to celé běží 
while True:
    print("\nVítejte v Alze!")
    print("Máte na výběr z :\n")
    for i, k in enumerate(kategorie):
        print(f"{i + 1}. {k}")
    print("Pro ukončení nákupu kliknětě 4")   
    
   
    vyber_k = int(input("\nVyberte číslo kategorie (1-3): ")) - 1 
#ukonci smyčku    
    if vyber_k == 3 :
        break

    elif vyber_k < 0 or vyber_k >= len(kategorie) :
        print("Neplatná volba kategorie. Zkuste to znovu.")
        continue 

    

    jmkategorie = kategorie[vyber_k]  

    print(f"\nProdukty v kategorii {jmkategorie}:")
    for i, produkt in enumerate(produkty[jmkategorie].keys()):
        cena = produkty[jmkategorie][produkt]

        print(f"{i + 1}. {produkt} - cena: {cena} Kč ")
    volba_produktu = int(input("\n Vyberte číslo produktu (1-3): ")) - 1
    produkty_v_kategorii = list(produkty[jmkategorie].keys())  
#podminka pro neplatnou volbu     
    if volba_produktu < 0 or volba_produktu >= len(produkty_v_kategorii):
        print("Neplatná volba produktu. Zkuste to znovu.")
        continue

    vybrany_produkt = produkty_v_kategorii[volba_produktu]
# ulozi vybrané produkty
    vybrane_produkty[jmkategorie].append(vybrany_produkt)
 
# vypíše cenu 
print("\nVaše zakoupené položky:")
celkova_cena = 0
for jmkategorie, produkty_v_kategorii in vybrane_produkty.items():
    cena = sum(produkty[jmkategorie][produkt] for produkt in produkty_v_kategorii)
    print(f"{jmkategorie}: {', '.join(produkty_v_kategorii)} - cena: {cena} Kč")
    celkova_cena += cena
print(f"Celková cena nákupu: {celkova_cena} Kč")
print("Děkujeme za nákup!")


