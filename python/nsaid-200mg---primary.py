# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"33357","system":"gprdproduct"},{"code":"37053","system":"gprdproduct"},{"code":"10209","system":"gprdproduct"},{"code":"43032","system":"gprdproduct"},{"code":"29704","system":"gprdproduct"},{"code":"29772","system":"gprdproduct"},{"code":"17754","system":"gprdproduct"},{"code":"30327","system":"gprdproduct"},{"code":"32227","system":"gprdproduct"},{"code":"20386","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nsaid-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nsaid-200mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nsaid-200mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nsaid-200mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
