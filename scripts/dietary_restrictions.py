import csv

'''
need to rewrite this for the local database, this assumes you have csv file 
'''

def read_csv(file_path):
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            yield row

def analyze_dietary_restrictions(csv_rows):
  restrictions = {
      "None": 0, 
      "Gluten-Free": 0,
      "Vegan": 0,
      "Lactose-Intolerant": 0,
      "Vegetarian": 0, 
      "No Pork": 0, 
      "No Beef": 0, 
      "Halal": 0, 
      "Kosher": 0, 
      "Other": 0 
  }

  for row in csv_rows:
      drs = row['dietaryRestrictions']
      list = drs[1:-1].split(', ') # slighly problematic for other but i manage by eyeballing

      for i in list:
        dr = i[1:-1] # i hate csv to string including quotes moment 
        if dr not in restrictions.keys():
            print(dr)
            restrictions["Other"] += 1
        else: 
            restrictions[dr] += 1

  print(restrictions)

if __name__ == "__main__":
  file_path = "./registration_apps.csv" 
  csv_rows = read_csv(file_path)
  analyze_dietary_restrictions(csv_rows)