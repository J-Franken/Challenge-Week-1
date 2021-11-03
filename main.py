import excel_bestand_inlezen



def main():
    huidige_punten_dict = {'SE': 0,
                           'IAT': 0,
                           'FICT': 0,
                           'BDaM': 0
                           }

    huidige_punten_dict = excel_bestand_inlezen.excel_inlezen('Database.xlsx')
    # huidige_punten_dict[specialisatie] = huidige_punten_dict[specialisatie] + punten_toevoegen
    print(huidige_punten_dict)

main()
