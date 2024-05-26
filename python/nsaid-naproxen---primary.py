# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"53626","system":"gprdproduct"},{"code":"39693","system":"gprdproduct"},{"code":"34769","system":"gprdproduct"},{"code":"34743","system":"gprdproduct"},{"code":"58708","system":"gprdproduct"},{"code":"51242","system":"gprdproduct"},{"code":"27366","system":"gprdproduct"},{"code":"3053","system":"gprdproduct"},{"code":"34610","system":"gprdproduct"},{"code":"56762","system":"gprdproduct"},{"code":"54476","system":"gprdproduct"},{"code":"55894","system":"gprdproduct"},{"code":"59246","system":"gprdproduct"},{"code":"55486","system":"gprdproduct"},{"code":"60408","system":"gprdproduct"},{"code":"807","system":"gprdproduct"},{"code":"55454","system":"gprdproduct"},{"code":"56106","system":"gprdproduct"},{"code":"54304","system":"gprdproduct"},{"code":"58213","system":"gprdproduct"},{"code":"39317","system":"gprdproduct"},{"code":"52931","system":"gprdproduct"},{"code":"30982","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nsaid-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nsaid-naproxen---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nsaid-naproxen---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nsaid-naproxen---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
