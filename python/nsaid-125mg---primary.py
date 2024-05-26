# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"3958","system":"gprdproduct"},{"code":"33994","system":"gprdproduct"},{"code":"612","system":"gprdproduct"},{"code":"57006","system":"gprdproduct"},{"code":"35711","system":"gprdproduct"},{"code":"11215","system":"gprdproduct"},{"code":"34091","system":"gprdproduct"},{"code":"32108","system":"gprdproduct"},{"code":"24121","system":"gprdproduct"},{"code":"31944","system":"gprdproduct"},{"code":"25329","system":"gprdproduct"},{"code":"18448","system":"gprdproduct"},{"code":"9637","system":"gprdproduct"},{"code":"7667","system":"gprdproduct"},{"code":"497","system":"gprdproduct"},{"code":"53164","system":"gprdproduct"},{"code":"24128","system":"gprdproduct"},{"code":"5407","system":"gprdproduct"},{"code":"40756","system":"gprdproduct"},{"code":"649","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nsaid-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nsaid-125mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nsaid-125mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nsaid-125mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
