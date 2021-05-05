# created by oprabin on 2021-05-04.

import csv

with open('../input/input_pa_engine_DATA.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row[0])
        with open('../output/output_rbp_DATA.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([row[8], row[52], row[42], row[172], row[159], row[179], row[181], row[187], row[193], row[194], row[103], row[200], row[174], row[175], row[39], row[41], row[77], row[74], row[76], row[189], row[108], row[110], row[112], row[114], row[116], row[118], row[120], row[122], row[124], row[126], row[128], row[130], row[132], row[134], row[136], row[138], row[140], row[142], row[144], row[146], row[148], row[150], row[152], row[154], row[156]])


