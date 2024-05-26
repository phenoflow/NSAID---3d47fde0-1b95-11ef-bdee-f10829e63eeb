# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"7524","system":"gprdproduct"},{"code":"21123","system":"gprdproduct"},{"code":"24531","system":"gprdproduct"},{"code":"41623","system":"gprdproduct"},{"code":"47816","system":"gprdproduct"},{"code":"53576","system":"gprdproduct"},{"code":"11495","system":"gprdproduct"},{"code":"5938","system":"gprdproduct"},{"code":"12075","system":"gprdproduct"},{"code":"3409","system":"gprdproduct"},{"code":"37750","system":"gprdproduct"},{"code":"9822","system":"gprdproduct"},{"code":"31064","system":"gprdproduct"},{"code":"3974","system":"gprdproduct"},{"code":"10169","system":"gprdproduct"},{"code":"42604","system":"gprdproduct"},{"code":"4965","system":"gprdproduct"},{"code":"1755","system":"gprdproduct"},{"code":"41621","system":"gprdproduct"},{"code":"24682","system":"gprdproduct"},{"code":"31777","system":"gprdproduct"},{"code":"6663","system":"gprdproduct"},{"code":"29465","system":"gprdproduct"},{"code":"3710","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nsaid-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nsaid-120mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nsaid-120mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nsaid-120mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
