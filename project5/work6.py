import csv
class City:
   def __init__(self, row, header):
        self.__dict__ = dict(zip(header, row))

data = list(csv.reader(open('file.csv')))
instances = [City(i, data[0]) for i in data[1:]]
