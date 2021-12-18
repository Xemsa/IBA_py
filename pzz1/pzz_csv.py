import csv

class pzzcsv:

    def __init__(self, mycsvname=''):
        self.Head = ''
        self.List = []
        with open(mycsvname, newline='',encoding='UTF8') as self.csvfile:
            # spamreader = csv.DictReader (csvfile, delimiter=',', quotechar='|')
            self.spamreader = csv.reader(self.csvfile, delimiter=',', quotechar='|')
            self.Head = next(self.spamreader)
            for row in self.spamreader:
                self.List.append(row)

    def getheader(self):
        return self.Head

    def getlist(self):
            # csv_list = ', '.join(row)
            # print(csv_list)
            # print(row)
        return self.List


if __name__ == '__main__':
    import pzz_config
    config = pzz_config.pzzconfig()
    mycsv = config.csv
    Ocsv=pzzcsv(mycsv)
    print(Ocsv.getheader())
    for i in Ocsv.getlist():
        print(i)
