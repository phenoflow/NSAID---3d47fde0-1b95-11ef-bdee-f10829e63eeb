# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"20805","system":"gprdproduct"},{"code":"1496","system":"gprdproduct"},{"code":"34190","system":"gprdproduct"},{"code":"60443","system":"gprdproduct"},{"code":"17126","system":"gprdproduct"},{"code":"19382","system":"gprdproduct"},{"code":"56898","system":"gprdproduct"},{"code":"57475","system":"gprdproduct"},{"code":"24308","system":"gprdproduct"},{"code":"31787","system":"gprdproduct"},{"code":"31589","system":"gprdproduct"},{"code":"31383","system":"gprdproduct"},{"code":"20395","system":"gprdproduct"},{"code":"1210","system":"gprdproduct"},{"code":"35935","system":"gprdproduct"},{"code":"580","system":"gprdproduct"},{"code":"47501","system":"gprdproduct"},{"code":"59880","system":"gprdproduct"},{"code":"754","system":"gprdproduct"},{"code":"38881","system":"gprdproduct"},{"code":"447","system":"gprdproduct"},{"code":"8062","system":"gprdproduct"},{"code":"3432","system":"gprdproduct"},{"code":"18662","system":"gprdproduct"},{"code":"50317","system":"gprdproduct"},{"code":"850","system":"gprdproduct"},{"code":"14476","system":"gprdproduct"},{"code":"4045","system":"gprdproduct"},{"code":"56275","system":"gprdproduct"},{"code":"4625","system":"gprdproduct"},{"code":"9222","system":"gprdproduct"},{"code":"14084","system":"gprdproduct"},{"code":"2904","system":"gprdproduct"},{"code":"11970","system":"gprdproduct"},{"code":"23204","system":"gprdproduct"},{"code":"38992","system":"gprdproduct"},{"code":"46844","system":"gprdproduct"},{"code":"29181","system":"gprdproduct"},{"code":"32854","system":"gprdproduct"},{"code":"4880","system":"gprdproduct"},{"code":"9500","system":"gprdproduct"},{"code":"9688","system":"gprdproduct"},{"code":"58842","system":"gprdproduct"},{"code":"18234","system":"gprdproduct"},{"code":"14672","system":"gprdproduct"},{"code":"17030","system":"gprdproduct"},{"code":"20621","system":"gprdproduct"},{"code":"2243","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nsaid-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nsaid-375mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nsaid-375mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nsaid-375mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
