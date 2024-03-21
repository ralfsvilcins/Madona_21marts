def ierakstit_vardu_faila(vards, fails):
    try:
        with open(fails, 'a') as f:
            f.write(vards + '\n')
        print("Vārds veiksmīgi ierakstīts failā.")
    except IOError:
        print("Kļūda: Nevarēja piekļūt failam vai rakstīt failā.")

if __name__ == "__main__":
    fails = "lietotajs.txt"
    while True:
        vards = input("Ievadiet savu vārdu (vai 'iziet', lai pabeigtu): ")
        if vards.lower() == 'iziet':
            break
        ierakstit_vardu_faila(vards, fails)
