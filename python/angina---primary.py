# Nathaniel M Hawkins, Shaun Scholes, Madhavi Bajekal, Hande Love, Martin O'Flaherty, Rosalind Raine, Simon Capewell, 2024.

import sys, csv, re

codes = [{"code":"G311200","system":"readv2"},{"code":"G311300","system":"readv2"},{"code":"G330000","system":"readv2"},{"code":"G311400","system":"readv2"},{"code":"14AJ.00","system":"readv2"},{"code":"G33z600","system":"readv2"},{"code":"G311.14","system":"readv2"},{"code":"G33z200","system":"readv2"},{"code":"4139AA","system":"readv2"},{"code":"4139AT","system":"readv2"},{"code":"4139N","system":"readv2"},{"code":"4139C","system":"readv2"},{"code":"4139PA","system":"readv2"},{"code":"4129RE","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["angina---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["angina---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["angina---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
