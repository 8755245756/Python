import ipaddress
import pandas as pd
import openpyxl
import csv
from pathlib import Path
p = Path("C:\\Users\\Administrator\\Desktop\\ip addr\\mate test.xlsx_files\\")
for csvfile in p.glob('*.csv'):
    Xn=csvfile
    filepath = Xn
    print(Xn)
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # skip the column
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                sNetwork_ID=row[0]
                sEmail_To = row[1]
    print(sNetwork_ID[-2:])
    #svd = pd.read_excel('MATE.xlsx')
    #Email_To = pd.DataFrame(svd,columns= ['Email To'])
    Email=[sEmail_To]*256
    #Network_ID = pd.DataFrame(svd, columns= ['Network ID'])
    subnet =[]
    data = {'ipaddr':subnet,
            'Email': Email}
    def get_all_ips_by_subnet(subnet):
        l = [*map(str, ipaddress.IPv4Network(subnet, strict=False))]
        return l
    for l in get_all_ips_by_subnet(sNetwork_ID):
        subnet.append(l)
    df = pd.DataFrame(data)
    df.to_csv(input()+'vlookupup_mate.csv')
    df
