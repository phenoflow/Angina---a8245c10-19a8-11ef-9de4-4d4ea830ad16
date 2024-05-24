# Nathaniel M Hawkins, Shaun Scholes, Madhavi Bajekal, Hande Love, Martin O'Flaherty, Rosalind Raine, Simon Capewell, 2024.

import sys, csv, re

codes = [{"code":"G33z700","system":"readv2"},{"code":"G311100","system":"readv2"},{"code":"G311.13","system":"readv2"},{"code":"4139U","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["unstable-angina---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["unstable-angina---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["unstable-angina---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
