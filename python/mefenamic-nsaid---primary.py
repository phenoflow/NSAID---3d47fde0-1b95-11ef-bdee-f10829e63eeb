# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"4710","system":"gprdproduct"},{"code":"259","system":"gprdproduct"},{"code":"34595","system":"gprdproduct"},{"code":"51827","system":"gprdproduct"},{"code":"46967","system":"gprdproduct"},{"code":"34438","system":"gprdproduct"},{"code":"34793","system":"gprdproduct"},{"code":"32090","system":"gprdproduct"},{"code":"34924","system":"gprdproduct"},{"code":"32234","system":"gprdproduct"},{"code":"32105","system":"gprdproduct"},{"code":"34910","system":"gprdproduct"},{"code":"41524","system":"gprdproduct"},{"code":"57007","system":"gprdproduct"},{"code":"34898","system":"gprdproduct"},{"code":"1073","system":"gprdproduct"},{"code":"57297","system":"gprdproduct"},{"code":"41677","system":"gprdproduct"},{"code":"46968","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nsaid-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["mefenamic-nsaid---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["mefenamic-nsaid---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["mefenamic-nsaid---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
