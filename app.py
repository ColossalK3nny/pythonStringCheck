from datetime import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
now = datetime.now()
while True:
    # Bekérjük a szériszámokat, és biztosítjuk, hogy nem lehet üres
    while True:
        szeriszam1 = input("Add meg az első szériszámot (vagy írd be 'kilép' a kilépéshez): ")
        if szeriszam1.strip() == 'kilép':  # Kilépés ellenőrzése
            print("Kilépés a programból...")
            exit()
        if szeriszam1.strip() != '':  # Nem engedjük üresen hagyni a bemenetet
            break
        else:
            print(f"{bcolors.WARNING}A szériszám nem lehet üres! Próbáld újra.{bcolors.ENDC}")
    
    while True:
        szeriszam2 = input("Add meg a második szériszámot (vagy írd be 'kilép' a kilépéshez): ")
        if szeriszam2.strip() == 'kilép':  # Kilépés ellenőrzése
            print("Kilépés a programból...")
            exit()
        if szeriszam2.strip() != '':  # Nem engedjük üresen hagyni a bemenetet
            break
        else:
            print(f"{bcolors.WARNING}A szériszám nem lehet üres! Próbáld újra.{bcolors.ENDC}")
    
    # Ellenőrizzük, hogy megegyezik-e a két szériszám
    if szeriszam1 == szeriszam2:
        print(bcolors.OKGREEN + "A két szériszám megegyezik.  \n" + now.strftime('%Y-%m-%d %H:%M:%S') + "\n")
        print('OK OK OK OK OK OK OK OK OK OK\nOK OK OK OK OK OK OK OK OK OK\nOK OK OK OK OK OK OK OK OK OK\nOK OK OK OK OK OK OK OK OK OK\nOK OK OK OK OK OK OK OK OK OK\nOK OK OK OK OK OK OK OK OK OK\n' + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "A két szériszám nem egyezik meg.  \n" + now.strftime('%Y-%m-%d %H:%M:%S') + "\n")
        print("NOK NOK NOK NOK NOK NOK NOK NOK NOK NOK\nNOK NOK NOK NOK NOK NOK NOK NOK NOK NOK\nNOK NOK NOK NOK NOK NOK NOK NOK NOK NOK\nNOK NOK NOK NOK NOK NOK NOK NOK NOK NOK\nNOK NOK NOK NOK NOK NOK NOK NOK NOK NOK\n" + bcolors.ENDC)

print("A program véget ért.")