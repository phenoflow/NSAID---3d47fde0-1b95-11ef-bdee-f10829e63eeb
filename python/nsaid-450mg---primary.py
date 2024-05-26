# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"52338","system":"gprdproduct"},{"code":"7481","system":"gprdproduct"},{"code":"53384","system":"gprdproduct"},{"code":"389","system":"gprdproduct"},{"code":"43045","system":"gprdproduct"},{"code":"5085","system":"gprdproduct"},{"code":"54075","system":"gprdproduct"},{"code":"28553","system":"gprdproduct"},{"code":"50785","system":"gprdproduct"},{"code":"58048","system":"gprdproduct"},{"code":"50602","system":"gprdproduct"},{"code":"29330","system":"gprdproduct"},{"code":"52389","system":"gprdproduct"},{"code":"58071","system":"gprdproduct"},{"code":"53345","system":"gprdproduct"},{"code":"27055","system":"gprdproduct"},{"code":"4692","system":"gprdproduct"},{"code":"5200","system":"gprdproduct"},{"code":"597","system":"gprdproduct"},{"code":"4631","system":"gprdproduct"},{"code":"10481","system":"gprdproduct"},{"code":"50058","system":"gprdproduct"},{"code":"26165","system":"gprdproduct"},{"code":"18798","system":"gprdproduct"},{"code":"24122","system":"gprdproduct"},{"code":"417","system":"gprdproduct"},{"code":"499","system":"gprdproduct"},{"code":"21387","system":"gprdproduct"},{"code":"54518","system":"gprdproduct"},{"code":"9736","system":"gprdproduct"},{"code":"55913","system":"gprdproduct"},{"code":"51099","system":"gprdproduct"},{"code":"51293","system":"gprdproduct"},{"code":"34487","system":"gprdproduct"},{"code":"59595","system":"gprdproduct"},{"code":"39823","system":"gprdproduct"},{"code":"16176","system":"gprdproduct"},{"code":"31950","system":"gprdproduct"},{"code":"57045","system":"gprdproduct"},{"code":"48059","system":"gprdproduct"},{"code":"49059","system":"gprdproduct"},{"code":"57162","system":"gprdproduct"},{"code":"40","system":"gprdproduct"},{"code":"589","system":"gprdproduct"},{"code":"54906","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nsaid-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nsaid-450mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nsaid-450mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nsaid-450mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
